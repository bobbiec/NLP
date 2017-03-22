#!/usr/bin/python

import sys

def generateQuestions(text, nquestions):
    pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 ask.py article.txt nquestions")
        sys.exit()

    articleFile = sys.argv[1]
    nquestions = int(sys.argv[2])
    
    with open(articleFile) as f:
        text = f.read()

    questions = generateQuestions(text, nquestions)

    with open("questions.txt", "w") as f:
        f.write("\n".join(questions))