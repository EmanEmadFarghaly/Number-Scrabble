# File : CS112_A1_T2_Game#2_20230619
# Purpose : Two players take turns to choose number from 1 : 9, to get 3 numbers their sum=15
# Author : Eman Emad Abdelraheem Farghaly
# ID : 20230619
def game_score(choiceslist):
    if len(choiceslist) == 3:
        if sum(choiceslist) == 15:
            return True
    elif len(choiceslist) == 4:
        for i in choiceslist:
            newlist = choiceslist.copy()
            newlist.remove(i)
            if sum(newlist) == 15:
                return True


def player1_score(choiceslist):
    for i in choiceslist:
        newlist = choiceslist.copy()
        newlist.remove(i)
        for j in newlist:
            newlist2 = newlist.copy()
            newlist2.remove(j)
            if sum(newlist2) == 15:
                return True


player1choices = []
player2choices = []
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('*Welcome to the Number Scrabble Game*')
while len(mylist) > 0:
    # player1 turn
    print('Player1 Enter number from', mylist)
    x = int(input())
    while x not in mylist:
        print(mylist)
        x = int(input('player1 please enter valid from the list'))
    mylist.remove(x)
    player1choices.append(x)
    print('player 1 chose', player1choices)
    if game_score(player1choices):
        print('player 1 is the winner')
        break
    elif player1_score(player1choices):
        print('player 1 is the winner')
        break
    else:
        if len(mylist) == 0:
            print('The Game is a Draw')
            break
        # player2 turn
        print('Player2 Enter number from', mylist)
        y = int(input())
        while y not in mylist:
            print(mylist)
            y = int(input('player2 please enter valid from the list'))
        mylist.remove(y)
        player2choices.append(y)
        print('player 2 chose', player2choices)
        if game_score(player2choices):
            print('player 2 is the winner')
            break
        else:
            continue
