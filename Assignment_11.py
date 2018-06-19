
from threading import Thread                 #IMPORTING threading and time for all the questions above only!!!!!!
import time

#Ques_1
def wait():
    time.sleep(5)
    print("Thank You for your patience!!!")
myThread=Thread(wait())

#Ques_2
def number(i):
    time.sleep(1)
    print(i)
for i in range (1,11):
    th=Thread(number(i))

#Ques_3
not_a_DC_Fan=("Tell","Me","Do You Bleed?","You Will","Superman goes off flying.......")
def dialogue():                               #applying for loop for execution of sleep() and list
  j=1
  while j<=5:
      for i in not_a_DC_Fan:
          time.sleep(2*j)
          print(i)
          j=j+1
d_thread=Thread(dialogue())                    #calling of the thread


#Ques_4
from math import factorial                      #Fctorial funciton called from math inbuilt
def fact():
    for i in range(1,6):                        #applying for loop for assigning variable to factorial()
      print(i)
      print("Factorial: %d"%factorial(i))       #calling of the factorial function
      time.sleep(2)
f_thread=Thread(fact())                         #calling of the function using thread


