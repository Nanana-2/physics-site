#!/bin/zsh
# この Mac にしかないもの（PDF 原稿・図のソース・作業用の道具）を，非公開リポジトリ
# Nanana-2/physics-site-private に控える。何度実行してもよい（変わった分だけ記録される）。
#   zsh scripts/backup_private.sh
set -e
SRC=${0:A:h:h}
DST=$HOME/physics-site-private
if [ ! -d $DST/.git ]; then
  gh repo clone Nanana-2/physics-site-private $DST
fi
EXC=(--exclude '*.aux' --exclude '*.log' --exclude '*.fls' --exclude '*.fdb_latexmk' --exclude '*.synctex.gz' --exclude '*.toc' --exclude '*.out' --exclude '.DS_Store')
rsync -a --delete $EXC --exclude 'build/' $SRC/private/pdf-books/ $DST/pdf-books/
rsync -a --delete $EXC --exclude 'build/' --exclude 'review/' $SRC/output/pdf/figures-work/ $DST/figures-work/
mkdir -p $DST/tools
cp $SRC/.env.example $DST/tools/ 2>/dev/null || true
cd $DST
git add -A
if git diff --cached --quiet; then echo "変更なし"; else git commit -qm "backup $(date '+%Y-%m-%d %H:%M')" && git push -q && echo "控えました"; fi
