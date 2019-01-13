#!/usr/local/bin/python3

import re
from collections import defaultdict
import urllib.request
from bs4 import BeautifulSoup
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(u"Net income was $9.4 million compared to the prior year of $2.7 million.")
ents_and_chunks = list(doc.ents)+list(doc.noun_chunks)



def get_html(url):
    return urllib.request.urlopen(url).read().decode("utf-8")

def sortieren(li):
    res = [li[0]]
    for i in li[1:]:
        insert_index = 0
        for index in range(len(res)):
            if i >= res[index]:
                insert_index += 1
        res.insert(insert_index, i)
    return res
