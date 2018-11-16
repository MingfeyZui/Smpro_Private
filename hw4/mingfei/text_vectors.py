from nltk import FreqDist, word_tokenize
from collections import defaultdict
import os, math

# 点积 skarlarproduct，
def dot(dictA, dictB):
    return sum([dictA.get(tok) * dictB.get(tok, 0) for tok in dictA])

# String tokenized
def normalized_tokens(text):
    return [token.lower() for token in word_tokenize(text)]

#Textdoc 结构： text， token counts dict， id
class TextDocument:
    def __init__(self, text, id=None):
        self.text = text
        self.token_counts = FreqDist(normalized_tokens(text))
        self.id = id


    #the file will be read, and in the text
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as myfile:
            text = myfile.read().strip()
        return cls(text, filename)


class DocumentCollection:
    def __init__(self, term_to_df, term_to_docids, docid_to_doc):
        # string to int # dict{string, int}
        self.term_to_df = term_to_df
        # string to set of string    dict{string, set(string)}
        self.term_to_docids = term_to_docids
        # string to TextDocument  dict{string,clsTextDocument}
        self.docid_to_doc = docid_to_doc

    # doc_list
    @classmethod
    def from_dir(cls, dir, file_suffix):
        files = [(dir + "/" + f) for f in os.listdir(dir) if f.endswith(file_suffix)]
        docs = [TextDocument.from_file(f) for f in files]
        return cls.from_document_list(docs)

    # from the doc_list got
    @classmethod
    def from_document_list(cls, docs):
        term_to_df = defaultdict(int)
        term_to_docids = defaultdict(set)
        docid_to_doc = dict()
        for doc in docs:
            docid_to_doc[doc.id] = doc
            for token in doc.token_counts.keys():
                term_to_df[token] += 1
                term_to_docids[token].add(doc.id)
        return cls(term_to_df, term_to_docids, docid_to_doc)



   #
    def docs_with_all_tokens(self, tokens):
        docids_for_each_token = [self.term_to_docids[token] for token in tokens]
        docids = set.intersection(*docids_for_each_token)  # unpack all the ele in the list as seperate arguments
        return [self.docid_to_doc[id] for id in docids]



    #term frequency , inverse docs frequency
    def tfidf(self, counts):
        N = len(self.docid_to_doc)
        return {tok: tf * math.log(N / self.term_to_df[tok]) for tok, tf in counts.items() if tok in self.term_to_df}




    # docs 的相似度
    def cosine_similarity(self, docA, docB):
        weightedA = self.tfidf(docA.token_counts)
        weightedB = self.tfidf(docB.token_counts)
        dotAB = dot(weightedA, weightedB)
        normA = math.sqrt(dot(weightedA, weightedA))
        normB = math.sqrt(dot(weightedB, weightedB))
        return dotAB / (normA * normB)



# 
class SearchEngine:
    def __init__(self, doc_collection):
        self.doc_collection = doc_collection

    def ranked_documents(self, query):
        query_doc = TextDocument(query)          #query als constructor von TextDocument
        query_tokens = query_doc.token_counts.keys()       #Zeile 17    FreDist
        docs = self.doc_collection.docs_with_all_tokens(query_tokens)
        docs_sims = [(doc, self.doc_collection.cosine_similarity(query_doc, doc)) for doc in docs]
        return sorted(docs_sims, key=lambda x: -x[1])    # tulpe set ranking

    def snippets(self, query, document, window=50):
        tokens = normalized_tokens(query)
        text = document.text
        for token in tokens:
            start = text.lower().find(token.lower())  #Position of sth ausgeben von find(sth)
            if -1 == start:    # -1 Position nicht gefunden
                continue        #back to the beginning of the loop
            end = start + len(token)
            left = "..." + text[start - window:start]
            middle = "[" + text[start: end] + "]"
            right = text[end:end + window] + "..."
            yield left + middle + right
