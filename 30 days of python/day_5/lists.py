#Unpacking list item 
lst=['banana','peach','apple','mango','gauva']
first_item,second_item,third_item,*rest=lst
print(first_item,second_item,third_item, rest)

print(lst[-1])
print(lst[-4] )

#second example of unpacking lists
num_list=[1,2,3,4,5,6,7,8,9,10]
first,second,third,*rest,ninth,tenth=num_list
print(first,second,rest,ninth)

#slicing item from the lists

fruits=['banana','mango','apple','peach','strawberry','gauva']
print(fruits[0:4])
print(fruits[0:])
print(fruits[:])
print(fruits[::2])
print(fruits[2:5])

