import nltk
import urllib
import bs4
from collections import defaultdict


def get_html(url):
    return urllib.request.urlopen(url).read().decode("utf-8")

def get_text(html):
    #TODO create the list of clean paragraphs (no HTML markup) from the given html
    #TODO return paragraphs as a string. Hint: join the list of paragraphs by newline
    paragraphs = [paragraph.get_text() for paragraph in list(bs4.BeautifulSoup(html, "html.parser").find_all("p"))]
    
    # print("\n".join(paragraphs))
    return "\n".join(paragraphs)

def get_headline(html):
    #TODO return the headline of html
    return bs4.BeautifulSoup(html, "html.parser").find_all("h1")[0].get_text()

def get_normalized_tokens(text):
    #TODO tokenize the text with NLTK and return list of lower case tokens without stopwords
    return [word.lower() for word in nltk.word_tokenize(text) if word not in nltk.corpus.stopwords.words("english")]

def get_pos_dict(tokens):
    #TODO return a dictionary of homographs (a dictionary of words and their possible POS)
    pos_dict = defaultdict(set)

    for word, tag in nltk.pos_tag(tokens):
        pos_dict[word].add(tag)

    return pos_dict

def filter_dict_homographs(word_dict_h):
    #TODO delete an entry from dictionary, if not a homograph
    pass

def find_homographs(tokens):
    #TODO return a dictionary which holds homographs'''
    pass

