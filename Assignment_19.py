import numpy as np

#Ques_1
a=np.random.random((10,1))    #Creating a random matrix of shape(10,1) using random()
print(a)
print(a.shape)                #Verifying shape
print(a.mean())               #passing mean function to 'a' array


#Ques_2
b=np.random.random((20,1))
print(b)
print(b.shape)
print("\nVariance of array 'b' is :",a.var())                #Passing in-built Variance function over b array
print("\nStandard Deviation of array 'b' is:",b.std(),"\n")  #Passing in-built Standard Deviation function over b array


#Ques_3
A=np.random.random((10,20))
B=np.random.random((20,25))
print("The Matrix multiplication of A and B:",np.matmul(A,B)) #Passing matmul dot scalar product funtion over A and B
print("\nThe shape of the new matrix:",np.matmul(A,B).shape)
C=np.matmul(A,B)                                              #storing matmul() matrix as obj in C
print("\nThe sum of the elements of new matix:",np.sum(C))    #Passing sum() over C


#Ques_4
from math import exp
A_1=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(A_1)
print(A_1.shape)

C_1=np.empty((0))            #Creating empty aray with empty() function
for i in np.nditer(A_1):     #get array method via nditer() function in-built numpy
 y=1+1+exp(i)
 print(i)                    #Checking if loop is catching values of array
 C_1=np.append(C_1,[[y]])
print(C_1)


