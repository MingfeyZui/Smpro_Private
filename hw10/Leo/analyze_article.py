import nltk
import urllib
import bs4
from collections import defaultdict


def get_html(url):
    return urllib.request.urlopen(url).read().decode("utf-8")

def get_text(html):
    #TODO create the list of clean paragraphs (no HTML markup) from the given html
    #TODO return paragraphs as a string. Hint: join the list of paragraphs by newline

    soup = bs4.BeautifulSoup(html, 'html.parser')
    paragraphs = []
    for p in soup.find_all('p'):
        paragraphs.append(p.get_text())
        text = '\n'.join(paragraphs)
    return text


def get_headline(html):
    #TODO return the headline of html

    soup = bs4.BeautifulSoup(html, 'html.parser')
    return soup.h1.get_text()

def get_normalized_tokens(text):
    #TODO tokenize the text with NLTK and return list of lower case tokens without stopwords

    stopWords = set(nltk.corpus.stopwords.words('english'))
    tokens = [token for token in nltk.word_tokenize(text.lower()) if token not in stopWords]
    return tokens

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
            non_homograph.append((key))

    for word in non_homograph:
        del word_dict_h[word]

def find_homographs(tokens):
    #TODO return a dictionary which holds homographs'''


