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
    
    clearScreen()
    choice = displayMenu('Création d\'un questionnaire', mainOptions)
    
    if choice == 1 : # Add a question
        clearScreen()
        addChoice = displayMenu('Ajout d\'une nouvelle question', addOptions)
        if addChoice == 1 :
            pass
        elif addChoice == 2 :
            pass
        elif addChoice == 3 :
            pass
        else : # back to the main menu
            pass
    elif choice == 2 : # Edit a question
        # display all the questions and answers first
        # then ask for the chosen id
        # 
        pass
    elif choice == 3 : # Remove a question
        pass
    elif choice == 4 : # Display chosen questions
        clearScreen()
        addChoice = displayMenu('Affichage d\'énoncés de questions', 
                                displayOptions)
        if addChoice == 1 : # Display all questions text
            printQuiz()
            input("Appuyer sur une touche")
        elif addChoice == 2 : # Display chosen questions text
            pass
        else : # back to the main menu
            pass
    elif choice == 5 : # export questions to web page
        clearScreen()
        addChoice = displayMenu('Export de questions', exportOptions)
        if addChoice == 1 : # Export all questions
            pass
        elif addChoice == 2 : # Export chosen questions
            pass
        else : # back to the main menu
            pass
    elif choice == 6 :
        saveQuizToFile()
    else : # Quit
        if (isModified 
            and 
            input("Des changements ont été faits. Voulez-vous les enregistrer (o / n) ? ") == 'o') :
            saveQuizToFile()
        break

