# Testing file: crosswords/1976/01/01.json

import json
from tkinter import *
import tkinter.font as font


def addtoDic (words, clues):
    tempDic = {}
    for i in range(len(words)):
        temp = tuple(words[i])
        clue = clues[i][clues[i].find(' ') + 1:] # removes the clue number from the front of the clue
        tempDic[temp] = clue
    return tempDic


def formatClues(acrossCluesList, downCluesList):
    acrossColumn = 'Across:\n'
    for clue in acrossCluesList:
        acrossColumn += clue + '\n'
    downColumn = 'Down\n'
    for clue in downCluesList:
        downColumn += clue + '\n'
    return acrossColumn, downColumn


def windowMaker(length, width, grid, gridNums):

    def correctText(*args):
        value = var.get()

        if len(value) > 1: value = value[len(value) - 1]
        value = value.upper()

        var.set(value)

        """ OG Code that kinda works
        curr = varList[x][y]
        value = curr.get()

        if len(value) > 1: value = value[len(value) - 1]
        value = value.upper()

        var.set(value)
        """

    def compareAnswer(*args):
        test = []
        for stuff in varList:
            for shit in stuff:
                test.append(shit.get())
        print(test)
        '''for i in range(0, len(grid)):
            if test[i] != grid[i]:
                
                e.config(background="red")
                print(test[i], "That shit wrong yo")
            else:
                print(test[i], "is correct")
'''
        count = 0
        for x in range(0, len(textBoxes)):
            for y in range(0, len(textBoxes[x])):
                if test[count] != grid[count]:
                    e = Entry(eFrame, font=("Comic Sans MS", 20), relief="flat", highlightcolor="white", justify="center",
                          textvariable=var, foreground="red")
                    textBoxes[x][y] = e
                    c.update()
                    print(test[count], "That shit wrong yo")
                else:
                    e = Entry(eFrame, font=("Comic Sans MS", 20), relief="flat", highlightcolor="white", justify="center",
                              textvariable=var, foreground="black")
                    textBoxes[x][y] = e
                    c.update()
                    print(test[count], "is correct")
                count += 1

    root = Tk()
    root.title("Crossword Simulator 2020")
    root.minsize(1200, 800)

    mycolor = '#%02x%02x%02x' % (255, 255, 255)

    c = Canvas(bg=mycolor, width='512', height='512')
    c.pack(side='top', fill='both', expand='1')

    rects = [[None for x in range(width + 1)] for y in range(length + 1)]
    handles = [[None for x in range(width + 1)] for y in range(length + 1)]
    rsize = 512 / 10
    guidesize = 512 / 0.665

    (xr, yr) = (1 * rsize, 1 * rsize)
    rects[0][0] = c.create_rectangle(xr, yr, xr + guidesize,
                                     yr + guidesize, width=3)

    userInputs = []
    textBoxes = []
    varList = []

    count = 0
    for y in range(1, length + 1):
        boxRow = []
        varRow =[]

        for x in range(1, width + 1):
            var = StringVar()

            (xr, yr) = (x * rsize, y * rsize)
            r = c.create_rectangle(xr, yr, xr + rsize, yr + rsize)

            '''eFrame = Frame(root, width=25, height=25)
            eFrame.pack()'''

            if grid[count] == ".":
                eFrame = Frame(root, width=25, height=25, background="black")
                eFrame.pack()
                c.create_rectangle(xr, yr, xr + rsize, yr + rsize, fill="black")
                t = c.create_window(xr + rsize / 2 + 5, yr + rsize / 2 + 5, window=eFrame)
            else:
                eFrame = Frame(root, width=25, height=25)
                eFrame.pack()
                e = Entry(eFrame, font=("Comic Sans MS", 20), relief="flat", highlightcolor="white", justify="center",
                          textvariable=var)
                # adding each entry to a list, so they can be accessed later (for checking purposes)
                boxRow.append(e)

                e.place(x=0, y=0, height=25, width=25)
                t = c.create_window(xr + rsize / 2 + 5, yr + rsize / 2 + 5, window=eFrame)

            handles[y][x] = (r, t)

            varRow.append(var)

            if gridNums[count] != 0:
                c.create_text(xr + 10, yr + 10, fill="black", font=("Comic Sans MS", 10), text=gridNums[count])
            count += 1

        textBoxes.append(boxRow)
        varList.append(varRow)

    '''for y in range(0, length):
        for x in range(0, width):
            textBoxes[x][y].bind("<Key>", correctText)'''

    root.canvas = c
    checkButton = Button(text="Check Puzzle", command=compareAnswer)
    checkButton.config(height=3, width=20)
    checkButton.pack(side=LEFT, padx=60, pady=20)

    displayClues(acrossString, downString, c)

    # c.bind("<Key>", correctText)
    # compareAnswer(varList, grid)

    root.mainloop()


def displayClues(acrossString, downString, canvas):
    c = canvas
    c.create_text(850, 60, fill="black", font=("Comic Sans MS", 8), text=acrossString, anchor='nw')
    c.create_text(1050, 60, fill="black", font=("Comic Sans MS", 8), text=downString, anchor='nw')


# Begin main
file = open("crosswords/1976/01/01.json")

jsonDta = json.load(file)

columns = jsonDta['size']['cols']
rows = jsonDta['size']['rows']
author = jsonDta['author']
editor = jsonDta['editor']
title = jsonDta['title']

acrossWords = jsonDta['answers']['across']
acrossClues = jsonDta['clues']['across']
downWords = jsonDta['answers']['down']
downClues = jsonDta['clues']['down']

allWords = acrossWords + downWords
allClues = acrossClues + downClues

grid = jsonDta['grid']
gridNums = jsonDta['gridnums']

acrossString, downString = formatClues(acrossClues, downClues)

windowMaker(rows, columns, grid, gridNums)
