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
# i=0
# while i<7:
    
#     i+=1
#     if i==4:
#         continue
#     print(i)
# else:
#     print("The loop has ended ")


#multiplication table using for loop and break statement
# x=int(input("Enter the number for the multiplication: "))
# for i in range(1,18):
#     print(x,"*",i,"=",x*i)
#     if(i==10):
#         break


#multiplication table using for loop and continue statement
# x=int(input("Enter the number for the multiplication: "))
# for i in range(1,11):
#      if(i==8):
#         continue
#      print(x,"*",i,"=",x*i)

#multiplication table using while loop with continue statement
# x=int(input("enter a number for its multiplication: "))
# i=0
# while i<10:
#     i+=1
#     if i==5:
#         continue
   
#     print(x,"*",i,"=",x*i)
   


#Function in python

#hello function
# def hello():
#     print("Hello, Welcome to python function")

# hello()
    

#passing arguments in function
# def avg(a,b):
#     average=(a+b)/2
#     return average
# firstavg=avg(10,12)
# print(firstavg)

# def func(fname):
#     print(fname+" "+"Infosis")

# func("Ishan")
# func("Corporate")


#passing Arbitrary arguments
# def NumOne(*company):
#     print("Number one company is "+company[2])

# NumOne("Infosis","Nemera","Brighttech","Vpanda")


# def avg(*num):
#     sum=0
#     for i in num:
#         sum=sum+i
#     print("Average =", sum/len(num))

# avg(2,4,6,12)


# #passing keyword argument
# def fullname(fname,mname,lname):
#     print(fname+" "+mname+" "+lname)

# fullname(mname="Raj",lname="Bartaula",fname="Ishan")
#we can pass arguments as key=value pair so the position of the arguments doesnt matter that much


# #passing arbitrary keyword argument
# def fullname(**name):
#     print("His last name is "+name["lname"])

# fullname(fname="Ishan",lname="Bartaula",mname="Raj")


# #default parameter value
# def myCountry(country="Nepal"):
#     print("My present country is "+country)

# myCountry("Switzerland")
# myCountry()
# myCountry("Japan")


# def avg(a=10,b=20):
#     x=(a+b)/2
#     print("The average of ",a,"and",b,"is",x)

# avg()
# avg(2,4)
# avg(5)    
# avg(a=3)
# avg(b=11) 


# #passing list as an argument 
# def fruit(fruits):
#     for i in fruits:
#         print(i)

# name=["apple","gauva","grapes"]
# fruit(name)






#list in python
# car=["nemeraa","lambo","honda"]
# marks=[90,48,62,71]
# print(car)
# print(marks)
# print(len(car))
# print(len(marks))
# print(type(marks))

# fruits=list(("apple","mango","litchi","peach"))  #creating list using list constructor
# print(fruits)



#accessing the lists
# name=["Ishan","pabitra","rakshya","Aayan"]
# marks=[98,72,88,54,89]
# print(name[3])
# print(marks[3])
# print(name[1:3])
# print(marks[:3])
# print(marks[1:])
# if "rakshya" in name:
#     print ("yes")
# else:
#     print("No")

# if 70 in marks:
#     print("yes ,70 is in list marks")
# else:
#     print("No")


#change list items
# fruits=["apple","peach","grapes","litchi","mango"]
# print(fruits)
# fruits[2]="dragonfruit"
# print(fruits)

# # fruits[1:4]=["gauva","blackberry","srifa"]   #changing the range of list items
# # print(fruits)

# # fruits[1:2]=["gauva","blackberry","srifa"]   #if range of index is less an listed items is more ,it will change the range of items and other items will fall accordingly 
# # print(fruits)                                   

# fruits[1:4]=["gauva"]     #yedi range of index dherai xa ra change garna lako item thorai xa vaney , tyo range of index ma parni sabbai item lai hatayera naya item halxa ra bacheko item accordingly basxa
# print(fruits)


# fruits.insert(2,"papaya")
# print(fruits)




#Add list items
# fruits=["apple","peach","grapes","litchi","mango"]
# print(fruits)
# fruits.append("papaya")
# print(fruits)

# berry=["balckberry","blueberry","walnuts"]
# fruits.extend(berry)

# print (fruits)

# print(fruits.index("peach"))



#remove list items
# fruits=["apple","peach","grapes","litchi","mango"]
# print(fruits)

# # fruits.remove('grapes')
# # print (fruits)

# # fruits.pop(fruits.index("peach"))
# # print (fruits)

# # fruits.clear()
# # print(fruits)


# del fruits[3]
# print (fruits)




#tuples in python
# name=("Ishan","rakshya","pabitra","aayan","saaya")
# print(name)
# print(type(name))
# print(len(name))
# print(name[2])

# marks=tuple((98,44,53,67,87,33))
# print(marks)
# print(type(marks))
# print(marks[2:4])
# print(name[:3])
# print(marks[2:])


# if "pabitra" in name:
#     print("yes pabitra exist in this tuple")
# else:
#     print("No")

# if 45 in marks:
#     print("Yes 45 is present in this tuple")
# else:
#     print("No it doesnt exist")


#update tuple
# name=("Ishan","rakshya","pabitra","aayan","saaya")
# name1=list(name)
# # name1.remove("Ishan")
# # print(name1)

# # name1.append("Pratikshya")
# # print(name1)

# # name1.insert(2,"Smriti")
# # print(name1)

# name2=("Ankita","dikshya","Astika")
# name=name+name2
# print (name)




#f-strings in python
# name="Ishan bartaula"
# age=22
# clgname="CCT"
# university="Tribhuwan"
# letter=f"Hello everyone ,I am {name} .I am  {age} years old . I am currently studying  in {clgname} affilitated with {university}."

# print(letter.format(name,university,clgname,age))




