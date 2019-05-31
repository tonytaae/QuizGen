#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from menu import *
from questions import *

mainOptions = ["Ajouter une nouvelle question",
               "Modifier une question",
               "Supprimer une question",
               "Afficher les énoncés de toutes les questions",
               "Exporter les questions sous forme de page web",
               "Quitter"
               ]

addOptions = ["Ajouter une question de type QCM, pour laquelle on saisit"
              + " toutes les réponses possibles",
              "Ajouter une question de type QCM, portant sur la somme de"
              + " nombres binaires et générée aléatoirement",
              "Ajouter une question qui attend la saisie d'une réponse",
              "Revenir au menu principal"
              ]

while True :
    
    clearScreen()
    choice = displayMenu("Création d'un questionnaire", mainOptions)
    
    if choice == 1 : # Add a question
        clearScreen()
        addChoice = displayMenu("Ajout d'une nouvelle question", addOptions)
        if addChoice == 1 :
            pass
        elif addChoice == 2 :
            pass
        elif addChoice == 3 :
            pass
        else :
            pass
    elif choice == 2 : # Edit a question
        pass
    elif choice == 3 : # Remove a question
        pass
    elif choice == 4 : # Display all questions
        pass
    elif choice == 5 : # export questions to web page
        pass
    else : # Quit
        break

clearScreen()
addQuestion("Conversion de base en base",
            "Quelle est la couleur du cheval banc de Henri IV ?",
            "qcm",
            [{"text" : "bleu", "fraction" : 0},
             {"text" : "blanc", "fraction" : 100},
             {"text" : "rouge", "fraction" : 0}
             ],
            "La réponse est dans la question !",
            1
            )

addQuestion("Conversion de base en base",
            "3 + 2 = ?",
            "qcm",
            [{"text" : "3", "fraction" : 0},
             {"text" : "4", "fraction" : 0},
             {"text" : "5", "fraction" : 100}
             ],
            "Tu peux compter sur tes doigts !",
            1
            )

addQuestion("Conversion de base en base",
            "0 + 0 = ?",
            "qcm",
            [{"text" : "0", "fraction" : 50},
             {"text" : "La tête à Toto", "fraction" : 50},
             {"text" : "C'est trop dur !", "fraction" : 0}
             ],
            "Il y a deux réponses possibles !",
            1
            )

printQuiz()
deleteQuestion("2")
printQuiz()
modifyQuestion("1",
               "Question bête",
               "Quelle est la couleur du cheval blanc d'Henri IV ?",
               "qcm",
               [{"text" : "bleu", "fraction" : 0},
                {"text" : "blanc", "fraction" : 100},
                {"text" : "rouge", "fraction" : 0}
                ],
               "La réponse est dans la question !",
               1
               )
printQuiz()
