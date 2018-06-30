import pandas as pd
#Ques_1
info=pd.read_csv("Assignment_20(Ques_1).csv")
data=pd.DataFrame(info)
print(data,"\n")


#Ques_2
Weather=pd.read_csv("Assignment_20(Ques_2).csv")
data_1=pd.DataFrame(Weather)

print("\nFirst 5 rows:\n",data_1.head(5))             #Prints first 5 rows of data_1
print("\nFirst 10 rows: \n",data_1.head(10))          #Prints first 10 rows of data_1

print("\nMean:\n:",data_1.mean())                     #Basic Stats
print("\nMedian: \n",data_1.median())
print("\nMode: \n",data_1.mode())

print("\nLast 5 rows: \n",data_1.tail(5))             #Prints last 5 rows

Column_3=data_1.loc[:,'MinTemp']                      #Column 3 of MinTemp was extracted instead
print(Column_3)
print("\nMean:\n",Column_3.mean())
print("\nMedian:\n",Column_3.median())
print("\nMode:\n",Column_3.mode())