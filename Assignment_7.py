#Ques_1
def ar(a):
    return 3.14*a*a
a=int(input("Enter radius of circle: "))
print(ar(a))


#Ques_2
def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        print("True")
    else: print("False")
n=int(input("Enter any number: "))
perfect(n)


#Ques_3
def table(a,i=1):
    print("%d x %d = %d"%(a,i,a*i))
    if i!=11:
        table(a,i+1)
print(table(12))

#Ques_4
def power(a,b):
    if b==1:
        return a
    else:
        return a*power(a,b-1)
a=int(input("Enter any integer: "))
b=int(input("Enter required power: "))
print(power(a,b))


#Ques_5
def fact(x):
    if x==1:
        return 1
    else: return x*fact(x-1)
x=int(input("Enter any integer: "))
print(fact(x))
dict={"%d!"%(x):fact(x)}
print(dict)