def hangman(word):
    wrong = 0
    stages =["",
             "_______      ",
             "|            ",
             "|      |     ",
             "|      0     ",
             "|    ／|＼   ",
             "|    ／ ＼   ",
             "|            ",
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print(" ハングマンへようこそ！")
    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字予想してね："
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))


mydict = {"1": "Ducati",
          "2": "YAMAHA",
          "3": "Honda",
          }

#num = input("1～3の数字を入力してちょ：")
import random
num = random.randint(1,3)
num = str(num)
print(num)
word1 = mydict[num]
hangman(word1)
    
