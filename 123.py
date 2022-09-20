from random import randint

print('Nhap Dam,La,Keo:')
player = input()
computer = randint(0,2)

if computer == 0:
    computer = 'Dam'
if computer == 1:
    computer = "La"
if computer == 2:
    computer = "Keo"

print("Ban chon : " + player + " May chon : " + computer)
print("-----") 

if player == computer:
    print("Draw")
else:
    if player == "Dam":
        if computer == "La":
            print("Lose")
        else:
            print("Win")

    elif player == "La":
        if computer == "Dam":
            print("Win")
        else:
            print("Lose")

    elif player == "Keo":
        if computer == "Dam":
            print("Lose")
        else:
            print("Win")

    else:
        print("Dau vao khong dung")