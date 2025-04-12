print("Hello world!")  
print(len("Hello world!"))
print(type("Hello world!"))
print(int('10'))
print(str(10))
print(float(10))
#input("Enter your name:")  #input() takes the input from user



print(min(20,30,32,11))
print(max(12,52,35,44))
print(sum([11,22,33,44]))

#syntax is sum(iterable,start) where the default value of start is 0

from itertools import chain
nested_list=[[1,2,3],[2,4,6],[1,3,5]]
flat_sum=sum(chain(*nested_list),10)
print(flat_sum)


square_sum=sum((x**2 for x in range(1,5)),10)
print(square_sum)


#variable and its declaration 
first_name="Ishan"
last_name="Bartaula"
country="Nepal"
age=20
subject=["Microprocessor","data structure and algorthm","cloud computing"]
marks={"microprocessor":80,"DSA":99,"CC":95}
is_married=True
print("married:",is_married)

#variables can be declared in singl lines also
first_name,last_name,age,country,is_married,is_passed="ishan","bartaula",20,"nepal",True,False
print("First name:",first_name)
print("Last name:",last_name)
print("Age:",age)
print("country:",country)
print("Is married:",is_married)
print("Passed the exam:",is_passed)
print("Course subject:",subject)
print("Marks obtained:",marks)


#Using input() built-in functions
# contact=9898989823
# last_name=input("Enter your last name:")
# location=input("Your current location")
# Skill=input("What skill are you upgrading currently:")

# print("Hello Mr.",last_name,"current location is ",location,"and he has been working in ",Skill,"at the current time .SO if there any vacancy for the required skill do let us know .You can contact us at ",contact)


#Casting ,converting a data type into another
#int to float
num_int=10
print(float(num_int))
print(num_int)

#float to int
num_float=10.6
print(num_float)
print(int(num_float))

#str to int and float
num_str='10'
print(type(num_str))
print(int(num_str))
print(type(int(num_str)))
print(float(num_str))
print(type(float(num_str)))


name="Ishan Bartaula"
print(type(name))
name_str_to_list=list(name)
print(name_str_to_list)
print(type(name_str_to_list))