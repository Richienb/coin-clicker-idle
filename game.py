from time import sleep as delay
coins = 0
while True:
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
