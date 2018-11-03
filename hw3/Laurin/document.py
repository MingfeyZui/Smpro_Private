from nltk import word_tokenize

def normalized_tokens(text):
    """ This takes a string and returns lower-case tokens, using nltk for tokenization. """
    word_list = word_tokenize(text)
    word_list = [word.lower() for word in word_list]
    return word_list

def word_count(text):
    mapping = dict()

    for lex in normalized_tokens(text):
        if lex in mapping:
            mapping[lex] += 1
        else:
            mapping[lex]  = 1
    return mapping

class TextDocument:
    def __init__(self, text, id=None):
        """ This creates a from a string and an identifier. """
        self.text = text
        self.word_to_count = word_count(text)
        self.id = id

    @classmethod
    def from_file(cls, filename):
        """ This creates a TextDokument by reading a file. """
        file = open(filename,"r")
        text = file.read()
        file.close()
        return cls(text, filename)

    def __str__(self):
        """ This returns a short string representation, which is at most 25 characters long.
        If the original text is longer than 25 characters, the last 3 characters of the short string should be '...'.
        """
        if len(self.text) >= 25:
            rep = self.text[0:22] + "..."
        else:
            rep = self.text[0:26]
        return rep

    def word_overlap(self, other_doc):
        """ This returns the number of words that occur in both of the documents (self and other_doc) at the same time.
        Every word should be considered only once, irrespective of how often it occurs in either document (i.e. we
        consider word *types*).
        """
        self_tokens = word_count(self.text)
        other_doc_tokens = word_count(other_doc.text)
        overlap = self_tokens.keys() & other_doc_tokens.keys()
        return len(overlap)