#Ques_1
class Animal():                                  #Defining base-class "Animal()"
  def __init__(self,animal_attribute):           #Assigning parameter
      self.carnivorous=animal_attribute          #passing attribute
  def nature(self):                              #defining function inside base class
        return self.carnivorous

class Tiger(Animal):                             #creating sub-class "Tiger()"
    def __init__(self,animal_attribute):         #inititalising it with parameter
        super().__init__(animal_attribute)       #assigning it with base class using super function

animal1=Tiger("is Carnivorous")                  #creating object with refernce sub-class
print(animal1.nature())                          #calling of nature() function from Base-class using sub-class


#Ques_2
print("ans 1 :A , B")
print("ans 2: A , B")


#Ques_3
class Cop():
    def __init__(self,name,age,designation,experience):
        self.n=name
        self.a=age
        self.des=designation
        self.exp=experience
    def display(self):
        return print("Details of First Officer",self.n,self.a,self.des,self.exp)
    def add(self,new_name,new_age,new_designation,new_experience):
        self.n=new_name
        self.a=new_age
        self.des=new_designation
        self.exp=new_experience
    def update(self):
        return print("\n\nDeatails of Second Officer: ",self.n,self.a,self.des,self.exp)
class Mission(Cop):
    def __init__(self,name,age,designation,experience):
        super().__init__(name,age,designation,experience)
    def add_mission_details(self):
        return ("Officer is assigned for Patrol Duty")
officer=Mission("\nName:        Ramesh Babu","\nAge:         28","\nDesignation: Inspector","\nExperience:  7years")
print(officer.display())
print(officer.add_mission_details())
officer.add("\nName:        Suresh Babu","\nAge:         31","\nDesignation: Senior Inspector","\nExperience:  11years")
print(officer.update())
print(officer.add_mission_details())

#Ques_4
class Shape():                                             #Creating Base-class Shape()
    def __init__(self,length,breadth):                     #Assigning varibale_names
        self.len=length
        self.bre=breadth
    def Area(self):                                        #Area Function
        return print("Area is: ",self.len*self.bre)

class Rectangle(Shape):                                    #Subclass Rectangle()
    def __init__(self,length,breadth):                     #Assigning varibales to sub-class
        super().__init__(length,breadth)                   #linking varibales of subclass with base-class using super()

class Square(Shape):                                       #Sub-class Square()
    def __init__(self,side):                               #Assigning variables to sub-class
        super().__init__(side,side)                        #linking with Base-class
obj_1=Rectangle(int(input("Enter length of rectangle: ")),int(input("Enter breadth of rectangle: ")))
print(obj_1.Area())
obj_2=Square(int(input("Enter side of Square: ")))
print(obj_2.Area())