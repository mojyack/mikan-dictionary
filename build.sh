#/usr/bin/bash

# update mozc repository.
if [ ! -d mozc ]; then
    git clone --filter=blob:none --no-checkout https://github.com/google/mozc
    cd mozc
    git config pull.rebase false
    git sparse-checkout init --cone
    git sparse-checkout set src/data/dictionary_oss
    git checkout
else
    cd mozc
    git pull
fi
cd ..

# update neologd
if [ ! -d mecab-ipadic-neologd ]; then
    git clone --filter=blob:none --no-checkout https://github.com/neologd/mecab-ipadic-neologd
    cd mecab-ipadic-neologd
    git config pull.rebase false
    git sparse-checkout init --cone
    git sparse-checkout set seed 
    git checkout
else
    cd mecab-ipadic-neologd
    git pull
fi
cd ..

if [ ! -d "source/neologd" ]; then
    mkdir "source/neologd/"
fi
for file in mecab-ipadic-neologd/seed/*.xz; do
    xz -dc "$file" > "source/neologd/$(basename -s .xz $file)"
done

# convert mozc
python ./generate_matrix_def.py
cat mozc/src/data/dictionary_oss/dictionary*.txt | tr "\\t" "," | grep -v "^," > source/system/lex.csv
python ./convert_mozc_emoji.py

# convert nlogd
python ./convert_neologd.py

# build
MECAB_DIC_COMPILER=$(mecab-config --libexecdir)/mecab-dict-index
$MECAB_DIC_COMPILER -f utf-8 -t utf-8 -d source/system/ -o dic/system/
$MECAB_DIC_COMPILER -f utf-8 -t utf-8 -d source/additional -o dic/additional/
