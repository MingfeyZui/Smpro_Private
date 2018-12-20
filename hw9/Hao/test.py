#!/usr/local/bin/python3
import nltk
from nltk.corpus import wordnet
import itertools

# dog_syn = wordnet.synsets("dog","n")[0]
# cat_syn = wordnet.synsets("cat", "n")[0]

# print(dog_syn.path_similarity(cat_syn))
li = ["huuo-hello","world-aii","ghiii-hio"]

for item in li:
    item = item.split("-")
print(li)