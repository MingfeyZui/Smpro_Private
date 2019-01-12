#!/usr/local/bin/python3

import nltk
import urllib.request
from bs4 import BeautifulSoup
from collections import defaultdict

url = urllib.request.urlopen("http://www.nytimes.com/2013/04/07/automobiles/autoreviews/hybrid-drivers-wanted.html?_r=0")
html = url.read().decode("utf-8")

soup = BeautifulSoup(html, 'html.parser')
paragraphs = []
for p in soup.find_all('p'):
    #print(p.get_text())
    paragraphs.append(p.get_text())
    text = '\n'.join(paragraphs)

#print(text)

stopWords = set(nltk.corpus.stopwords.words('english'))

tokens = [token for token in nltk.word_tokenize(text.lower()) if token not in stopWords]
#print(tokens)


tags = nltk.pos_tag(tokens)
#print(tags)

dic = defaultdict(set)
for k, v in tags:
    dic[k].add(v)

print(dic)

def get_pos_dict(tokens):
    #TODO return a dictionary of homographs (a dictionary of words and their possible POS)
    tags = nltk.pos_tag(tokens)
    pos_dict = defaultdict(set)
    for word, tag in tags:
        pos_dict[word].add(tag)

    return pos_dict

def filter_dict_homographs(word_dict_h):
    #TODO delete an entry from dictionary, if not a homograph
    non_homograph = []
    for key, value in word_dict_h.items():
        if len(value) == 1:
            non_homograph.append(key)

    for word in non_homograph:
        del word_dict_h[word]


filter_dict_homographs(dic)
print(dic)
