#!/usr/local/bin/python3

import nltk
import spacy

model = spacy.load('en_core_web_sm')
path = "../data/hydrogenics_report.txt"


class RelationExtractor(object):

    def __init__(self, path, nlp):
        self.nlp = nlp
        with open(path, 'r') as file:
            text = file.read()
        #TODO read text as a string and tokenize it by sentences

        self.sentences = nltk.sent_tokenize(text) #TODO replace -> create the list of sentences from the file


    def entities_and_nounChunks(self,doc):
        #TODO extract all entities and noun phrases and save them into one list'''

        ent_liste = []
        for ent in doc.ents:
            ent_liste.append(ent)

        return ent_liste

extractor = RelationExtractor(path, model)
doc = extractor.nlp("Net income was $6.4 million")
entitiesAndChunks = extractor.entities_and_nounChunks(doc)
extractor.entities_and_nounChunks(doc)
print(doc.ents)
print(entitiesAndChunks)

#print(len(extractor.sentences), 12)

entitiesAndChunks = [el.text for el in entitiesAndChunks]

print('Net income' in entitiesAndChunks)
print('$6.4 million' in entitiesAndChunks)