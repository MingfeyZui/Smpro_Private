from nltk import word_tokenize, FreqDist


def normalized_tokens(text):
    """ This takes a string and returns lower-case tokens, using nltk for tokenization. """
    return [token.lower() for token in word_tokenize(text)]     # TODO: return list with lower-case tokens.

class TextDocument:
    def __init__(self, text, id=None):
        """ This creates a from a string and an identifier. """
        self.text = text
        self.word_to_count = FreqDist(normalized_tokens(text))     # TODO: Create dictionary from words to counts.
        self.id = id

    @classmethod
    def from_file(cls, filename):
        """ This creates a TextDokument by reading a file. """
        with open(filename, 'r') as file:
            text = file.read()              # TODO: read text from filename
            return cls(text, filename)

    def __str__(self):
        """ This returns a short string representation, which is at most 25 characters long.
        If the original text is longer than 25 characters, the last 3 characters of the short string should be '...'.
        """
        if len(self.text) > 25:         # TODO: Implement correct return statement.
            return self.text[:22] + "..."
        else:
            return self.text



    def word_overlap(self, other_doc):
        """ This returns the number of words that occur in both of the documents (self and other_doc) at the same time.
        Every word should be considered only once, irrespective of how often it occurs in either document (i.e. we
        consider word *types*).
        """
         # TODO: Implement correct return statement.
        overlap = 0
        for word in self.word_to_count:
            if word  in other_doc.word_to_count:
                overlap +=1
        return overlap




