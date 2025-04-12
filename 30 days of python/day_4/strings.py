# first_name="Ishan"
# last_name="Bartaula"
# space=" "
# print(len(first_name))
# full_name=first_name+space+last_name
# print(full_name)
# print(len(full_name))

# multiline_str='''I am a student of Bsc CSIT. I am from Pokhara
# .I am currently a student of Pokhara University .
# I am in my 4th semester of my course.'''
# print(multiline_str)
# print(len(multiline_str))


# #Escape sequence in python 

# print("I hope everbody is enjoying the holiday.\nAre you ?")
# print("Days \tExercise\tNumber of exercise")
# print("day1 \tChest\t\t4")
# print("day2 \tback\t\t5")
# print("day3 \tshoulder\t\t3")
# print("day4 \tlegs\t\t5")


# print("Every programming language strats with ,\"Hello world!\"")



# #String formatting in python .
# #Old way to format a string 

# first_name="Ishan"
# last_name="Bartaula"
# age=20
# height=5.6783

# formatted_string='My full name is %s %s and my age is %d whereas my height seems to be %.2f '%(first_name,last_name,age,height)
# print(formatted_string)

# #In new way we use .format method insted of module(%) to make it more clean and readable

# new_formatted_string='My full name is {} {} and my age is {} while my height seems to be around {:.2f}'.format(first_name,last_name,age,height)
# print(new_formatted_string)

# index_formatted_string='My age is {2} and My full name is {0} {1}'.format("Saayan","Sharma",20)
# print(index_formatted_string)

# named_formatted_string='My full name is {name} and I am of age {age}'.format(name="Ishan bartaula",age=20)
# print(named_formatted_string)


# #f-string ;most recommended and widely used 

# f_formatted_string=f'My full name is {first_name}{last_name} and I am of age {age} while my height seems to be around {height:.2f}'
# print("f-string:",f_formatted_string)

# num1=25
# num2=32
# f_string=f'{num1} + {num2} = {num1+num2}'
# print(f_string)

# string1="Chitwan"
# string2="Kathamandu"
# string3=" to "
# print(f'{string1}{string3}{string2}')


# #Python string as a sequence of characters

# language="javascript"
# print(language[0])
# print(language[1])
# print(language[2])
# print(language[len(language)-1])

# print(language[0:4])     #slicing string
# print(language[4:])
# print(language[-4:])
# print(language[-1])
# print(language[4:-4])

# #Reversing a string
# universe='Milkyway,Galaxy'
# print(universe[::-1])

# language="python"
# reverse_string=""
# for char in language:
#     reverse_string=char+reverse_string

# print(reverse_string)
# result=language[::2]
# print(result)

# #String methods
# phrase='a fifty shades of grey'
# print(phrase.capitalize())

# print(phrase.count('s'))
# print(phrase.count('of'))
# print(phrase.count('a',1,9))
# print(phrase[10])

# print(phrase.endswith("rey"))
# print(phrase.endswith('ion'))


# print(phrase.find('a'))
# print(phrase.find('of'))
# print(phrase.rfind("e"))
# print(phrase[20])
# print(phrase[15])


# web_tech=['javascript','HTML','python','SQL']
# result=' '.join(web_tech)
# print(result)

# first_string="Hello, I am a student of the CSIT in chitwan"
# stripped_string=(first_string.strip("dent"))
# print(stripped_string)



#Concatenate the string 'Thirty', 'Days', 'Of', 
# 'Python' to a single string, 'Thirty Days Of 
# Python'.
con_string=['Thirty','Days','Of','Python']
print('  '.join(con_string))


#Concatenate the string 'Coding', 'For' , 'All' to a 
# single string, 'Coding For All'.

main_string=['Coding','For','All']
print(' '.join(main_string))



#Declare a variable named company and assign it to 
# an initial value "Coding For All".

company='Coding For All'
#Print the variable company using print().
print(company)
#Print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize(),"\n",company.swapcase(),"\n",company.title())

