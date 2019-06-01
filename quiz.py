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

import json

quiz = {}
quizFileName = 'quiz.json'
questionId = 1

def addQuestion(description, text, qtype, answers, feedback, points) :
    global questionId
    
    quiz[questionId] = {'description' : description,
        'text' : text, 
        'qtype' : qtype,
        'answers' : answers,
        'feedback' : feedback,
        'points' : points
        }
    questionId += 1

def modifyQuestion(id, description, text, qtype, answers, feedback, points) :
    quiz[id] = {'description' : description,
        'text' : text, 
        'qtype' : qtype,
        'answers' : answers,
        'feedback' : feedback,
        'points' : points
        }

def deleteQuestion(id) :
    del quiz[id]
    
def loadQuizFromFile() :
    try :
        with open(quizFileName) as quizFile :
            tempQuiz = json.load(quizFile)
            quizFile.close()
            
            for qId in tempQuiz.keys() :
                quiz[int(qId)] = tempQuiz[qId]
    except :
        print('Quiz inexistant. Nouveau quiz en cours de création')
        pass

def saveQuizToFile() :
    try :
        with open(quizFileName, 'w') as quizFile :
            json.dump(quiz, quizFile)
            quizFile.close()
    except :
        print('Erreur dans la sauvegarde des modifications')

# for testing only
def printQuiz():
    for key, value in quiz.items() :
        questionTitle = 'Question id ' + str(key)
        print(questionTitle)
        print("=" * len(questionTitle), "\n")
        print(value["description"])
        print(value["text"])
        print(value["qtype"])
        print(value["answers"])
        print(value["feedback"])
        print(value["points"])
        print("\n\n")
        
