# Ques_1
from typing import List
vegetables=["potato","tomato","ladyfinger","potato"]
print(vegetables)

#Ques_2
random_Question_2=["google","apple","facebook","microsoft","tesla"]
print(vegetables+random_Question_2)

#Ques_3
print(vegetables.count("potato"))
print(vegetables.count("tomato"))

#Ques_4
numbers=[2,6,8,4,5,1,3,9,7]
numbers.sort()
print(numbers)

#Ques_5
A=[1,3]
B=[2,4]
C=[] #Empty Array C
C=A+B
C.sort()
print(C)

#Ques_6
#Using stack
fruits=["banana","apple","mango"]
fruits.append("potato")            # pushing potato as LAST IN
print(fruits)
fruits.pop()                       # pull out potato as first out
print(fruits.pop())                # printing pulled out item of list
print(fruits)

#using Queues
from collections import deque                            #using deque() for fast appends and pops
games=deque(["Watchdogs","CounterStrike","GTA5"])
print(games)
games.append("DOTA2")
games.popleft()                                          #POP out as first in
print(games)