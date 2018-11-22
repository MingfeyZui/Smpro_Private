from nltk import FreqDist, word_tokenize
from collections import defaultdict
import os, math

class DokumentenSammlung:
    def __init__(self, doc_from_id, t_to_docIds, t_to_df, token_counts, text = ""):
        #id : doc ie int : obj
        #maps an id to its document
        self.doc_from_id = doc_from_id
        #token : id ie str : int
        #maps a token to the documents containing it
        self.t_to_docIds = t_to_docIds
        #str
        self.text = text
        #token : document freq ie str : int
        #maps a token to the number of documents containing it
        self.t_to_df = t_to_df
        self.token_counts = token_counts
    def docs_with_all_tokens(self, tokens):
        '''
        returns list with all documents which contain all said tokens.
        assumes self.t_to_docIds to be filled 
        '''
        tokens_to_ids = [self.t_to_docIds[token] for token in tokens]
        id_list = set.intersection(*tokens_to_ids)
        return [self.doc_from_id[identity] for identity in id_list]
    def docs_with_any_tokens(self, tokens):
        '''
        returns list with all documents which contain at least some said tokens.
        assumes self.t_to_docIds to be filled
        '''
        tokens_to_ids = [self.t_to_docIds[token] for token in tokens]
        id_list = set.union(*tokens_to_ids)
        return [self.doc_from_id[identity] for identity in id_list]
    def tfidf(self, freq_dict):
        n = len(self.doc_from_id)
        #if a term from the freq_dict has a number of documents associated with it, 
        #this function returns a mapping of these terms to their frequencies times 
        #the log of all documents devided by the number of documents associated with it.
        t_to_tfidf = {term : tf * math.log( n / self.t_to_df[term] ) \
               for term,tf in freq_dict.items() if term in self.t_to_df}
        return t_to_tfidf
    def cos_sim(self, doc1, doc2):
        doc1_vector = self.tfidf(doc1.token_counts)
        doc2_vector = self.tfidf(doc2.token_counts)
        dot_prod = sum(doc1_vector[key] * doc2_vector.get(key, 0) for key in doc1_vector)
        vec_length_doc1 = math.sqrt(sum(doc1_vector[key]**2 for key in doc1_vector))
        vec_length_doc2 = math.sqrt(sum(doc2_vector[key]**2 for key in doc2_vector))
        if vec_length_doc1 == 0 or vec_length_doc2 == 0:
            return 0
        else:
            return dot_prod / (vec_length_doc1 * vec_length_doc2)