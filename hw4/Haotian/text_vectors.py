from nltk import FreqDist, word_tokenize
from collections import defaultdict
import os, math
import re


def dot(dictA, dictB):
    """ returns dot product of dictA and dictB: multiplies values of their common attributes(frequency of token), if token does not exist in dictB, a default of 0 is used

    >>> dot({1:1, 2:2, 3:3}, {2:2, 3:3, 4:4})
    13
    >>> dot({1:2, 2:3}, {1:3, 2:4})
    18

    """
    return sum([dictA.get(tok) * dictB.get(tok, 0) for tok in dictA])


def normalized_tokens(text):
    """ returns a list with lower case tokenized text
    >>> normalized_tokens("Hello World.")
    ['hello', 'world', '.']
    >>> normalized_tokens("This is a Test Sentence")
    ['this', 'is', 'a', 'test', 'sentence']
    """
    return [token.lower() for token in word_tokenize(text)]


class TextDocument:
    def __init__(self, text, id=None):
        """ creates a TextDocument object with variables text, doc id and a frequency list
        """
        self.text = text
        self.token_counts = FreqDist(normalized_tokens(text))
        self.id = id

    @classmethod
    def from_file(cls, filename):
        """ returns a TextDocument object with text read from the file(filename) and filename as the doc id
        """
        with open(filename, 'r') as myfile:
            # text = myfile.read().strip()
            text = myfile.read()           # <- changed for unittesting
            while not text[0].isalpha():
                text = text[1:]
            while not text[-1].isalpha():
                text = text[:-1]
        return cls(text, filename)


class DocumentCollection:
    """ creates DocumentCollection object, passes in term_to_df, term_to_docids, docid_to_doc
    """
    def __init__(self, term_to_df, term_to_docids, docid_to_doc):
        # string to int
        self.term_to_df = term_to_df
        # string to set of string
        self.term_to_docids = term_to_docids
        # string to TextDocument
        self.docid_to_doc = docid_to_doc

    @classmethod
    def from_dir(cls, dir, file_suffix):
        """ creates DocumentCollection objects from files with suffix file_suffix in dir
        """
        files = [(os.path.abspath(dir) + "/" + f) for f in os.listdir(dir) if f.endswith(file_suffix)]  # <- changed for unittesting
        # files = [(dir + "/" + f) for f in os.listdir(dir) if f.endswith(file_suffix)]
        docs = [TextDocument.from_file(f) for f in files]
        return cls.from_document_list(docs)

    @classmethod
    def from_document_list(cls, docs):
        """ creates DocumentCollection objects from a list of documents(docs)
        """
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
        """ returns a list of docids corresponding to documents with all the tokens present
        """
        # if not re.match(re.compile("'.*'"), tokens[0]):
        #     docids_for_each_token = [self.term_to_docids[token] for token in tokens]
        # else:
        #     docids_for_each_token = [self.term_to_docids[tokens[0]]]
        docids_for_each_token = [self.term_to_docids[token] for token in tokens]
        docids = set.intersection(*docids_for_each_token)  # union?
        return [self.docid_to_doc[id] for id in docids]

    def tfidf(self, counts):
        """ returns a dictionary mapping all tokens to their tf-idfs
        """
        N = len(self.docid_to_doc)
        return {tok: tf * math.log(N / self.term_to_df[tok]) for tok, tf in counts.items() if tok in self.term_to_df}

    def cosine_similarity(self, docA, docB):
        """ returns cosine similarity between docA and docB
        """
        weightedA = self.tfidf(docA.token_counts)
        weightedB = self.tfidf(docB.token_counts)
        dotAB = dot(weightedA, weightedB)
        normA = math.sqrt(dot(weightedA, weightedA))
        normB = math.sqrt(dot(weightedB, weightedB))
        return dotAB / (normA * normB) if (normA * normB) != 0 else 0


class SearchEngine:
    def __init__(self, doc_collection):
        """ creates SearchEngine object with a class object of DocumentCollection
        """
        self.doc_collection = doc_collection

    def ranked_documents(self, query):
        """ creates a TextDocument object query with text = query, docs includes all documents with all tokens in query, docs_sims returns a list of cosine similarities, which in the end will be sorted and returned
        """
        query_doc = TextDocument(query)
        query_tokens = query_doc.token_counts.keys()
        docs = self.doc_collection.docs_with_all_tokens(query_tokens)
        docs_sims = [(doc, self.doc_collection.cosine_similarity(query_doc, doc)) for doc in docs]
        return sorted(docs_sims, key=lambda x: -x[1])

    def snippets(self, query, document, window=50):
        """ search for each token in query, return all contexts
        """
        tokens = normalized_tokens(query)
        text = document.text
        for token in tokens:
            # if -1 == start or -1 == text.find(exact_token.lower()):
            spaced_token = " " + token + " "
            start = text.lower().find(token.lower())
            full_token = text.lower()[start-1:start+len(token)+1]
            if start == -1:
                continue
            elif not re.match(r"\s\w+\s", full_token):
                continue
            # elif start == -1 and re.match("\b\w+\b", full_token):
            #     end = start + len(token)
            #     left = "..." + text[start - window:start]
            #     middle = "[" + text[start: end] + "]"
            #     right = text[end:end + window] + "..."
            #     yield left + middle + right

            end = start + len(token)
            left = "..." + text[start - window:start]
            middle = "[" + text[start: end] + "]"
            right = text[end:end + window] + "..."
            yield left + middle + right
