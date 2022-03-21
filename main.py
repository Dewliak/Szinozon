import random
from collections import defaultdict
from colorama import Fore, Back, Style,init
import os
init(convert=True)

colormap = {
    "red" : Fore.RED,
    "white": Fore.WHITE,
    'blue': Fore.BLUE,
    "pink": Fore.LIGHTMAGENTA_EX,
    "yellow": Fore.YELLOW,
    "purple": Fore.MAGENTA,
    "green": Fore.GREEN,
    "black": Fore.BLACK,

}

class Color:

    def __init__(self):
        RED = "red"
        WHITE = 'white'
        BLUE = 'blue'
        PINK = 'pink'
        YELLOW = 'yellow'
        PURPLE = 'purple'
        GREEN = 'green'
        self.color = {

            1 : RED,
            2 : WHITE,
            3 : BLUE,
            4 : PINK,
            5 : YELLOW,
            6 : PURPLE,
            7 : GREEN,
        }





def readInput(color):
    amount = defaultdict(lambda : 0)
    for i in color:
        amount[i] += 1

    return amount


def checkGreen(amount,colors,player,solution):
    for i in range(len(player)):
        if player[i] == colors[i]:
            solution[i] = 'green'
            amount[player[i]] -= 1

    return solution

def checkYellow(amount,colors,player,solution):
    for i in range(len(player)):
        if player[i] in colors and solution[i] != 'green' and amount[player[i]] > 0:
            solution[i] = "yellow"
            amount[player[i]] -= 1

    return solution


def printRow(arr,brr):
    string = ""

    for i in arr:
        string += colormap[i] + "●"+ " "

    string += colormap["white"] +  "| "

    for i in brr:
        string += colormap[i] + "●"+ " "

    print(string)

def printEmpty():
    print(colormap["white"] + "○ " + "○ " + "○ " + "○ ")

if __name__ == "__main__":
    c = Color()
    solution = ['black' for i in range(4)]
    amount = defaultdict(lambda : 0)
    #colors = [c.color[random.randint(1, 7)] for i in range(4)]
    prev = []
    colors = ["red", 'green', 'blue', 'purple']
    player = ["blue",'red','blue','purple']


    amount = readInput(colors)
    flag = True
    counter = 0
    solution = checkGreen(amount,colors,player,solution)
    solution = checkYellow(amount,colors,player,solution)

    prev.append(tuple([player,solution]))

    print(colors)
    printRow(colors,[])

    for i in prev:
        printRow(i[0],i[1])

    for i in range(11-len(prev)):
        printEmpty()


    #printRow()