import nltk

def normalized_tokens(text):
    """ This takes a string and returns lower-case tokens, using nltk for tokenization. """

    return [word.lower() for word in nltk.word_tokenize(text)]

class TextDocument:
    def __init__(self, text, id=None):
        """ This creates a from a string and an identifier. """
        self.text = text
        self.word_to_count = {}
        for word in nltk.word_tokenize(text):
            if word in word_to_count:
                word_to_count[word] += 1
            else:
                word_to_count[word] = 1
        self.id = id

    @classmethod
    def from_file(cls, filename):
        """ This creates a TextDokument by reading a file. """
        text = filename.read()
        return cls(text, filename)

    def __str__(self):
        """ This returns a short string representation, which is at most 25 characters long.
        If the original text is longer than 25 characters, the last 3 characters of the short string should be '...'.
        """
        if len(self.text) <= 25:
            return self.text
        else:
            res = self.text[:22] + '...'
            return res

    def word_overlap(self, other_doc):
        """ This returns the number of words that occur in both of the documents (self and other_doc) at the same time.
        Every word should be considered only once, irrespective of how often it occurs in either document (i.e. we
        consider word *types*).
        """
        list1 = {word for word in nltk.word_tokenize(self.text)}
        list2 = {word for word in nltk.word_tokenize(other_doc.text)}
        return len(list1.intersection(list2))
