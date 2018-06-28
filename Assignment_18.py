#Ques_1
def cmd():
    messagebox.showwarning("Eror 404","Not found!")

from tkinter import *

root=Tk()
root.title("Emergency Numbers")

options=Menu(root)
root.config(menu=options)
exit=Menu(options)
about=Menu(options)
tools=Menu(options)

options.add_cascade(label="File",menu=exit)
options.add_cascade(label="Options",menu=tools)
options.add_cascade(label='Help',menu=about)

exit.add_command(label='Exit',command=root.quit)
about.add_command(label="About",command=cmd)
tools.add_command(label="Tools",command=cmd)

name_L=Label(root,text="Helpline Name").grid(row=1,column=0)
number_L=Label(root,text="Number").grid(row=1,column=3)

list_number=Listbox()
list=Listbox()
scroll=Scrollbar()
scroll_1=Scrollbar()

scroll.grid(row=2,column=2)
scroll_1.grid(row=2,column=4)

scroll.configure(command=list.yview)
scroll_1.configure(command=list_number.yview)

list.configure(yscrollcommand=scroll.set)
list_number.configure(yscrollcommand=scroll_1.set)

list_number.grid(row=2,column=3)
list.grid(row=2,column=0)

list.insert(1,"Police")
list.insert(2,"Ambulance")
list.insert(3,"Fire")
list.insert(4,"Disaster Management")
list.insert(5,"Women\'s Helpline")
list.insert(6,"AIDS helpline")
list.insert(7,"Child Abuse Helpline")
list.insert(8,"Air Ambulance")
list.insert(9,"Anti Poison(New Delhi)")
list.insert(10,"RailWay Enquiry")
list.insert(11,"Road Accident Emergency")
list.insert(12,"Railway Accident Emergency")
list.insert(13,"Children in Difficult Situation")
list.insert(14,'LPG Leak Helpline')
list.insert(15,'Central Vigilance Commission')

list_number.insert(1,"100")
list_number.insert(2,"102")
list_number.insert(3,"101")
list_number.insert(4,"108")
list_number.insert(5,"181")
list_number.insert(6,"1097")
list_number.insert(7,"1098")
list_number.insert(8,"9540161344")
list_number.insert(9,"1066 or 011-1066")
list_number.insert(10,"139")
list_number.insert(11,"1073")
list_number.insert(12,"1072")
list_number.insert(13,"1098")
list_number.insert(14,"1906")
list_number.insert(15,1964)

#Ques_2
from tkinter import messagebox

def insert():
    var_1=StringVar()
    var_1=e1.get()
    list.insert(16,var_1)
    messagebox.showinfo("Notice","Key was inserted!")
def inser_value():
    var_2=StringVar()
    var_2=e2.get()
    list_number.insert(16,var_2)
    messagebox.showinfo("Notice","Value was inserted!")

e1=Entry(root)
e2=Entry(root)

e1.grid(row=3,column=0)
e2.grid(row=3,column=3)

insert_Button=Button(root,text="INSERT",command=insert)
insert_value_Button=Button(root,text="INSERT",command=inser_value)

insert_Button.grid(row=4,column=0)
insert_value_Button.grid(row=4,column=3)


root.mainloop()