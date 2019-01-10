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

print(text)

stopWords = set(nltk.corpus.stopwords.words('english'))

tokens = [token for token in nltk.word_tokenize(text.lower()) if token not in stopWords]
#print(tokens)


tags = nltk.pos_tag(tokens)
#print(tags)

dic = defaultdict(set)
for k, v in tags:
    dic[k].add(v)

print(dic)

not_homograph = []
for key, value in dic.items():
    if len(value) == 1:
        not_homograph.append(key)
for word in not_homograph:
    del dic[word]
print(len(dic))