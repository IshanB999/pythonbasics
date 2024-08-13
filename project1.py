#Project first; Who wants to became Millionaire?
import sys
print("Welcome to  Who Want To Became A Millionaire!")
cont=input("You wanna continue type y else n ")
if cont=="y":
    print("This gonna be a Question/Answer round and if you give correct answers you will win money")
else:
    print("You are quitting the game")
    sys.exit()
cont1=input("Do you like to play?")
if cont1=="y":
    quest=['''1. What is the capital of France?
                  A) Madrid
                  B) Berlin
                  C) Paris (Correct)
                  D) Rome''',
              '''2. Which planet is known as the Red Planet?
                  A) Venus
                  B) Mars (Correct)
                  C) Jupiter
                  D) Saturn''',
                 ''' 3. What is the chemical symbol for water?
                  A) H₂O (Correct)
                  B) O₂
                  C) CO₂
                  D) H₂''',
                 ''' 4. Who wrote the play "Romeo and Juliet"?
                  A) Charles Dickens
                  B) Leo Tolstoy
                  C) William Shakespeare (Correct)
                  D) Mark Twain''',
                 ''' 5. What is the largest ocean on Earth?
                  A) Atlantic Ocean
                  B) Indian Ocean
                  C) Pacific Ocean (Correct)
                  D) Arctic Ocean''',
                  '''6. What is the powerhouse of the cell?
                  A) Nucleus
                  B) Ribosome
                  C) Mitochondria (Correct)
                  D) Chloroplast''',
                 ''' 7. Which element has the atomic number 1?
                  A) Helium
                  B) Hydrogen (Correct)
                  C) Oxygen
                  D) Nitrogen''',
                 ''' 8. What is the longest river in the world?
                  A) Amazon River
                  B) Nile River (Correct)
                  C) Yangtze River
                  D) Mississippi River''',
                  '''9. Which country is known as the Land of the Rising Sun?
                  A) China
                  B) Japan (Correct)
                  C) South Korea
                  D) Thailand''',
                ''' 10. Who painted the Mona Lisa?
                  A) Vincent van Gogh
                  B) Pablo Picasso
                  C) Leonardo da Vinci (Correct)
                  D) Michelangelo''']
    print("Here is your first question for 500 rupees")
    print(quest[0])
    ans=input("your answer ")


