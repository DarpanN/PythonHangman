import random
import time

def hangman(word):
    wrong = 0

    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome To Hangman..!!!")
    print("Guess The Programming Language..!!!")
    name = input("Enter Your Name: ")
    print("Welcome To Hangman Guessing Game", name + " Good Luck !!!")
    time.sleep(2)
    print("The game is about to start!\n Let's play Hangman!")
    time.sleep(3)





    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("​Congratulations " +"!!!" , name + " You Win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Sorry " + name + " You lose! It was {}.".format(word))

words = ["python", "java", "kotlin", "javascript", "ruby", "html", "php", "swift", "sql", "go", "dart", "c", "scala", "rust"]
word = random.choice(words)
hangman(word)
