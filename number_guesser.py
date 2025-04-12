import random 

while True:
    top_range=input("Enter the top range: ")
    if top_range.isdigit():
       top_range=int(top_range)
       if top_range <=0:
        print("Enter a number greater than 0 for top range ")
        continue
       if top_range >0:
        break
    else:
        print("Please enter a number for top range ")
    

rand_num=random.randint(0,top_range)
guesses=0

while True:
    guesses +=1
    user_guess=input("Enter your guess:")
    if user_guess=="q":
        print("You have quitted")
        quit()
    if user_guess.isdigit():
        user_guess=int(user_guess)
   
    else:
        print("Enter number as a guess")
        continue

    if user_guess==rand_num:
        print("You have won")
        break     
    elif user_guess<rand_num:
        print("Guess above")
    else:
        print("Guess below")    

print("You won in",guesses,"guesses")



