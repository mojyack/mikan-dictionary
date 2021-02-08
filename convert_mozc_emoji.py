import os
import csv

ROOT_PATH = os.path.dirname(__file__)
SOURCE_PATH = os.path.join(ROOT_PATH, "mozc/src/data/emoji/emoji_data.tsv")
OUTPUT_PATH = os.path.join(ROOT_PATH, "source/system/emoji.csv")
SOURCE_PATH = "/home/mojyack/working/mecab-as-kkc/mozc/src/data/emoji/emoji_data.tsv"

def main():
    with open(SOURCE_PATH, newline = '') as source, open(OUTPUT_PATH, 'w', newline = '') as dest:
        reader = csv.reader(source, delimiter='\t')
        writer = csv.writer(dest, lineterminator='\n')
        for line in reader:
            if len(line) != 13 or len(line[1]) == 0:
                continue
            for yomi in line[6].split():
                if(len(yomi) == 0):
                    continue
                converted = [yomi, 0, 0, 10000, line[1]]
                writer.writerow(converted)

if __name__ == '__main__':
    main()
