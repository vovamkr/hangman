pred = ["кот","собака","самолет","город",
        "прогулка","подъезд","сквозняк",
        "компьютер","лиса","доктор","знак",
        "победа","грузовик","амбивалентность"]
import random
a = random.randint(0, len(pred))
## Здесь я создаю список, и путем вызова рандома создаю число, которое
## будет случайно выбираться из индексов этого списка (от 0 до длины списка)
def hangman(word):
    wrong = 0
    
    stages = ["",
              "_________          ",
              "!                  ",
              "!        !         ",
              "!        0         ",
              "!       /!\        ",
              "!       / \        ",
              "!                  ",
              ]
               
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to the CUM zone!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Enter a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1      
        print ("\n".join(stages[0: e]))
        if "_" not in board:
            print("You won! The answer is: {}.".format(word))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! The answer is: {}.".format(word))
word = pred[a]
hangman(word)
## Я кладу в переменную, отвечающую за слово в игре, рандомное число, выбранное
## ранее. Этим числом выбирается индекс в списке, и выдается рандомное слово.
                
                
