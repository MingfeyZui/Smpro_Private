import os
from unittest import TestCase

#Unittest zuerst , dann funktions,
from hw4.mingfei.text_vectors import TextDocument, DocumentCollection   #datei und funktionen importieren und testen


class DocumentCollectionTest(TestCase):

    # setUp (aufbauen)ist optional,  tearDown Methode (abbauen)
    def setUp(self):
        test_doc_list = [TextDocument(text_and_id[0], text_and_id[1]) for text_and_id in
                         [("the cat sat on a mat", "doc1"),
                          ("a rose is a rose", "doc2")]]
        self.small_collection = DocumentCollection.from_document_list(test_doc_list)

        # TODO: uncomment in case tests need access to whole document collection.
        this_dir = os.path.dirname(os.path.abspath(__file__))
        document_dir = os.path.join(this_dir, os.pardir, 'hw4/mingfei/enron/enron1/ham/')
        self.large_collection = DocumentCollection.from_dir(document_dir, ".txt")

# 注意self不要忽略, self 作为object 必须出现
    def test_unknown_word_cosine(self):
        """ Return 0 if cosine similarity is called for documents with only out-of-vocabulary words. """
        # Document that only contains words that never occurred in the document collection.
        query_doc = TextDocument(text="unknownwords", id=None)
        # Some document from collection.
        collection_doc = self.small_collection.docid_to_doc["doc1"]
        # Similarity should be zero (instead of undefined).
        self.assertEqual(self.small_collection.cosine_similarity(query_doc, collection_doc), 0.)       #überprüft die funktionen durch 2 argumente


class TextDocumentTest(TestCase):
    # TODO: Unittests for TextDocument go here.
    def test_from_file(self,test_doc_list):
        pass




class SearchEngineTest(TestCase):
    # TODO: Unittests for SearchEngine go here.
    def test_ranked_document(self):
        pass
    def test_snippets(self):
        pass

