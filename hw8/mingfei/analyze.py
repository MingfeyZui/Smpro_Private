from nltk import FreqDist
from nltk import word_tokenize

class Analyzer(object):
    def __init__(self, path):
        '''reads the file text, creates the list of words (use nltk.word_tokenize to tokenize the text),
            and calculates frequency distribution '''
        with open(path) as file:
            self.text = word_tokenize(file.read())
        #self.text =  word_tokenize(open(path).read())#TODO the list of words from text file
        self.token_counts = FreqDist(self.text) #TODO frequency distribution of words from text file
    
    def numberOfTokens(self):
        '''returns number of tokens in the text '''
        return len(self.text)
    
    def vocabularySize(self):
        '''returns a list of the vocabulary of the text '''
        return len(self.token_counts)
    
    def lexicalDiversity(self):
        '''returns a list of the vocabulary of the text '''
        return len(self.text) / len(self.token_counts)
    
    def getKeywords(self):
        '''return words as possible key words, that are longer than seven characters, that occur more than seven times (sorted alphabetically)'''
        return sorted([word for word in self.token_counts.keys() if (len(word) > 7 and self.token_counts[word] > 7)])
    
    def numberOfHapaxes(self):
        '''returns the number of hapaxes in the text'''
        return len([word for word in self.token_counts.keys() if self.token_counts[word] == 1])
    
    def avWordLength(self):
        '''returns the average word length of the text'''
        return sum(len(word) for word in self.token_counts) / len(self.token_counts)

    def topSuffixes(self):
        '''returns the 10 most frequent 2-letter suffixes in words
            (restrict to words of length 5 or more)'''
        liste = []
        for word in self.token_counts.keys():
            if len(word) >= 5:
                liste.append(word[-2:])
        sliste = sorted(FreqDist(liste).items(), key=lambda x: x[1], reverse=True)

        return [suffix[0] for suffix in sliste][:10]
    
    def topPrefixes(self):
        '''returns the 10 most frequent 2-letter prefixes in words
            (restrict to words of length 5 or more)'''
        liste = []
        for word in self.token_counts.keys():
            if len(word) >= 5:
                liste.append(word[:2])
        sliste = sorted(FreqDist(liste).items(), key=lambda x: x[1], reverse=True)

        return [suffix[0] for suffix in sliste][:10]
    
    def tokensTypical(self):
        """TODO returns first 5 tokens of the (alphabetically sorted) vocabulary 
        that contain both often seen prefixes and suffixes in the text. As in topPrefixes()
        and topSuffixes(), Prefixes and Suffixes are 2 characters long."""
        return sorted([word for word in self.token_counts.keys() if word[-2:] in self.topSuffixes() and word[:2] in self.topPrefixes()])[:5]
                
        
            
        
        
        
        
        
        

