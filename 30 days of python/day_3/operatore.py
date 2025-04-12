# print("Cash is cash","cash" is "cash")
# print("I is in Asia","i" in "Asia" )
# print("5 is in the list", 5 in [2,3,4,6])
# print("5 is not in the list", 5 not in [2,3,4,6])

# age=20
# height=5.6
# complex_num=3+2j

#Write a script that prompts the user to enter base 
# and height of the triangle and calculate an area of
#  this triangle (area = 0.5 x b x h).

# base=input("Enter the base of the triangle:")
# height=input("Enter the height of the triangle:")
# area=(1/2)*float(base)*float(height)
# print("Area of the triangle is :",area)


#Write a script that prompts the user to enter side 
# a, side b, and side c of the triangle. Calculate 
# the perimeter of the triangle (perimeter = a + b + c).

# a=input("Enter the side a:")
# b=input("Enter the side b:")
# c=input("Enter the side c:")
# perimeter=int(a)+int(b)+int(c)
# print("The perimeter of the triangle is :",perimeter)


#Get length and width of a rectangle using prompt.
#Calculate its area (area = length x width) and 
# perimeter (perimeter = 2 x (length + width))

# length=input("Enter the legh of the rectangle:")
# width=input("Enter the width of the rectangle:")
# area=int(length)*int(width)
# perimeter=(2*(int(length)+int(width)))
# print("The area of the rectangle is :",area)
# print("The perimeter of the rectangle is ",perimeter)



#Get radius of a circle using prompt. Calculate the 
# area (area = pi x r x r) and circumference 
# (c = 2 x pi x r) where pi = 3.14.

# pi=3.14
# radius=input("Enter the radius of the circle")
# area=(pi*(float(radius)**2))
# circum=(float(2)*pi*float(radius))
# print("Area of the circle is :",area)
# print("Circumference of the circle is :",circum)



#Calculate the slope, x-intercept and y-intercept of 
# y = 2x -2

#Find the length of 'python' and 'dragon' and make a 
# falsy comparison statement.

# len_py=len("python")
# len_dra=len("dragon")
# print("Length of python:",len_py)
# print("Length of dragon:",len_dra)
# print(len_py != len_dra)


#Use and operator to check if 'on' is found in both 
# 'python' and 'dragon'

print(("on" in 'python') and ("on" in "dragon"))



#I hope this course is not full of jargon. Use in 
# operator to check if jargon is in the sentence.

print("jargon" in "I hope this course is not full of jargon")



#Find the length of the text python and convert the
#  value to float and convert it to string

len_py=len("python")
print("Length of python ",len_py)
float_len_py=float(len_py)
str_float_len_py=str(float_len_py)
print(float_len_py)
print(str_float_len_py)


#Even numbers are divisible by 2 and the remainder is
#  zero. How do you check if a number is even or not
#  using python?


# num=input("Enter a number to be checked: ")
# flag=((int(num)%2)==0)
# print("Flag=",flag)
# print("If flag=True the numbre is even otherwise not")




#Check if the floor division of 7 by 3 is equal to 
# the int converted value of 2.7.

flr_div=7//3
int_value=int(2.7)
print("7//3 is equal to int(2.7)",flr_div==int_value)



#Check if type of '10' is equal to type of 10

print("Type of '10' is equal to Type of 10",type("10")==type(10))


#Check if int('9.8') is equal to 10

print("int(9.8) is equal to 10",int(9.8)==10)

#Write a Python script that displays the following 
# table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125


print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")