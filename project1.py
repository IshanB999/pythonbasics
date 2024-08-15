#Project first; Who wants to became Millionaire?
import sys
print("Welcome to  Who Want To Became A Millionaire!")
cont=input("You wanna continue type y else n ")
if cont=="y":
    print("This gonna be a Question/Answer round and if you give correct answers you will win money")
else:
    print("You are quitting the game")
    sys.exit()
cont=input("Do you like to play?")
if cont=="y":
    quest=['''1. What is the capital of France?
                  A) Madrid
                  B) Berlin
                  C) Paris 
                  D) Rome''',
              '''2. Which planet is known as the Red Planet?
                  A) Venus
                  B) Mars 
                  C) Jupiter
                  D) Saturn''',
                 ''' 3. What is the chemical symbol for water?
                  A) H₂O 
                  B) O₂
                  C) CO₂
                  D) H₂''',
                 ''' 4. Who wrote the play "Romeo and Juliet"?
                  A) Charles Dickens
                  B) Leo Tolstoy
                  C) William Shakespeare 
                  D) Mark Twain''',
                 ''' 5. What is the largest ocean on Earth?
                  A) Atlantic Ocean
                  B) Indian Ocean
                  C) Pacific Ocean 
                  D) Arctic Ocean''',
                  '''6. What is the powerhouse of the cell?
                  A) Nucleus
                  B) Ribosome
                  C) Mitochondria 
                  D) Chloroplast''',
                 ''' 7. Which element has the atomic number 1?
                  A) Helium
                  B) Hydrogen 
                  C) Oxygen
                  D) Nitrogen''',
                 ''' 8. What is the longest river in the world?
                  A) Amazon River
                  B) Nile River 
                  C) Yangtze River
                  D) Mississippi River''',
                  '''9. Which country is known as the Land of the Rising Sun?
                  A) China
                  B) Japan 
                  C) South Korea
                  D) Thailand''',
                ''' 10. Who painted the Mona Lisa?
                  A) Vincent van Gogh
                  B) Pablo Picasso
                  C) Leonardo da Vinci 
                  D) Michelangelo''']
    print("Here is your first question for 500$")
    print(quest[0])
    ans=input("your answer ")
    if ans=="paris"or"Paris":
        print("Thats a correct answer. Congratulations you win 500$")
        cont=input("You wanna continue: ")
        if cont=="y":
            print("Here is your second question for 1000$")
            print(quest[1])
            ans=input("your answer ")
            if ans=="mars" or "Mars":
                print("Thats a correct answer. Congratulations you win 1000$")
                cont=input("You wanna continue: ")
                if cont=="y":
                    print("Here is your third question for 2000$")
                    print(quest[2])
                    ans=input("your answer ")
                    if ans=="h2o"or"H2O":
                        print("Thats a correct answer. Congratulations you win 2000$")
                        cont=input("You wanna continue: ")
                        if cont=="y":
                            print("Here is your fourth question for 4000$")
                            print(quest[3])
                            ans=input("your answer ")
                            if ans=="William Shakespeare"or "william Shakespeare":
                                print("Thats a correct answer. Congratulations you win 4000$")
                                cont=input("You wanna continue: ")
                                if cont=="y":
                                    print("Here is your fifth question for 8000$")
                                    print(quest[4])
                                    ans=input("your answer ")
                                    if ans=="Pacific Ocean"or"pacific ocean":
                                        print("Thats a correct answer. Congratulations you win 8000$")
                                        cont=input("You wanna continue: ")
                                        if cont=="y":
                                            print("Here is your sixth question for 10000$")
                                            print(quest[5])
                                            ans=input("your answer ")
                                            if ans=="Mitochondria"or"mitochondria":
                                                print("Thats a correct answer. Congratulations you win 10000$")
                                                cont=input("You wanna continue: ")
                                                if cont=="y":
                                                    print("Here is your seventh question for 20000$")
                                                    print(quest[6])
                                                    ans=input("your answer ")
                                                    if ans=="Hydrogen"or"hydrogen":
                                                        print("Thats a correct answer. Congratulations you win 20000$")
                                                        cont=input("You wanna continue: ")
                                                        if cont=="y":
                                                            print("Here is your eighth question for 50000$")
                                                            print(quest[7])
                                                            ans=input("your answer ")
                                                            if ans=="nile river"or"Nile River":
                                                                print("Thats a correct answer. Congratulations you win 50000$")
                                                                cont=input("You wanna continue: ")
                                                                if cont=="y":
                                                                    print("Here is your nineth question for 100000$")
                                                                    print(quest[8])
                                                                    ans=input("your answer ")
                                                                    if ans=="Japan"or"japan":
                                                                        print("Thats a correct answer. Congratulations you win 100000$")
                                                                        cont=input("You wanna continue: ")
                                                                        if cont=="y":
                                                                            print("Here is your tenth and final question for 1000000$")
                                                                            print(quest[9])
                                                                            ans=input("your answer ")
                                                                            if ans=="Leonardo da Vinci"or"leonardo da vinci":
                                                                                print("Thats a correct answer. Congratulations you win 1000000$")
                                                                                print("Thats the end of the final round")
                                                                                print("Congratulations! You have won a Million dollars")
                                                                            else:
                                                                                print("Thats incorrect. The correct answer is Leonardo da Vinci")
                                                                                print("You are eliminated")
                                                                                sys.exit()

                                                                        else:
                                                                            print("You have quitted the game")
                                                                            sys.exit()

                                                                    else:
                                                                        print("Thats incorrect. The correct answer is Japan")
                                                                        print("You are eliminated")
                                                                        sys.exit()

                                                                else:
                                                                    print("You have quitted the game")
                                                                    sys.exit()

                                                            else:
                                                                print("Thats incorrect. The correct answer is Nile River")
                                                                print("You are eliminated")
                                                                sys.exit()

                                                        else:
                                                            print("You have quitted the game")
                                                            sys.exit()

                                                    else:
                                                        print("Thats incorrect. The correct answer is Hydrogen")
                                                        print("You are eliminated")
                                                        sys.exit()

                                                else:
                                                    print("You have quitted the game")
                                                    sys.exit()

                                            else:
                                                print("Thats incorrect. The correct answer is Mitochondria")
                                                print("You are eliminated")
                                                sys.exit()

                                        else:
                                            print("You have quitted the game")
                                            sys.exit()

                                    else:
                                        print("Thats incorrect. The correct answer is Pacific Ocean")
                                        print("You are eliminated")
                                        sys.exit()

                                else:
                                    print("You have quitted the game")
                                    sys.exit()

                            else:
                                print("Thats incorrect. The correct answer is William Shakespeare")
                                print("You are eliminated")
                                sys.exit()

                        else:
                            print("You have quitted the game")
                            sys.exit()

                    else:
                        print("Thats incorrect. The correct answer is H2O")
                        print("You are eliminated")
                        sys.exit()

                else:
                    print("You have quitted the game")
                    sys.exit()


            else:
                print("Thats incorrect. The correct answer is Mars")
                print("You are eliminated")
                sys.exit()
                    
        else:
            print("You have quitted the game")
            sys.exit()


    else:
        print("Thats incorrect. The correct answer is Paris")
        print("You are eliminated")
        sys.exit()


else:
    print("You have quitted the game")
    sys.exit()


