from nltk import FreqDist
from nltk import word_tokenize
from collections import Counter

class Analyzer(object):
    def __init__(self, path):
        '''reads the file text, creates the list of words (use nltk.word_tokenize to tokenize the text),
            and calculates frequency distribution '''
        with open(path,'r') as file:
            self.text = word_tokenize(file.read())
        #self.text = word_tokenize(open(path,'r').read()) #TODO the list of words from text file
        self.token_counts = FreqDist(self.text) #TODO frequency distribution of words from text file

    def numberOfTokens(self):
        '''returns number of tokens in the text '''
        return len(self.text)
    
    def vocabularySize(self):
        '''returns a list of the vocabulary of the text '''
        return len(self.token_counts)
    
    def lexicalDiversity(self):
        '''returns a list of lexical diversity of the text '''
        # Höhe Diversity: mehr unterschiedliche Wörter
        return self.numberOfTokens()/self.vocabularySize()

    def getKeywords(self):
        '''return words as possible key words, that are longer than seven characters, that occur more than seven times (sorted alphabetically)'''
        keys =[]
        for key,value in self.token_counts.items():
            if len(key) > 7 and value >7:
                keys.append(key)
        return sorted(keys)

        #Musterlösung     : iterier Typs , and iterier das Filter
        #return sorted([w for w in self.token_counts.keys() if len(w)>7 and self.token_counts[w]>7])

    
    def numberOfHapaxes(self):
        '''returns the number of hapaxes in the text'''
        return len(self.token_counts.hapaxes())
    
    def avWordLength(self):
        #此处题目表述为 所有不同词汇的平均值，而不是所有词汇的平均值'''returns the average word length of the text'''
        #Musterlösung
        #return sum([len(word) for word in self.token_counts])/len(self.token_counts)

        sumWordLen = 0
        for word in self.token_counts:
            sumWordLen = sumWordLen +len(word)
        return sumWordLen/len(self.token_counts)

    def topSuffixes(self):
        '''returns the 10 most frequent 2-letter suffixes in words
            (restrict to words of length 5 or more)'''

        #Musterlösung
        #list_of_words = [word for word in self.token_counts if len(word) >=5]
        #suf_dict = FreqDist(suf[-2:] for suf in list_of_words)
        #suf_most_freq =[elem[0] for elem in suf_dict.most_common(10)]
        #return suf_most_freq


        suffixes= []
        for langWord in self.token_counts.keys():
            if len(langWord) >= 5:
                suffixes.append(langWord[-2:])
        return [word for word,count in Counter(suffixes).most_common(10)]



    
    def topPrefixes(self):
        '''returns the 10 most frequent 2-letter prefixes in words
            (restrict to words of length 5 or more)'''
        suffixes= []
        for langWord in self.token_counts.keys():
            if len(langWord) >= 5:
                suffixes.append(langWord[:2])
        return [word for word,count in Counter(suffixes).most_common(10)]


    def tokensTypical(self):
        """TODO returns first 5 tokens of the (alphabetically sorted) vocabulary 
        that contain both often sccleen prefixes and suffixes in the text. As in topPrefixes()
        and topSuffixes(), Prefixes and Suffixes are 2 characters long."""

        sufixes  = self.topSuffixes()
        prefixes = self.topPrefixes()
        return sorted([word for word in self.token_counts.keys() if word[:2] in prefixes and word[-2:] in sufixes])[:5]

                
        
            
        
        
        
        
        
        

