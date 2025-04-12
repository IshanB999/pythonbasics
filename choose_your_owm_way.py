name=input("Type your name :")
print("Welcome",name,"to the game where you gonna chose your owm path and have fun")

answer=input('''You have been involving in gambling recently.Today while you are betting the cops arrived and 
              now you are running from them . Now you have to choose your own path and run from cops .Lets start 
             .If you wanna exit the gambling spot from door type door and if from window type window   ''')

if answer=="door":
   
    answer=input('''Now you have exited through door there are two ways ahead. A way leading to highway and a way leading to river
          .If you want to towards highway type "highway" or if you want to go towards river type "river"   ''')
    if answer=="highway":

         answer=input('''You have reached a citymall in highway. Now if you want to hijack a car and run 
                       then type "hijack" or if you want to hide inside the mall type "hide"     ''')
         if answer=="hijack":
            print("You have escaped successfully and You won")
         elif answer=="hide":
            print("you got caught and you lost")
         else:
            print("Thats not a valid answer")

    elif answer=="river":
        print("You have reached the river. You died of drowing .You lost")
    else:
        print("Thats a invalid answer")



elif answer=="window":
    answer=input('''You have exited from the window and its glass cut you thighs so you are bleeding now . There is a 
           hospital nearby ,if you want to head to hospital type "hospital" or if you want to run bleeding type "run"    ''')

    if answer=="hospital":
        print("You reached the hospital but got caught later and you lost the game")
    elif answer=="run":
        print("You died of bleeding")
    else:
        print("Thats not a valid answer")

else:
    print("Thats a invalid answer")

print("The game has ended")
    