#Cut(slice) out the first word of Coding For All string.
print(company[0:6])
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))
print(company.index("Coding"))

#Replace the word coding in the string 'Coding For All' to Python.
replaced_string=(company.replace("Coding","Python"))
print(replaced_string)

#Change Python for Everyone to Python for All using the replace method or other methods.
real_string="Python for Everyone"
print(real_string)
replaced_string=(real_string.replace("Everyone","All"))
print(replaced_string)

#Split the string 'Coding For All' using space as the separator (split()) .
main_string="Coding for All"
print(main_string)
splitted_string=(main_string.split(' '))
print(splitted_string)


#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

company="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
splitted_string=(company.split(","))
print(splitted_string)

#What is the character at index 0 in the string Coding For All.

print(main_string[0])

#What is the last index of the string Coding For All.
print(main_string.rindex('l'))

#What character is at index 10 in "Coding For All" string.
print(main_string[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
main_string="Python For Everyone"
splitted_string=(main_string.split(" "))
Abb_string=(splitted_string[0][0],splitted_string[1][0],splitted_string[2][0])
print("Acronym="," ".join(Abb_string)[0::2])


#Create an acronym or an abbreviation for the name 'Coding For All'.
main_string="Coding For All"
splitted_string=(main_string.split(" "))
Abb_string=(splitted_string[0][0],splitted_string[1][0],splitted_string[2][0])
print("Acronym="," ".join(Abb_string)[0::2])


#Use index to determine the position of the first occurrence of C in Coding For All.
main_string="Coding For All"
print(main_string.index("C"))

#Use index to determine the position of the first occurrence of F in Coding For All.
print(main_string.index("F"))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
main_string=("Coding For All People")
print(main_string.rindex("l"))

#Use index or find to find the position of the first 
# occurrence of the word 'because' in the following 
# sentence: 'You cannot end a sentence with because 
# because because is a conjunction'

main_sentence='You cannot end a sentence with because because because is a conjunction'
print(main_sentence.index("because"))
print(main_sentence.find("because"))

#Use rindex to find the position of the last
#  occurrence of the word because in the following 
# sentence: 'You cannot end a sentence with because 
# because because is a conjunction'

print(main_sentence.rindex("because"))
print(main_sentence.rfind("because"))

#Slice out the phrase 'because because because' in 
# the following sentence: 'You cannot end a sentence
#  with because because because is a conjunction'

print(main_sentence[main_sentence.index("because"):main_sentence.rindex("is")])

#Does ''Coding For All' start with a substring Coding?
main_string="Coding Fo All"
print(main_string.startswith("Coding"))

#Does 'Coding For All' end with a substring coding?
print(main_string.endswith("coding"))

#'   Coding For All      '  , remove the left and 
# right trailing spaces in the given string.

main_string="  Coding For All     "
print(main_string)
print(main_string.strip(" "))


#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python

first_string="30DaysOfPython"
second_string="thirty_days_of_python"
print(first_string.isidentifier())
print(second_string.isidentifier())


#The following list contains the names of some of
#  python libraries: ['Django', 'Flask', 'Bottle', 
# 'Pyramid', 'Falcon']. Join the list with a hash
#  with space string.

given_list=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("  #".join(given_list))


#Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.

main_string="I am enjoying this challenge.\nI just wonder what is next."
print(main_string)

#Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki

print("Name\t\t Age\t\tCountry\t\tCity")
print("Asabeneh\t250\t\tFinland\t\t\tHelsinki")


#Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.

radius=10
area=3.14*radius**2
print("The area of the circle with radius {} is {}".format(radius,area))


#Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144

print("{}+{}={}".format(8,6,(8+6)))
print("{}-{}={}".format(8,6,(8-6)))
print("{}*{}={}".format(8,6,(8*6)))
print("{}/{}={}".format(8,6,(8/6)))
print("{}%{}={}".format(8,6,(8%6)))
print("{}//{}={}".format(8,6,(8//6)))
print("{}**{}={}".format(8,6,(8**6)))