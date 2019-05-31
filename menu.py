#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import system, name

mainOptions = ["Ajouter une nouvelle question",
               "Modifier une question",
               "Supprimer une question",
               "Afficher les question",
               "Exporter les questions sous forme de page web",
               "Quitter"
               ]

addOptions = ["""Ajouter une question de type QCM, pour laquelle on saisit
              toutes les réponses possibles""",
              """Ajouter une question de type QCM, portant sur la somme de 
              nombres binaires et générée aléatoirement""",
              "Ajouter une question qui attend la saisie d'une réponse",
              "Revenir au menu principal"
              ]

def clearScreen() :
    if name == "nt" : # for Windows
        system("cls")
    else : # for mac and linux
        system("clear")

def inputInt(prompt) :
    while True :
         try :
             userInt = int(input(prompt))
             break
         except :
             pass
    return userInt

def displayMenu(title, options) :
    print(title)
    print("="*len(title), "\n\n")
    number = 1
    for option in options :
        print("{:d}. {:s}".format(number, option))
        number += 1
    
    choice = inputInt("\nChoisir une option : ")
    choiceRange = range(1,len(options)+1)
    while not(choice in choiceRange) :
        choice = inputInt("Choisir une option : ")
    
    return choice;