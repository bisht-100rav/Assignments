#Ques_1
class Circle():                                 #Defining class Circle()
    def __init__(self,radius):                  #inititalising the attribute variable radius to class
        self.r=radius

    def Area(self):                             #defining method Area()
            return self.r**2*3.14
    def Circumference(self):                    #Defining method Circumference()
            return 2*3.14*self.r
shape=Circle(int(input("Enter the radius of circle: ")))           #Calling of the class inside shape variable_name
print(shape.Area())
print(shape.Circumference())



#Ques_2
class Student():
    def __init__(self,name,rollno):             #assigning variables to class Student()
        self.n=name
        self.r=int(rollno)
    def display(self):
        return print("Name: %s"%(self.n),"\nTotal Marks: %d/500"%(self.r))
Student_1=Student(input("Enter student\'s name: "),input("Enter student\'s total marks: "))
print(Student_1.display())


#Ques_3
class Temperature():
    def __init__(self,temperature):
        self.t=temperature
    def convert_celsius(self):
        return 1.8*self.t+32
    def convert_farhenheit(self):
        return (self.t-32)*5/9
convert=Temperature(int(input("Enter the required temperature for conversion: ")))
choice=int(input("Choose: \n(1) for C to F \n(2) for F to C \n"))
if choice==1:                                        #simple if loop for choosing between function celsius and farhenheit
    print(convert.convert_celsius())
elif choice==2:
    print(convert.convert_farhenheit())
else: print("Enter a valid option!!!!!")



#Ques_4
class Movie_Details():
    def __init__(self,movie_name,artist_name,year_of_release,ratings):      #assigning variables to class
        self.M_N=movie_name
        self.A_N=artist_name
        self.Y=year_of_release
        self.R=ratings
    def display(self):
        return print(self.M_N,self.A_N,self.Y,self.R)
    def Update(self, new_movie_name,new_artist_name,new_year_of_release,new_ratings):  #assigning new variables to existing class attributes
                                                                                       #using Update as functional parameter
        M_N=new_movie_name
        A_N=new_artist_name
        Y=new_year_of_release
        R=new_ratings
        return print("NEW MOVIE:",M_N,A_N,Y,R)

movie=Movie_Details("Avengers: Infinity War","\nAnthony Russo\nJoe Russo","\n2018","\n8.8 Imdb\n83% Rotten Tomatoes")
print(movie.display())
print(movie.Update("\nDeadPool2","\nDavid Leitch","\n2018","\n8.1 Imdb \n82% Rotten Tomatoes"))



#Ques_5
class Expenditure():
    def __init__(self,expenditure,savings):
         self.exp=expenditure
         self.s=savings
    def display(self):
         return print("Expenditure: ",self.exp,"\nSavings: ",self.s)
    def calculate(self):
        return (self.s+self.exp)
    def display_salary(self):
         return print(self.s+self.exp)
income=Expenditure(int(input("Enter monthly expenses: ")),int(input("Enter monthly savings: ")))
print(income.display())
print(income.display_salary())




















