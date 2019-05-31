#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# answer type (dict) :
# {"text" : string,
#  "fraction" : integer in [0 ; 100]
# }

# questionInfos type (dict) :
# {"description" : string,
#  "text" : string,
#  "qtype" : string in ["qcm", "shortanswer"], # must think to all questions types we'll manage
#  "answers" : array of "answer",
#  "feedback" : string,
#  "points" : float
# }

# quiz type (dict) : 
# {"name" : questionInfos}

# Assuming we are working with only one quiz without any possibilty to
# switch to another quiz
quiz = {}

def addQuestion(name, description, text, qtype, answers, feedback, points) :
    quiz[name] = {"description" : description,
        "text" : text, 
        "qtype" : qtype,
        "answers" : answers,
        "feedback" : feedback,
        "points" : points
        }

def modifyQuestion(name, description, text, qtype, answers, feedback, points) :
    addQuestion(name, description, text, qtype, answers, feedback, points)

def deleteQuestion(name) :
    del quiz[name]

# for testing only
def printQuiz():
    for key, value in quiz.items() :
        questionTitle = "Question " + key
        print(questionTitle)
        print("=" * len(questionTitle), "\n")
        print(value["description"])
        print(value["text"])
        print(value["qtype"])
        print(value["answers"])
        print(value["feedback"])
        print(value["points"])
        print("\n\n")