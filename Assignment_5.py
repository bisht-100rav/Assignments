#Ques_1
year=int(input("Enter a year: "))
if year %4 ==0 and year %400 ==0:
    if year %100 != 0:
        print("Year is leap year ")
else :
   print("Year is not leap year ")


#Ques_2

len=int(input("Enter the length: "))
bre=int(input("Enter the breadth: "))
if len==bre:
    print ("The input dimensions are of square ")
else :
    print("The input dimensions are of rectangle ")




#Ques_3
a=int(input('Enter Ritu\'s age: '))
b=int(input('Enter Priya\'s age: '))
c=int(input('Enter Komal\'s age: '))

if a>b and a>c:
    print ("Oldest is Ritu")
    if b>c:
        print ("Youngest is Komal")
    else: print("Youngest is Priya")
elif b>a and b>c:
    print ("Oldest is Priya")
    if a>c:
        print ("Youngest is Komal")
    else: print ("Youngest is Ritu")
elif c>a and c>b:
    print ("Oldest is Komal")
    if a>b:
        print ("Youngest is Priya")
    else: print ("Youngest is Ritu")



 #Ques_4
points=int(input("Enter your total points: "))
if points>=1 and points<=50:
     print ("Sorry! No prize this time")
elif points>=51 and points<=150:
    print ('''Congratulations!!!!
    You\'ve won a WOODEN DOG''')
elif points>=151 and points<=180:
    print ('''Congratulations!!!!
    You\'ve won a BOOK ''')
elif points>=181 and points<=200:
    print ('''Congratulations!!!!
    You\'ve won CHOCOLATES''')
else: print("Enter valid amount of points!!!!!")



#Ques_5
quant=int(input("Enter number of units: "))
cost=quant*100
if (cost > 1000):
    disc=cost*10/100
    cost=cost-disc
    print ("Discounted price is Rs%d"%(cost))
else :
    print ("You are not applicabe for discount!!!!")
    print("cost = Rs%d" %(cost))


