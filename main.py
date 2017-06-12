from gensim.parsing import PorterStemmer
from wikipedia import page

title = "Machine learning"
wikipedia = page(title)

# print wikipedia.content

global_stemmer = PorterStemmer()

class StemmingHelper(object):
    word_lookup = {}

    @classmethod
    def stem(cls, word):
        stemmed = global_stemmer.stem(word)

        if stemmed not in cls.word_lookup:
            cls.word_lookup[stemmed] = {}
        cls.word_lookup[stemmed][word] = (
            cls.word_lookup[stemmed].get(word, 0) + 1)
        return stemmed

    @classmethod
    def original_form(cls, word):
        if word in cls.word_lookup:
            return max(cls.word_lookup[word].keys(),
                       key=lambda x: cls.word_lookup[word][x])
        else:
            return word

# print StemmingHelper.stem('learning')
# print StemmingHelper.original_form('learn')

StemmingHelper.stem('learning')
StemmingHelper.original_form('learn')

with open("Output.txt", "w") as text_file:
    text_file.write(wikipedia.content.encode('utf-8'))


from gensim.models import word2vec, Word2Vec
import logging


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.Text8Corpus('Output.txt')
model = Word2Vec(sentences, min_count=2, size=50, window=4)

# print 'learn' in model
print model['learn']