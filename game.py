from time import sleep as delay
from sys import exit as quit
import readsettings as rs

coins = 0
print("Welcome To Coin Clicker 2")

def startmenu():
    print("Type play To Play")
    print("Type quit To Quit")
    menuchoice = input(">> ")
    if menuchoice.lower() == "play":
        quit(0)
    elif menuchoice.lower() == "quit":
        quit(0)
    else:
        print("Unkown Command Entered")
        startmenu()
startmenu()

while True:
    print("Type a command")
    print("Type help for commands")
    menuchoice = input(">> ")
    if not(input("Press any key and press enter: ") == ""):
        coins += 1
        print("You Got A Coin!")
        f = open('coin.txt')
        print("-+yy:-")
        print("-ddNd/h:")
        print(":ddmh/h/")
        print("-+oo::` ")
        print("You Now Have {0} Coins".format(coins))
        print("Keep Going!")
    else:
        print("You didn't press any key and press enter")
        print("Try again")
