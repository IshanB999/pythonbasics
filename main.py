#Simple mathematical operations
# a=13
# b=4
# print("the value of ",a ,"+",b,"is",a+b)
# print (a-b)
# print(a/b)
# print(a*b)




#assigning same values to multiple variables in same line
# x=y=z=3
# print(x)
# print(y)
# print(z)



#If else condition

# a=int(input("Enter a number"))
# if (a>0 and a<=10):
#     print("a is a number between 0-10")
# elif(a>10 and a<100):
#     print("a is a number between 10 and 100")
# else:
#     print("a is either zero , negative or greater than 100")





#match case statement
# num=int(input("Enter a number"))

# match num:
#     case num if num>0:
#         print("positive number")

#     case num if num<0:
#         print("Negative number")
#     case _:
#         print("Zero")




# #For loop
# fruits=["Apple","mango","gauva","orange"]
# for fruit in fruits:
#     print(fruit)
#     for i in fruit:
#         print(i)



#for loop with range
# for x in range(1,100,5):
#     print(x)



#for loop with break statement
# fruits=["Apple","mango","gauva","orange"]
# for fruit in fruits:
#     print(fruit)
#     if (fruit=="gauva"):
#      break


#for loop with continue statement
# fruits=["Apple","mango","gauva","orange"]
# for x in fruits:
#     if(x=="mango"):
#         continue
#     print(x)
    
# for x in range(2,15):
#  print(x)        
# else:                          #for loop ma else statement loop sakkesi matra execute hunxa
#  print("finally completed")



# for x in range(2,15):
#  print(x)
#  if(x==10):
#   break  #break use gareko condition break vayo vani else statement execute hudaina
# else:
#  print("finally completed")


#nested for loop
# fruits=["mango","gauva","litchi","grapes"]
# car=["ferrera","nemerra","lambo"]

# for x in fruits:
#     for y in car:
#         print(x,y)
    


#while loop 
# i=0
# while i<10:
#     print(i)
#     i+=1

# "second while loop with break statement"
# i=0
# while i<10:
#     print(i)
#     if i==5:
#         break
#     i+=1


#with continue statement
i=0
while i<7:
    
    i+=1
    if i==4:
        continue
    print(i)
else:
    print("The loop has ended ")
