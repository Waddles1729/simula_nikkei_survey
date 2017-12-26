import gensim
from gensim import corpora
import MeCab
import re

def _get_noun_list(text):
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    # tagger = MeCab.Tagger('mecabrc')
    tagger.parse('')
    node = tagger.parseToNode(text)
    target_parts_of_speech = ('名詞',)
    keywords = []
    while node:
        if node.feature.split(",")[0] in target_parts_of_speech:
            keywords.append(node.surface)
        node = node.next
    return keywords

f = open('p_data.txt')
line = f.readline()
all_text = []
while line:
    new_line = line.replace('\n', '')
    p_list = re.findall('([^。]+。)', new_line)
    for p in p_list:
        all_text.append(_get_noun_list(str(p)))
    line = f.readline()
f.close()



print(all_text)
