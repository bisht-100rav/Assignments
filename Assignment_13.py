#Ques_1
print("The exception occurred in the program is named as ZeroDivisionError")
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("Value of 'a' becomes infinite!!!!")


#Ques_2
print("\nThe exception occurred in the program is named as IndexError")
try:
    l=[1,2,3]                    #Creating a list
    print(l[3])                  #Calling of the element in list using index
except IndexError:
    print("The following element does\'s exist in the list!!!!")


#Ques_3
print('''\nThe output of the program will print 
"An Exception"''')


#Ques_4
print('''\n1. -5
2. a/b result is 0''')


#Ques_5
try:
    import r
except ImportError:
    print("\nImported library does\'nt exixst!!!!")

try:
    a = int("Saurav")
    print(a)
except ValueError:
    print("\nValue of 'a' must be integer!!!!")

try:
    l = [1, 2]
    print(l[4])
except IndexError:
    print("\nThe following element does\'nt exist inside the list!!!!")


#Ques_5
class AgeTooSmallError(Exception):                #Creating Error for small age
    pass

result = None
while result is None:                             #Infinite loop untill the Exception gets resolved
  try:
    age=int(input("\nEnter your age: "))
    if age<18:
        raise AgeTooSmallError
  except AgeTooSmallError:
    print("\nAge must be less than 18!!!!")
    pass                                          #Until exceptions get resolved calling of the loop
  else:
      print(age)                                  #If there are no exceptions the loop will break
      break



