#Project 1 : Who wants to became a millionaire ! is done here using function ,for loop,if else statement
#while in project1 is previously done using if else statement only

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
    ans=["c","b","a","c","c","c","b","b","b","c"]
    amount=[500,1000,2000,4000,8000,20000,50000,100000,500000,1000000]

    for i in range(0,10):        #for questions running loop form 0-9
      print(quest[i])            
      
      def incre():
          yourans=input("Enter your ans: ")               #taking answer as an string input
          if yourans==ans[i]:                        #running if statement to check if the answer is correct or not ,storing the correct answers in list ans
              print("Congratulations thats a correct answer .You have won ",amount[i])
              cont=input("Do you wanna continue or quit the game: ")
              if cont=="continue":
                  return i+1               #if wanna continue returning the value of i by incrementing 1 for next question
              else:
                  print("You have quitted the game .")
                  sys.exit()
          else:
              print("Thats incorrect answer. You are eliminated")
              sys.exit()

          

      val=incre()            #calling the fucntion , so every time incre function is called; answer is checked
      i=val                  # if correct and wanna continue then the i is incremented by 1 and its value is returned
                            # so next question is displayed
                
    else:
        sys.exit()


else:
    print("You have quitted the game")
    sys.exit()

    
