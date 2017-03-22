#!/usr/bin/python

"""
Some functions require the Punkt Tokenizer Models:
>>> import nltk
>>> nltk.download('punkt')
"""

import sys
import nltk.data
from keywords import getStems, mostStemMatches

def answerQuestion(text, question):
    pass

if __name__ == "__main__":
    # Uncomment for final program

    # if len(sys.argv) != 3:
    #     print("Usage: python3 answer.py article.txt questions.txt")
    #     sys.exit()

    # articleFile = sys.argv[1]
    # questionsFile = sys.argv[2]
    
    articleFile = "data/set1/a1.txt"
    questionsFile = "questions/set1/a1.txt"

    # Open files and do some pre-processing
    with open(articleFile, encoding="utf8") as a, open(questionsFile, encoding="utf8") as q:
        text = a.read()
        questions = q.read()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(text)
    stems = [getStems(sentence) for sentence in sentences]

    answers = []
    for question in questions.splitlines():
        print(question)
        questionStems = getStems(question)
        most = mostStemMatches(stems, questionStems)[0][0]

        print("\t" + sentences[most])
        print()

        answer = answerQuestion(text, question)
        answers.append(answer)

    # with open("answers.txt", "w") as f:
    #     f.write("\n".join(answers))