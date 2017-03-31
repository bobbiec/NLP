import sys
import nltk
import random
from nltk import word_tokenize, sent_tokenize
import math
import os
from nltk.corpus import conll2002

textfile = sys.argv[1]
questionfile = sys.argv[2]
numberofquestions = sys.argv[3]

def traverse(t):
    try:
        t.label()
    except AttributeError:
        print(t, end=" ")
    else:
        # Now we know that t.node is defined
        print('(', t.label(), end=" ")
        for child in t:
            traverse(child)
        print(')', end=" ")



with open(textfile) as myfile:
	rawText = myfile.read()
text = word_tokenize(rawText)

question = open(questionfile, "w")

tt = nltk.pos_tag(text)

print(traverse(nltk.ne_chunk(tt)[6]))



sentences = nltk.sent_tokenize(rawText)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)

    entity_names.extend(extract_entity_names(tree))

# Print all entity names
#print entity_names

# Print unique entity names
print(entity_names)


