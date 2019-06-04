#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from menu import *
from quiz import *

mainOptions = ['Ajouter une nouvelle question',
               'Modifier une question',
               'Supprimer une question',
               'Afficher des questions',
               'Exporter les questions sous forme de page web',
               'Enregistrer les changements',
               'Quitter'
               ]

addOptions = ['Ajouter une question de type QCM, pour laquelle on saisit'
              + ' toutes les réponses possibles',
              'Ajouter une question de type QCM aléatoire portant sur l\'addition et la conversion',
              'Ajouter une question qui attend la saisie d\'une réponse (non aléatoire)',
              'Ajouter une question qui attend la saisie d\'une réponse (aléatoire)',
              'Revenir au menu principal'
              ]

displayOptions = ['Afficher les énoncés de toutes les questions',
                  'Choisir des questions',
                  'Revenir au menu principal'
                  ]

exportOptions = ['Exporter toutes les questions',
                 'Choisir des questions',
                 'Revenir au menu principal'
                 ]

# Some examples (addQuestion(), modifyQuestion(), deleteQuestion())
#addQuestion('Conversion de base en base',
#            'Quelle est la couleur du cheval banc de Henri IV ?',
#            'qcm',
#            [{'text' : 'bleu', 'fraction' : 0},
#             {'text' : 'blanc', 'fraction' : 100},
#             {'text' : 'rouge', 'fraction' : 0}
#             ],
#            'La réponse est dans la question !',
#            1
#            )
#
#addQuestion('Conversion de base en base',
#            '3 + 2 = ?',
#            'qcm',
#            [{'text' : '3', 'fraction' : 0},
#             {'text' : '4', 'fraction' : 0},
#             {'text' : '5', 'fraction' : 100}
#             ],
#            'Tu peux compter sur tes doigts !',
#            1
#            )
#
#addQuestion('Conversion de base en base',
#            '0 + 0 = ?',
#            'qcm',
#            [{'text' : '0', 'fraction' : 50},
#             {'text' : 'La tête à Toto', 'fraction' : 50},
#             {'text' : 'C\'est trop dur !', 'fraction' : 0}
#             ],
#            'Il y a deux réponses possibles !',
#            1
#            )
#deleteQuestion(2)
#modifyQuestion(1,
#               'Question bête',
#               'Quelle est la couleur du cheval blanc d\'Henri IV ?',
#               'qcm',
#               [{'text' : 'bleu', 'fraction' : 0},
#                {'text' : 'blanc', 'fraction' : 100},
#                {'text' : 'rouge', 'fraction' : 0}
#                ],
#               'La réponse est dans la question !',
#               1
#               )

loadQuizFromFile()

while True :

    choice = showMenu('Création d\'un questionnaire', mainOptions)

    if choice == 0 : # Add a question
        clearScreen()
        choice = showMenu('Ajout d\'une nouvelle question', addOptions)
        if choice == 0 :
            print('Ajouter une question QCM et toutes les réponses:')
            print('--------- Exemple ----------')
            print('Description:Addition \ntype:qcm')
            print('Question:1+1=? \n     Réponse:2   fraction:50\n     Réponse:3   fraction:0\n     Réponse:2.0 fraction:50')
            print('Aide: deux\npoint:1')
            print('----------------------------')
            description=input('Description:')
            qtype=input('Type:')
            qtext=input('Question:')
            lansw=[]
            again='o'
            while again!='n':
                nextanwser=1
                rtext=input('Réponse:')
                fraction=int(input('Fraction:'))
                lansw.append({'text': rtext, 'fraction' : fraction})
                again=input('Ajouter une autre réponse? o/n: ')
            feedback=input('Aide:')
            points=float(input('points:'))
            addQuestion(description, qtext, qtype, lansw, feedback, points)
            printQuiz()
            print(lanw)
        elif choice == 1 :
            pass
        elif choice == 2 :
            pass
        else : # back to the main menu
            pass
    elif choice == 1 : # Edit a question
        # display all the questions and answers first
        # then ask for the chosen id
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
    elif choice == 2 : # Remove a question
        printQuiz()
        key=int(input('Entrer l\'id de la question:'))
        deleteQuestion(key)
    elif choice == 3 : # Display chosen questions
        choice = showMenu('Affichage d\'énoncés de questions', displayOptions)
        if choice == 0 : # Display all questions text
            print('Affichage de toutes les questions: \n')
            printQuiz()
            input('Appuyer sur une touche')
        elif choice == 1 : # Display chosen questions text
            clearScreen()
            print('Affichage de questions:')
            print('Utiliser le format suivant pour afficher les questions 1, 2 et 9: 1,8,9')
            numbers = input('Entrer les numéros:')
            printQuizPlus(numbers)
            input('Appuyer sur une touche')
        else : # back to the main menu
            pass
    elif choice == 4 : # export questions to web page
        choice = showMenu('Export de questions', exportOptions)
        if choice == 0 : # Export all questions
            pass
        elif choice == 1 : # Export chosen questions
            pass
        else : # back to the main menu
            pass
    elif choice == 5 :
        saveQuizToFile()
    else : # Quit
        if (isQuizModified()
            and
            input("Des changements ont été faits. Voulez-vous les enregistrer (o / n) ? ") == 'o') :
            saveQuizToFile()
        break
