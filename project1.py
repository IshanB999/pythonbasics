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
    print("Here is your first question for 500 rupees")
    print(quest[0])
    ans=input("your answer ")
    if ans=="paris"or"Paris":
        print("Thats a correct answer. Congratulations you win 500 rupees")
        cont=input("You wanna continue: ")
        if cont=="y":
            print("Here is your second question for 1000 rupees")
            print(quest[1])
            ans=input("your answer ")
            if ans=="mars" or "Mars":
                print("Thats a correct answer. Congratulations you win 1000 rupees")
                cont=input("You wanna continue: ")
                if cont=="y":
                    print("Here is your third question for 5000 rupees")
                    print(quest[2])
                    ans=input("your answer ")
                    if ans=="h2o"or"H2O":
                        if cont=="y":
                            if ans=="William Shakespeare"or "william Shakespeare":
                                if cont=="y":
                                    if ans=="Pacific Ocean"or"pacific ocean":
                                        if cont=="y":
                                            if ans=="Mitochondria"or"mitochondria":
                                                if cont=="y":
                                                    if ans=="Hydrogen"or"hydrogen":
                                                        if cont=="y":
                                                            if ans=="nile river"or"Nile River":
                                                                if cont=="y":
                                                                    if ans=="Japan"or"japan":
                                                                        if cont=="y":
                                                                            if ans=="Leonardo da Vinci"or"leonardo da vinci":
                                                                            else:
                                                                                print("Thats incorrect. The correct answer is Paris")
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

                                                            else:
                                                                print("Thats incorrect. The correct answer is Paris")
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

                                            else:
                                                print("Thats incorrect. The correct answer is Paris")
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

                            else:
                                print("Thats incorrect. The correct answer is Paris")
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


            else:
                print("Thats incorrect. The correct answer is Paris")
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


