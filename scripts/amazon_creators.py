#!/usr/bin/env python3
"""Amazon Creators API の接続確認と商品情報取得を行う補助スクリプト。"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, Iterable, List


ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
API_ENDPOINT = "https://creatorsapi.amazon/catalog/v1/getItems"
SEARCH_ENDPOINT = "https://creatorsapi.amazon/catalog/v1/searchItems"
BOOKS_PATH = ROOT / "data" / "amazon_books.json"
TOKEN_ENDPOINTS = {
    "3.1": "https://api.amazon.com/auth/o2/token",
    "3.2": "https://api.amazon.co.uk/auth/o2/token",
    "3.3": "https://api.amazon.co.jp/auth/o2/token",
}


def load_dotenv(path: Path) -> None:
    """依存パッケージを使わず、単純な KEY=VALUE 形式の .env を読み込む。"""
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if value[:1] == value[-1:] and value.startswith(("'", '"')):
            value = value[1:-1]
        os.environ.setdefault(key, value)


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"{name} が設定されていません。")
    return value


def request_json(
    url: str,
    *,
    payload: Dict[str, object],
    headers: Dict[str, str],
) -> Dict[str, object]:
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Amazon API が HTTP {error.code} を返しました: {detail}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"Amazon API に接続できませんでした: {error.reason}") from error


def fetch_access_token() -> str:
    credential_id = require_env("AMAZON_CREATORS_CREDENTIAL_ID")
    secret = require_env("AMAZON_CREATORS_SECRET")
    version = os.environ.get("AMAZON_CREATORS_VERSION", "3.3").strip()

    try:
        endpoint = TOKEN_ENDPOINTS[version]
    except KeyError as error:
        supported = ", ".join(TOKEN_ENDPOINTS)
        raise RuntimeError(
            f"認証情報バージョン {version} には未対応です。対応バージョン: {supported}"
        ) from error

    response = request_json(
        endpoint,
        payload={
            "grant_type": "client_credentials",
            "client_id": credential_id,
            "client_secret": secret,
            "scope": "creatorsapi::default",
        },
        headers={"Content-Type": "application/json"},
    )
    token = str(response.get("access_token", ""))
    if not token:
        raise RuntimeError("アクセストークンが応答に含まれていません。")
    return token


def chunks(values: List[str], size: int) -> Iterable[List[str]]:
    for index in range(0, len(values), size):
        yield values[index : index + size]


def fetch_items(asins: List[str]) -> List[Dict[str, object]]:
    token = fetch_access_token()
    partner_tag = require_env("AMAZON_PARTNER_TAG")
    marketplace = os.environ.get("AMAZON_MARKETPLACE", "www.amazon.co.jp").strip()
    items: List[Dict[str, object]] = []

    for batch in chunks(asins, 10):
        response = request_json(
            API_ENDPOINT,
            payload={
                "itemIds": batch,
                "itemIdType": "ASIN",
                "languagesOfPreference": ["ja_JP"],
                "marketplace": marketplace,
                "partnerTag": partner_tag,
                "resources": [
                    "images.primary.large",
                    "itemInfo.title",
                ],
            },
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "x-marketplace": marketplace,
            },
        )

        for error in response.get("errors", []):
            print(
                f"警告: {error.get('code', 'UnknownError')}: "
                f"{error.get('message', '')}",
                file=sys.stderr,
            )
        result = response.get("itemsResult") or {}
        items.extend(result.get("items") or [])

    return items


def search_book_candidates() -> List[Dict[str, object]]:
    token = fetch_access_token()
    partner_tag = require_env("AMAZON_PARTNER_TAG")
    marketplace = os.environ.get("AMAZON_MARKETPLACE", "www.amazon.co.jp").strip()
    catalog = json.loads(BOOKS_PATH.read_text(encoding="utf-8"))
    results: List[Dict[str, object]] = []

    for index, book in enumerate(catalog["books"]):
        if index:
            time.sleep(1.1)

        response = request_json(
            SEARCH_ENDPOINT,
            payload={
                "keywords": book["title"],
                "itemCount": 5,
                "languagesOfPreference": ["ja_JP"],
                "marketplace": marketplace,
                "partnerTag": partner_tag,
                "searchIndex": "Books",
                "resources": [
                    "images.primary.large",
                    "itemInfo.byLineInfo",
                    "itemInfo.title",
                ],
            },
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "x-marketplace": marketplace,
            },
        )
        search_result = response.get("searchResult") or {}
        candidates = []
        for item in search_result.get("items") or []:
            title = ((item.get("itemInfo") or {}).get("title") or {}).get(
                "displayValue", ""
            )
            candidates.append(
                {
                    "asin": item.get("asin", ""),
                    "title": title,
                    "detailPageURL": item.get("detailPageURL", ""),
                }
            )
        results.append(
            {
                "id": book["id"],
                "requestedTitle": book["title"],
                "candidates": candidates,
            }
        )

    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("check", help="認証情報を使ってトークン取得だけを確認する")

    get_items = subparsers.add_parser(
        "get-items", help="ASINから商品画像URL・商品URL・タイトルを取得する"
    )
    get_items.add_argument("asins", nargs="+", help="10桁のASIN。複数指定可能")
    subparsers.add_parser(
        "find-asins", help="amazon_books.json の書名からASIN候補を検索する"
    )
    return parser.parse_args()


def main() -> int:
    load_dotenv(ENV_PATH)
    args = parse_args()

    try:
        if args.command == "check":
            fetch_access_token()
            print("Creators API の認証に成功しました。")
            return 0

        if args.command == "find-asins":
            print(json.dumps(search_book_candidates(), ensure_ascii=False, indent=2))
            return 0

        asins = [asin.strip().upper() for asin in args.asins]
        invalid = [asin for asin in asins if len(asin) != 10 or not asin.isalnum()]
        if invalid:
            raise RuntimeError(f"ASINの形式を確認してください: {', '.join(invalid)}")

        print(json.dumps(fetch_items(asins), ensure_ascii=False, indent=2))
        return 0
    except RuntimeError as error:
        print(f"エラー: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
