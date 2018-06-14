#Ques_1
print('''Time tuple module provides various functions to manipulate time values.
 There are two standard representations of time.One is the number
of seconds since the Epoch, in UTC (a.k.a. GMT).It may be an integer
or a floating point number (to represent fractions of seconds).
The Epoch is system-defined; on Unix, it is generally January 1st, 1970.''')


#Ques_2
import time
print(time.asctime())             #printing the current date-time


#Ques_3
import _datetime
date=_datetime.date.today()        #passing value to date ,the cuurent time
print(date.month)                  #printing month form the current timeline


#Ques_4
print(date.day)                    #printing day from the current time line


#Ques_5
d='21-12-1999'                                    #Assigning a date format to d
d=_datetime.datetime.strptime(d,"%d-%m-%Y")       #calling of the d in striptime() in format given in d
print(d.day)


#Ques_6
import time                               #importing time function
print(time.localtime())                   #printing the local time
print(time.asctime(time.localtime()))     #printing the local time in asci format


#Ques_7
from math import factorial
n=int(input("Enter a number: "))
print(factorial(n))


#Ques_8
from math import gcd                     #gcd functoin determines the greatest common divisor of two integers
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
print(gcd(x,y))


#Ques_9
import os
print(os.getcwd())
print(os.environ)







