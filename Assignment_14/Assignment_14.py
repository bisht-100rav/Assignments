#Ques_1
def reverse(f,n):                                 #defining a function for reversing
    with open('para.txt',"r") as f:             #opening of the file using with
        print("last " ,n ," lines from file: ")
        for line in (f.readlines()[-n:]):         #use for loop in readlines() funciton while adding offset by taking each line using loop
            print(line,end='')
n=int(input("Enter the last line to read: "))
reverse("para.txt",n)                            #calling of the funciton


#Ques_2
from collections import Counter                    #Importing Counter() function
def fre(f):
    with open("para.txt","r") as f:
        return Counter(f.read().split())           #Using split function to split words inside file into seperable items in list
print(fre("para.txt"))


#Ques_3
with open("para.txt","r") as f:                     #transmit file is opened in read mode
    with open("Copy(Ques_3).txt","w") as copy:      #receiving file is opened in read mode
        for line in f:                              #for loop is used to iterate each line
            copy.write(line)


#Ques_4
lines1 = [ line.rstrip() for line in open("para.txt")]         #using function rstrip() in built line parameter
lines2 = [ line.rstrip() for line in open("f2(Ques_4).txt")]
for i in range((len(lines1))):
    print(lines1[i] + " ||| " + lines2[i])                     #combining two files using len() function on lines of files inside for loop


#Ques_5
with open("random.txt","w") as fw:
    i=0
    while i<10:
        fw.writelines(input("Enter any random number: "))
        fw.writelines("\n")
        i=i+1
with open("random.txt","r") as fr:
   lines_sort=fr.readlines()
   sort_num=[int(e.strip()) for e in lines_sort]
   sort_num.sort()
   print(sort_num)
   with open("Sorted(Ques_5.txt","w")as frs:
       for lines in fr:
           frs.write(lines)