# Rock ,paper and scissor game

import random
import sys
print("Welcome to rock, paper and scissor")

def rand():
    choice=["rock",'paper','scissor']
    return random.choice(choice)            #this function will return random value from the list

                     

def choice():
    user_choice=input("Enter rock, paper or scissor: ")
    if user_choice not in ("rock","paper",'scissor'):
        print("Invalid input")
        return choice()
    else:
        return user_choice                   #this function will ask and return the choice from the user 

                          


def play():   
    input1=rand()                #it will store the random rock, paper, scissor returned by rand( )
    input2=choice()             #it will store the rock,paper,scissor given by the user
    result=[''' rock and rock;     draw.       Try again:''',
            ''' rock and scissor; you lose. Try again''',
            ''' rock and paper; its a win. Nice game''',
            ''' paper and paper; its a draw. Try again''',
            ''' paper and scissor; its a win. Nice game''',
            ''' paper and rock; you lose. Try again''',
            ''' scissor and scissor; its a draw. Try again''',
            ''' scissor and paper; you lose. Try again''',
            ''' scissor and rock; its a win. Nice game''']
    
    
        

    if input1=="rock" and input2=="rock":
        print(result[0])
    elif input1=="rock" and input2=="scissor":
        print(result[1])
    elif input1=="rock" and input2=="paper":
        print(result[2])
    elif input1=="paper" and input2=="paper":
        print(result[3])
    elif input1=="paper" and input2=="scissor":
        print(result[4])
    elif input1=="paper" and input2=="rock":
        print(result[5])
    elif input1=="scissor" and input2=="scissor":
        print(result[6])
    elif input1=="scissor" and input2=="paper":
        print(result[7])
    elif input1=="scissor" and input2=="rock":
        print(result[8])
    else:
        print("Error occured")

    def play_again():
        print("Enter  or   quit")       #press enter to continue and enter quit to quit the game
        user_input=input()
        if user_input=="":
            play()
        elif user_input=="quit":
            print("You have quitted the game")
            sys.exit()
        else:
            print("Error occured")
            play_again()

    play_again()

play()
        
        

        


