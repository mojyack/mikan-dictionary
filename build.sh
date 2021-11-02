#!/bin/bash

# update mozc repository.
if [ ! -d mozc ]; then
    git clone --filter=blob:none --no-checkout https://github.com/google/mozc
    cd mozc
    git config pull.rebase false
    git sparse-checkout init --cone
    git sparse-checkout set src/data/dictionary_oss
    git sparse-checkout add src/data/emoji/emoji_data.tsv
    git checkout
else
    cd mozc
    git pull
fi
cd ..

# convert mozc
python ./generate_matrix_def.py
cat mozc/src/data/dictionary_oss/dictionary*.txt | tr "\\t" "," | grep -v "^," > source/system/lex.csv
python ./convert_mozc_emoji.py

# build
MECAB_DIC_COMPILER=$(mecab-config --libexecdir)/mecab-dict-index
$MECAB_DIC_COMPILER -f utf-8 -t utf-8 -d source/system/ -o dic/system/
