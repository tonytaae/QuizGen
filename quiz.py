#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# answer type (dict) :
# {'text' : string,
#  'fraction' : integer in [0 ; 100]
# }

# questionInfos type (dict) :
# {'description' : string,
#  'text' : string,
#  'qtype' : string in ['qcm', 'shortanswer'], # must think to all questions types we'll manage
#  'answers' : array of 'answer',
#  'feedback' : string,
#  'points' : float
# }

# quiz type (dict) : 
# {'id' : questionInfos}

import json

quiz = {}
quizFileName = 'quiz.json'
questionId = 0
isModified = False

def addQuestion(description, text, qtype, answers, feedback, points) :
    global questionId
    global isModified
    
    questionId += 1
    quiz[questionId] = {'description' : description,
        'text' : text, 
        'qtype' : qtype,
        'answers' : answers,
        'feedback' : feedback,
        'points' : points
        }
    isModified = True

def modifyQuestion(id, description, text, qtype, answers, feedback, points) :
    global isModified
    
    quiz[id] = {'description' : description,
        'text' : text, 
        'qtype' : qtype,
        'answers' : answers,
        'feedback' : feedback,
        'points' : points
        }
    isModified = True

def deleteQuestion(id) :
    global isModified
    
    del quiz[id]
    isModified = True
    
def isQuizModified() :
    return isModified
    
def loadQuizFromFile() :
    try :
        global questionId
        with open(quizFileName) as quizFile :
            tempQuiz = json.load(quizFile)
            quizFile.close()
            
            for qIdStr in tempQuiz.keys() :
                qIdInt = int(qIdStr)
                quiz[qIdInt] = tempQuiz[qIdStr]
                if questionId < qIdInt :
                    questionId = qIdInt
    except :
        print('Quiz inexistant. Nouveau quiz en cours de création')
        pass

def saveQuizToFile() :
    global isModified
    
    try :
        with open(quizFileName, 'w') as quizFile :
            json.dump(quiz, quizFile)
            quizFile.close()
        isModified = False
    except :
        print('Erreur dans la sauvegarde des modifications')

# for testing only
def printQuiz():
    for key, value in quiz.items() :
        id=int(key)
        point=quiz[id]['points']
        if point>1:            
            questionTitle = 'Question id ' + str(id) + ' (' + str(point) + ' points)'
        else:
            questionTitle = 'Question id ' + str(id) + ' (' + str(point) + ' point)'  
        print(questionTitle)
        print('=' * len(questionTitle), '\n')
        print(value['text'], '\n')
        
        number = 1
        for answer in value['answers'] :
            print("{:d}. {:s}".format(number, answer['text']))
            number += 1
        print('\n')
       
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def printQuizMore(numbers):
    numbers=numbers.split(',')
    for key in numbers:
        id=int(key)
        print('Description: ' + quiz[id]['description'])  
        print('Type: ' + quiz[id]['qtype'])  
        print('Question: ' + quiz[id]['text'])     
        number = 1
        for answer in quiz[id]['answers'] :
            if answer['fraction']!=0:       
                print("Réponse {:d}: {:s} (Fraction:{:d})".format(number, answer['text'], answer['fraction']))
            else:
                print("Réponse {:d}: {:s}".format(number, answer['text']))
            number += 1
        print('Feedback:' + quiz[id]['feedback'])  
        print('Points:' + str(quiz[id]['points']))            
        print('\n')         
    
def printQuizPlus(numbers):
    numbers=numbers.split(',')
    for key in numbers:
        id=int(key)
        point=quiz[id]['points']
        if point>1:            
            questionTitle = 'Question id ' + str(id) + ' (' + str(point) + ' points)'
        else:
            questionTitle = 'Question id ' + str(id) + ' (' + str(point) + ' point)' 
        print(questionTitle)
        print('=' * len(questionTitle))
        print(quiz[id]['text'])
        number = 1
        for answer in quiz[id]['answers'] :
            if answer['fraction']!=0:       
                print("    {:d}. {:s} ({:d})".format(number, answer['text'], answer['fraction']))
            else:
                print("    {:d}. {:s}".format(number, answer['text']))
            number += 1
        print('\n')   
