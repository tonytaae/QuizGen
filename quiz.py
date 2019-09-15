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
# from collections import OrderedDict

quiz = {}
exportquiz={}
quizFileName = 'quiz.json'
exportQuizFileName = 'exportquiz.json'
questionId = 0
isModified = False

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

def saveExportQuizToFile(dict_) :
    try :
        with open(exportQuizFileName, 'w') as exportQuizFile :
            json.dump(dict_, exportQuizFile)
            exportQuizFile.close()
        
    except :
        print('Erreur dans la sauvegarde des modifications')           

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

def InputQuestion():
    description=input('Description:')
    qtype=input('Type:')
    qtext=input('Question:')
    lansw=[]
    again='o'
    while again!='n':
        rtext=input('Réponse:')
        fraction=int(input('Fraction:'))
        lansw.append({'text': rtext, 'fraction' : fraction})
        again=input('Ajouter une autre réponse? o/n: ')
    feedback=input('Aide:')
    points=float(input('points:'))
    addQuestion(description, qtext, qtype, lansw, feedback, points)

def addQuestionQcmCloseMain():
    print('Ajouter une question QCM et toutes les réponses:')
    print('--------- Exemple ----------')
    print('Description:Addition \ntype:qcm')
    print('Question:1+1=? \n     Réponse:2   fraction:50\n     Réponse:3   fraction:0\n     Réponse:2.0 fraction:50')
    print('Aide: deux\npoint:1')
    print('----------------------------')
    InputQuestion()
    printQuiz()

def addQuestionOpenCloseMain():
    print('Ajouter une question qui attend la saisie d\'n une réponse (non aléatoire):')
    print('--------- Exemple ----------')
    print('Description:Addition \ntype:Ouverte')
    print('Question:1+1=? \n     Réponse:2   fraction:50\n     Réponse:2.0   fraction:50\n')
    print('Aide: deux\npoint:1')
    print('Attention: Chaque reponse doit être juste et le total de toutes les fractions doit être égal à 100.')
    print('----------------------------')
    InputQuestion()
    printQuiz()

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

def modifyQuestionMain():
    print('Modifier une question')
    printQuiz()
    key=input('Entrer l\'id de la question:')
    printQuizMore(key)
    print('Entrer les nouvelles valeurs:')
    description=input('Description:')
    qtype=input('Type:')
    qtext=input('Question:')
    lansw=[]
    id=int(key)
    number=1
    for elt in range(len(quiz[id]['answers'])):
        rtext=input('Réponse '+str(number)+':')
        fraction=int(input('Fraction:'))
        lansw.append({'text': rtext, 'fraction': fraction})
        number+=1
    feedback=input('Aide:')
    points=float(input('points:'))
    modifyQuestion(id, description, qtext, qtype, lansw, feedback, points)
    printQuizPlus(key)         
     
def deleteQuestion(id) :
    global isModified
    del quiz[id]
    isModified = True

def deleteQuestionMain():
    print('Supprimer une question')
    printQuiz()
    key=int(input('Entrer l\'id de la question à supprimer:'))
    deleteQuestion(key)
       
def printQuiz():
    for key, value in quiz.items() :
        id=int(key)
        point=quiz[id]['points']
        qtype=quiz[id]['qtype']
        if point>1:
            questionTitle = 'ID ' + str(id) + ' | ' + qtype + ' | ' + str(point) + ' points'
        else:
            questionTitle = 'ID ' + str(id) + ' | ' + qtype + ' | ' + str(point) + ' point'
        print(questionTitle)
#       print('=' * len(questionTitle), '\n')
        print(value['text'])
        number = 1
        for answer in value['answers'] :
            if answer['fraction']!=0:
                print("    {:d}. {:s}  ({}%)".format(number, answer['text'], answer['fraction']))
            else:
                print("    {:d}. {:s}".format(number, answer['text']))
            number += 1
        print('\n')

def printQuizMain():
    print('Affichage de toutes les questions: \n')
    printQuiz()
    input('Appuyer sur une touche')

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
        qtype=quiz[id]['qtype']
        if point>1:
            questionTitle = 'ID ' + str(id) + ' | ' + qtype + ' | ' + str(point) + ' points'
        else:
            questionTitle = 'ID ' + str(id) + ' | ' + qtype + ' | ' + str(point) + ' points'
        print(questionTitle)
#       print('=' * len(questionTitle))
        print(quiz[id]['text'])
        number = 1
        for answer in quiz[id]['answers'] :
            if answer['fraction']!=0:
                print("    {:d}. {:s} ({:d}%)".format(number, answer['text'], answer['fraction']))
            else:
                print("    {:d}. {:s}".format(number, answer['text']))
            number += 1
        print('\n')

def printQuizChosePlus(numbers):
    numbers=numbers.split(',')
    for key in numbers:
        id=int(key)
        point=quiz[id]['points']
        qtype=quiz[id]['qtype']
        if point>1:
            questionTitle = 'ID ' + str(id) + ' | ' + qtype + ' | ' + str(point) + ' points'
        else:
            questionTitle = 'ID ' + str(id) + ' | ' + qtype + ' | ' + str(point) + ' points'
        print(questionTitle)
#       print('=' * len(questionTitle))
        print(quiz[id]['text'])
        number = 1
        for answer in quiz[id]['answers'] :
            if answer['fraction']!=0:
                print("    {:d}. {:s} ({:d}%)".format(number, answer['text'], answer['fraction']))
            else:
                print("    {:d}. {:s}".format(number, answer['text']))
            number += 1
        print('\n')

def printQuizPlusMain():
    print('Affichage de quelques questions:')
    print('Utiliser le format suivant pour afficher les questions 1, 2 et 9: 1,8,9')
    numbers = input('Entrer les numéros:')
    printQuizPlus(numbers)
    input('Appuyer sur une touche')

def printQuizChoseMain():
    print('Choix des questions à générées:')
    printQuiz()
    print('Utiliser le format suivant pour choisir les questions 1, 2 et 9: 1,8,9')
    numbers = input('Entrer les numéros:')
    printQuizChosePlus(numbers)
    input('Appuyer sur une touche')

def printTotalPoint():
    total=0
    for key, value in quiz.items():
        id=int(key)
        point=quiz[id]['points']
        total += point
    print('Points total: ', total)

# Search elt in list     
def searchL(elt_, list_):    
    for elt in list_:
        if elt==elt_:
            return True
    return False

# Get all same type of question
def qtypeL(qtype_):
    lsameqtype=[]
    for key in quiz.items():
        id=int(key)
        qtype=quiz[id]['qtype']
        if qtype == qtype_:
            lsameqtype.append({'key': id})

def sortAllQuestion():
    #global quiz
    lqtype=[]
    # Get each type of question
    for key in quiz.items():
        id=int(key)
        qtype=quiz[id]['qtype']
        if searchL(qtype,lqtype) == False:
            lqtype.append({'qtype' : qtype})
    for elt in lqtype:
        print(qtypeL(elt))

    