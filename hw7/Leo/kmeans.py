import string
import numpy as np
import random
class Reader:

    def __init__(self, path):
        self.path = path
        self.punctuation = set(string.punctuation)
        self.courses = self.get_lines()
        self.vocabulary = self.get_vocabulary()
        self.vector_spaced_data = self.data_to_vectorspace()

    def get_lines(self):
        #TODO return list of courses from file
        lines = []
        with open("../data/courses.txt", "r") as file:
            for line in file:
                line = line.strip()
                lines.append(line)
        return lines

    def normalize_word(self,word):
        #TODO normalize word by lower casing and deleting punctuation from word
        #TODO use set of punctuation symbols self.punctuation
        return word.lower().strip(string.punctuation)

    def get_vocabulary(self):
        #TODO return list of unique words from file and sort them alphabetically
        vocab = set()
        for line in self.courses:
            line = line.split()
            for i in line:
                vocab.add(self.normalize_word(i))

        return sorted(vocab)

    def vectorspaced(self,course):
        #TODO represent course by one-hot vector: vector filled with 0s, except for a 1 at the position associated with word in vocabulary
        #TODO length of vector should be equal vocabulary size
        liste = []
        course_words = course.lower().split()
        for word in self.get_vocabulary():
            if word in course_words:
                liste.append(1)
            else:
                liste.append(0)

        return liste

    def data_to_vectorspace(self):
        return [self.vectorspaced(course) for course in self.courses if course]

class Kmeans:
    """performs k-means clustering"""

    def __init__(self, k):
        self.k = k
        self.means = None

    def distance(self, x,y):
        #TODO calculate Euclidean distance between two vectors x and y

        return np.linalg.norm(np.array(x)-np.array(y))

    def classify(self,input):
        #TODO calculate Euclidean distances between input and the means and return the mean index with min distance
        return 0

    def vector_mean(self,vectors):
        #TODO calculate mean of the list of vectors

        return list(np.mean(np.array(vectors), axis=0))

    def train(self, inputs):
        # choose k random points as the initial means
        self.means = random.sample(inputs, self.k)#step 1

        assignments = None
        iter = 0
        while iter != 100:
            # find new assignments
            assignments = map(self.classify, inputs)

            # compute new means based on the new assignments
            for i in range(self.k):
                # find all the points assigned to cluster i
                i_points = [p for p, a in zip(inputs,assignments) if a == i]
                if i_points:
                    ## make sure i_points is not empty so don't divide by 0
                    self.means[i] = self.vector_mean(i_points)
            iter += 1



