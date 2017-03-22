"""
Useful functions involving keywords 
"""

from nltk.stem.snowball import SnowballStemmer
from nltk.util import ngrams
import nltk

def getStems(sentence):
    """Return a set of word stems (unigram) and tuples of stems (bigram)."""
    words = nltk.word_tokenize(sentence)
    stemmer = SnowballStemmer("english")
    unigrams = [stemmer.stem(word) for word in words] 
    bigrams = ngrams(unigrams, 2)             
    return (set(unigrams) | set(bigrams))

def mostStemMatches(textStemsList, questionStems):
    """Return a sorted list of indices corresponding to most stem matches."""
    matches = []
    for i, sentenceStems in enumerate(textStemsList):
        count = len(questionStems & sentenceStems)
        matches.append((i, count))
    return sorted(matches, key=lambda x:-x[1])