#recursion in python
#function to calculate factorial of anumber using recursion
# def factorial(a):
#     if(a==0 or a==1):
#         return 1
#     else:
#         return a*factorial(a-1)
# print(factorial(5))


#fiboncci sequence using recursion
# def fibonacci(n):
    
#     if n<=1:
#        return n
        
#     else:
#      return(fibonacci(n-1)+fibonacci(n-2))

    
# num_terms=int(input("Enter the number of fibonacci you need :"))
# print(num_terms," fibonacci sequence are ")
# for i in range(num_terms):
#    print(fibonacci(i))




#Set in python

# num={1,2,"ishan",5,4,7,"bartaula",6,4,2}
# print(num)

# info=set()
# print(type(info))

# for i in num:
#     print(i)



#Uninon and update in set
# set1={2,4,6,8,10}
# set2={5,6,7,8,9,11}
# set3=set1.union(set2)
# print(set3)

# print(set1,set2)

# set1.update(set2)
# print(set1)



#intersection and intersection_update in set
# set1={2,4,6,8,10}
# set2={5,6,7,8,9,11}
# set3=set1.intersection(set2)
# print(set3)
# print(set1,set2)


# set1.intersection_update(set2)
# print(set1)


#symmetric difference  and symmetric difference update in set
# name1={"Nepal","Bhutan","India","Japan","Africa"}
# name2={"America","China","Japan","Korea","India"}
# name3=name1.symmetric_difference(name2)
# print(name3)

# print(name1,name2)

# name1.symmetric_difference_update(name2)
# print(name1)


#difference  and difference_update in set
# name1={"Nepal","Bhutan","India","Japan","Africa"}
# name2={"America","China","Japan","Korea","India"}
# name3=name1.difference(name2)
# print(name3)

# print(name1,name2)

# name1.difference_update(name2)
# print(name1)



#isdisjoint in set
# set1={2,4,6,8,10}
# set2={5,6,7,8,9,11}
# print(set1.isdisjoint(set2))

# set1={2,4,6,8,10}
# set2={1,3,5,7,9}
# print(set1.isdisjoint(set2))


#issuperset in set
# set1={1,2,3,4,5,6,7,8,9,10,11,12}
# set2={1,3,5,7,9}
# print(set1.issuperset(set2))


# set1={2,4,6,8,10}
# set2={5,6,7,8,9,11}
# print(set1.issuperset(set2))


#issubset in set
# set1={1,2,3,4,5,6,7,8,9,10,11,12}
# set2={1,3,5,7,9}
# print(set2.issubset(set1))


# set1={2,4,6,8,10}
# set2={5,6,7,8,9,11}
# print(set1.issubset(set2))


#add() in set
# set={1,3,5,7,9}
# set.add(10)
# print(set)

# set.add("ishan")
# print(set)


# set.remove(5)
# print(set)

# set.discard("ishan")  #discard use garera ste ma navako item romove garda pani error thrpw chai gardaina
# print(set)

# set.remove("ishan")
# print(set)        # remove use garera set ma navako ietem hatauda chai error throw garxa




#pop in set 
# set={1,3,5,7,9}
# set.add(10)
# print(set.pop())
# print(set)


# #del in set
# set={1,3,5,7,9}
# del set
# print(set)

#clear in set
# set={1,3,5,7,9}
# set.clear()
# print (set)


#check if exist in set
# set={1,3,5,7,9}
# if 3 in set:
#     print("3 is present in set")
# else:     
#     print("No its not present in set")



#Dictionary in python
# cars={"name":"Ford Mustang",
#       "model":"hellcat",
#       "year":1960,
#       "color":"Matt black",
#       "type":"disel",
#       "Electric":False
#     }
# print(cars)
# print(cars["year"])
# print(cars["model"])
# print(cars["color"])
# print(cars["name"])
# print(cars["Electric"])
#  print(len(cars))




# #Using dict() constructor to create dictionary

# student=dict(name="Ishan", age=22, course="CSIT",)
# print(student)



#Access items in dictionary

# employee={"name":"Ishan","batchno":2,"branch":"backend","age":22}
# employee=dict(name="Ishan",age=22,batchno=2,branch="backend")
# print(employee)

# print(employee["name"],employee["age"])
# x=employee.get("batchno")    #get will also return value as per key given
# print(x)

# key=employee.keys()    #will give you the keys name in the dictionary
# print(key)

# employee["status"]="Unmarried"  #after updating the keys will also update 
# print(key)



# value=employee.values()
# print(value)

# employee["status"]="Unmarried"   #will return the values of the dictionary in ordered form
# print(value)


# employee["batchno"]=126   #if the values is updated .values() will return the updated values
# print(value)


# item=employee.items()   #it will return key value pair in dictionary as tuples or list
# print(item)


#check if exist
# employee=dict(name="Ishan",age=22,batchno=2,branch="backend")
# print(employee)
# if "age" in employee:
#     print("Yes, age is one of the key ")
# else:
#     print("No the key you are looking for is not present the given dictionary")



#Exception handling in python

# a=input("Enter a number :")

# try :
#     for i in range(0,11):
#      print(f"{int(a)}x{i}={int(a)*i}")

# except:
#    print("Invalid syntax")



# try:
#     print("hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")    #it wont get executed if try throw an error
# finally:
#     print("Try except end")         #it will get executed whether try throw an error or not 


# i=11
# if (i<0 or i>10):
#     raise Exception("Number less then 0 and greater than 10 not allowed")



# def func():
#     try:
#         l=[1,3,5,7,9,11]
#         i=int(input("Enter the index of value required :"))
#         print(l[i])
#         return l[i]
#     except:
#         print("Some error occured")
#         return 1
#     finally:
#         return 0
# x=func()
# print(x)



 














