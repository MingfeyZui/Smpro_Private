from nltk import FreqDist, word_tokenize
from collections import defaultdict
import os, math


def dot(dictA, dictB):
    '''
    >>> dot({"001":3, "002":8, "003":2, "004":14}, {"001":8, "002":2, "003":12})
    64
    >>> dot({"first": 0.5, "second": 2.5, "third": 0.05}, {"first": 3, "second": 5})
    14.0
    '''
    return sum([dictA.get(tok) * dictB.get(tok, 0) for tok in dictA])


def normalized_tokens(text):
    '''
    >>> normalized_tokens("Hallo hier ist Leo")
    ['hallo', 'hier', 'ist', 'leo']
    >>> normalized_tokens("In Japan stellen Manga einen bedeutenden Teil der Literatur sowie der Medienlandschaft dar.")
    ['in', 'japan', 'stellen', 'manga', 'einen', 'bedeutenden', 'teil', 'der', 'literatur', 'sowie', 'der', 'medienlandschaft', 'dar', '.']
    '''
    return [token.lower() for token in word_tokenize(text)]


class TextDocument:
    def __init__(self, text, id=None):
        '''
        Erschafft ein Objekt der Klasse TextDocument mit den Attributen
        text und id, wobei id den default-wert None hat
        '''
        self.text = text
        self.token_counts = FreqDist(normalized_tokens(text))
        self.id = id

    @classmethod
    def from_file(cls, filename):
        '''
        Erschafft ein Objekt der Klasse TextDocument aus einer Datei
        '''
        with open(filename, 'r') as myfile:
            text = myfile.read().strip()
        return cls(text, filename)


class DocumentCollection:
        '''
        Erschafft ein Objekt der Klasse DocumentCollection mit den 3 Attributen
        term_to_df, term_to_docids, docid_to_doc
        '''
    def __init__(self, term_to_df, term_to_docids, docid_to_doc):
        # string to int
        self.term_to_df = term_to_df
        # string to set of string
        self.term_to_docids = term_to_docids
        # string to TextDocument
        self.docid_to_doc = docid_to_doc

    @classmethod
    def from_dir(cls, dir, file_suffix):
        '''
        Übergibt der Methode cls.from_document_list eine Liste aller Dateien
        mit der gleichen Endung im angegeben Verzeichnis
        '''
        files = [(dir + "/" + f) for f in os.listdir(dir) if f.endswith(file_suffix)]
        docs = [TextDocument.from_file(f) for f in files]
        return cls.from_document_list(docs)

    @classmethod
    def from_document_list(cls, docs):
        '''
        Erschafft Objekte der Klasse DocumentCollection
        '''
        term_to_df = defaultdict(int)
        term_to_docids = defaultdict(set)
        docid_to_doc = dict()
        for doc in docs:
            docid_to_doc[doc.id] = doc
            for token in doc.token_counts.keys():
                term_to_df[token] += 1
                term_to_docids[token].add(doc.id)
        return cls(term_to_df, term_to_docids, docid_to_doc)

    def docs_with_all_tokens(self, tokens):
        docids_for_each_token = [self.term_to_docids[token] for token in tokens]
        docids = set.intersection(*docids_for_each_token)  # union?
        return [self.docid_to_doc[id] for id in docids]

    def tfidf(self, counts):
        N = len(self.docid_to_doc)
        return {tok: tf * math.log(N / self.term_to_df[tok]) for tok, tf in counts.items() if tok in self.term_to_df}

    def cosine_similarity(self, docA, docB):
        weightedA = self.tfidf(docA.token_counts)
        weightedB = self.tfidf(docB.token_counts)
        dotAB = dot(weightedA, weightedB)
        normA = math.sqrt(dot(weightedA, weightedA))
        normB = math.sqrt(dot(weightedB, weightedB))
        return dotAB / (normA * normB)


class SearchEngine:
    def __init__(self, doc_collection):
        self.doc_collection = doc_collection

    def ranked_documents(self, query):
        query_doc = TextDocument(query)
        query_tokens = query_doc.token_counts.keys()
        docs = self.doc_collection.docs_with_all_tokens(query_tokens)
        docs_sims = [(doc, self.doc_collection.cosine_similarity(query_doc, doc)) for doc in docs]
        return sorted(docs_sims, key=lambda x: -x[1])

    def snippets(self, query, document, window=50):
        tokens = normalized_tokens(query)
        text = document.text
        for token in tokens:
            start = text.lower().find(token.lower())
            if -1 == start:
                continue
            end = start + len(token)
            left = "..." + text[start - window:start]
            middle = "[" + text[start: end] + "]"
            right = text[end:end + window] + "..."
            yield left + middle + right
