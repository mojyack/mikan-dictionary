import os
import csv

ROOT_PATH = os.path.dirname(__file__)
NEOLOGD_PATH = os.path.join(ROOT_PATH, "source/neologd")
OUTPUT_PATH = os.path.join(ROOT_PATH, "source/additional")

# from jaconv
# https://github.com/ikegami-yukino/jaconv/tree/master/jaconv
HIRAGANA = list('ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすず'
                'せぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴ'
                'ふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろわ'
                'をんーゎゐゑゕゖゔゝゞ・「」。、')
KATAKANA = list('ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソ'
                 'ゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペ'
                 'ホボポマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶヴ'
                 'ヽヾ・「」。、')
FULL_KANA_ORD = list(map(ord, KATAKANA))
K2H_TABLE = dict(zip(FULL_KANA_ORD, HIRAGANA))
del HIRAGANA
del KATAKANA
del FULL_KANA_ORD

def kana_conv(katakana) :
    return katakana.translate(K2H_TABLE)

def convert(filename):
    csv_path = os.path.join(NEOLOGD_PATH, filename)
    save_path = os.path.join(OUTPUT_PATH, filename)
    with open(csv_path, newline = '') as source, open(save_path, 'w', newline = '') as dest:
        reader = csv.reader(source)
        writer = csv.writer(dest, lineterminator='\n')
        for line in reader:
            converted = [kana_conv(line[11]), line[1], line[2], line[3], line[0]]
            writer.writerow(converted)

def main():
    for file in os.listdir(NEOLOGD_PATH):
        if file.endswith(".csv"):
            print(file)
            convert(file);

if __name__ == '__main__':
    main()
