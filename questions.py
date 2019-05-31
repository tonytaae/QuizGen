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
# {"id" : questionInfos}

# Assuming we are working with only one quiz without any possibilty to
# switch to another quiz
quiz = {}
questionId = 1

def addQuestion(description, text, qtype, answers, feedback, points) :
    global questionId
    
    quiz[str(questionId)] = {"description" : description,
        "text" : text, 
        "qtype" : qtype,
        "answers" : answers,
        "feedback" : feedback,
        "points" : points
        }
    questionId += 1

def modifyQuestion(id, description, text, qtype, answers, feedback, points) :
    quiz[id] = {"description" : description,
        "text" : text, 
        "qtype" : qtype,
        "answers" : answers,
        "feedback" : feedback,
        "points" : points
        }

def deleteQuestion(id) :
    del quiz[id]

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