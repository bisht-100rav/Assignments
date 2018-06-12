#Ques_1
i=0
while i<10:

    a=int(input("Write any number: "))
    i=i+1
    print(a)


#Ques_2
while True:
    print("This is an infinite loop")


#Ques_3
num=int(input("Number of elements you want in list: "))
i=0
b=[]
square=[]
while i<num:
    a=int(input("Write an integer %d: "%(i+1)))
    b.append(a)
    square.append(a*a)
    i=i+1
print(b)
print(square)





#Ques_5
even=[]
odd=[]
for i in range(1,101):
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)



#Ques_6
n=4                            #can also user input desired value
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")                 #ending the line after each row


#Ques_7
i=0
n=int(input("Number of elements required in dictionary: "))
random={}
for i in range(1,n+1):
    keys=input("Enter the keys for %d element: "%(i))
    values=int(input("Enter the values for %d element: "%(i)))
    random[keys]=values
for j in random:
    print(j)





#Ques_8
list=[]
i=0
n=int(input("Enter number of elements you want in list: "))
while i<n:
    a=input("Enter element %d: "%(i+1))
    list.append(a)
    i=i+1
print(list)

search=input("Search from list (case-sensitive): ")
if search in list:
    list.remove(search)
    print("The searched entry was deleted from list")
    print(list)
else:
    print("Searched entry does not exist!!!")

