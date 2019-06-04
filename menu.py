#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import system, name
import curses
# curses is already installed on linux and macOS
# pip install windows-curser for windows


# help : https://docs.python.org/3/howto/curses.html
# https://github.com/nikhilkumarsingh/python-curses-tut

menuTitle = ''
menuOptions = ''
choice = -1


def clearScreen() :
    if name == 'nt' : # for Windows
        system('cls')
    else : # for mac and linux
        system('clear')


def printTitle(consoleScreen) :
    height, width = consoleScreen.getmaxyx()
    x = width // 2 - len(menuTitle) // 2
    y = 5
    try :
        consoleScreen.addstr(y, x, menuTitle, curses.A_BOLD)
    except curses.error :
        pass
    consoleScreen.refresh()


def printMenu(consoleScreen, currentRow) :
    consoleScreen.clear()
    printTitle(consoleScreen)
    height, width = consoleScreen.getmaxyx()
    for index, option in enumerate(menuOptions) :
        x = width // 2 - len(option) // 2
        y = height // 2 - len(menuOptions) // 2 + index
        if index == currentRow :
            consoleScreen.attron(curses.color_pair(1))
            try :
                consoleScreen.addstr(y, x, option)
            except curses.error :
                pass
            consoleScreen.attroff(curses.color_pair(1))
        else :
            try :
                consoleScreen.addstr(y, x, option)
            except curses.error :
                pass


def show(consoleScreen) :
    global choice

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    currentRow = 0

    printMenu(consoleScreen, currentRow)
    while(True) :
        keyPressed = consoleScreen.getch()

        if keyPressed == curses.KEY_UP and currentRow > 0 :
            currentRow -= 1
        elif keyPressed == curses.KEY_DOWN and currentRow < len(menuOptions) - 1 :
            currentRow += 1
        elif keyPressed == curses.KEY_ENTER or keyPressed in [10, 13] :
            choice = currentRow
            break

        printMenu(consoleScreen, currentRow)


def showMenu(title, options) :
    global menuTitle
    global menuOptions

    menuTitle = title
    menuOptions = options
    curses.wrapper(show)
    # the wrapper calls showMenu giving it one paramater : the window object
    # which represents the whole console screen
    return choice
