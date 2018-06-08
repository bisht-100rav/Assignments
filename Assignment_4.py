#Ques_1
random=(1,3,6,"pizza","burger")     #creating tuple containing list , numeric and string
print(random)

#finding the len of the tuples
print(len(random))
print(len('pizza'))
print(len('burger'))

#Ques_2
#finding largest and smallest in tuples
#since random cannot be used as contains both string and int data types
t=(1,44,65,34,66,45,67,23,34)          #creating new tuples
print(min(t))
print(max(t))

#Ques_3
numbers=(1,2,3,4,5,6)            #multiplication of all elements in tuple can be achieved using loops
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply(numbers))

#######################################################################################################################
#SETS

#Ques_1
set1=set()
A=int(input('Enter first element: '))
B=int(input('Enter second element: '))
C=int(input('Enter third element: '))
set1=set((A,B,C))
print(set1)

set2=set()
X=int(input('Enter first element: '))
Y=int(input('Enter second element: '))
Z=int(input('Enter third element: '))
set2=set((X,Y,Z))
print(set2)

#Part1
set3=set1-set2
print(set3)

#Part2                    #comparing two sets
setx=set1 >= set2          #for this the one or the other set must be a subset of another to attain true value
sety=set1 <= set3
print(setx)
print(sety)

#Part3                     #this gives the common elements present inside the two sets
setz=set1&set2
print(setz)

#######################################################################################################################
#DICTIONARIES

#Ques_1
result={}

name1=(input('Write your name: '))
marks1=int(input('Writes your marks: '))

name2=(input('Write your name: '))
marks2=int(input('Writes your marks: '))

name3=(input('Write your name: '))
marks3=int(input('Writes your marks: '))

name4=(input('Write your name: '))
marks4=int(input('Writes your marks: '))

name5=(input('Write your name: '))
marks5=int(input('Writes your marks: '))

name6=(input('Write your name: '))
marks6=int(input('Writes your marks: '))

name7=(input('Write your name: '))
marks7=int(input('Writes your marks: '))

name8=(input('Write your name: '))
marks8=int(input('Writes your marks: '))

name9=(input('Write your name: '))
marks9=int(input('Writes your marks: '))

name10=(input('Write your name: '))
marks10=int(input('Writes your marks: '))

result={name1 : marks1,
        name2 : marks2,
        name3 : marks3,
        name4 : marks4,
        name5 : marks5,
        name6 : marks6,
        name7 : marks7,
        name8 : marks8,
        name9 : marks9,
        name10 : marks10}
print(result)



#Ques_2
from collections import OrderedDict                      #sorting of values can be done using OrderedDict() function
d_sorted_by_value = OrderedDict(sorted(result.items(), key=lambda x : x[1] ) )
print(d_sorted_by_value)


#Ques_1
import collections                                        #importing counter() function from collections
letter_count = collections.Counter("MISSISSIPPI")
print(letter_count)