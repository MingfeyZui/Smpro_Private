import nltk
from itertools import combinations
from nltk.corpus import wordnet as wn
from collections import Counter

def leave_odd_man_out(words):
    #TODO find the odd man in the list of words: use get_similarity_scores() method
    pass

def get_similarity_scores(pairs):  # path_similarity

    results = []

    for pair in pairs:

        max_score = 0.0
        max_line = () #should look like "('food-fruit', 0.1)"

        #TODO 1. iterate over all combinations of synsets formed by the synsets of the words in the word pair
        #TODO 2. determine the maximum similarity score
        #TODO 3. save max_line in results in form ("pair1-pair2", similarity_value) e.g.('car-automobile', 1.0)
        syn1 = wn.synsets(pair[0], pos='n')
        syn2 = wn.synsets(pair[1], pos='n')

        for synset in syn1:
            for other in syn2:
                wert = synset.path_similarity(other)
                if wert > max_score:
                    max_score = wert
                    max_line = (pair[0] + '-' + pair[1], wert)
        results.append(max_line)

    return results
    #TODO 4. return results in order of decreasing similarity

