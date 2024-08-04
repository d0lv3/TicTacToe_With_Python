from random import randint
from time import sleep
def main_menu():
    print("Welcome to TicTacToe By Abdallah Alnuaimy")
    print("Starting the Toss", end="")
    for _ in range(0, 3):
        sleep(0.5)
        print(".", end="")
        sleep(0.5)
    print()
    Turn = Toss()
    print(f"{Turn} Starting:")
    xoImplementation(Turn)
    
def xoImplementation(Turn):
    n = 0
    reserved_places = []
    struc = {'n1' : "1",
             'n2' : "2",
             'n3' : "3",
             'n4' : "4",
             'n5' : "5",
             'n6' : "6",
             'n7' : "7",
             'n8' : "8",
             'n9' : "9"}
    
    
    while n<=9:
        print(f"   {struc['n1']}  |  {struc['n2']}  |  {struc['n3']}  \n--------------------\n   {struc['n4']}  |  {struc['n5']}  |  {struc['n6']}  \n--------------------\n   {struc['n7']}  |  {struc['n8']}  |  {struc['n9']}   ")
        
        #Checking the winner conds
        if n>=5 and n<=9:
            winning_probs = [(struc['n1'], struc['n2'], struc['n3']), (struc['n4'], struc['n5'], struc['n6']), (struc['n7'], struc['n8'], struc['n9']), (struc['n1'], struc['n4'], struc['n7']), (struc['n2'], struc['n5'], struc['n8']), (struc['n3'], struc['n6'], struc['n9']), (struc['n1'], struc['n5'], struc['n9']), (struc['n3'], struc['n5'], struc['n7'])]
            for i in winning_probs:
                if i == ('X', 'X', 'X'):
                    end('X')
                elif i == ('O', 'O', 'O'):
                    end('O')
                    
        #Draw condtion
        if n == 9:
            end('D')
            
        #X's Turn
        if Turn == 'X':
            print("X's Turn")
            inp = input()
            if inp in reserved_places:
                print("Wrong input! Reserved place, try again please.")
                continue
            for i in struc.keys():
                if inp == i[-1]:
                    struc[i] = 'X'
                    reserved_places.append(inp)
                    n += 1
            Turn = 'O'
            continue
        
        #Y's Turn
        elif Turn == 'O':
            print("O's Turn")
            inp = input()
            if inp in reserved_places:
                print("Wrong input! Reserved place, try again please.")
                continue
            for i in struc.keys():
                if inp == i[-1]:
                    struc[i] = 'O'
                    reserved_places.append(inp)
                    n += 1
            Turn = 'X'
    
def Toss():
    Turn = None
    i = randint(0, 2)
    if i == 0:
        Turn = 'O'
    else:
        Turn = 'X'
    return Turn

def end(State):
    if State == 'D':
        print("it's a DRAW!")
    else:
        print(f"Congratulations! {State} Won!")
    choice = input("Would you like to play again? \nEnter (y) for Yes and (n) for No: ")
    while True:
        if choice in ['y', 'Y']:
            main_menu()
        elif choice in ['n', 'N']:
            exit()
        else:
            print("Wrong input")
main_menu()
