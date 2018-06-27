from tkinter import *
#Ques_1
root=Tk()                                                                        #Assigning object
root.title("Assignment_17")                                                      #Giving title
var=StringVar()                                                                  #Initialising a variable
label_1=Label(root,textvariable=var,fg="black",font="bold")     #Attaching label obj
var.set("Hello World")                                                           #Parameter for variable
label_1.pack()                                                                   #Packing of the label obj inside GUI

exit_button=Button(root,text="Click to Exit",command=root.destroy).pack()


#Ques_2
from tkinter import messagebox                   #Print button command using Dialog Box
def Message():
   messagebox.showinfo("Quote of the DAY","The most important thing is to enjoy your life—to be happy—it’s all that matters. —Audrey Hepburn")
print_text_button=Button(root,text="Print",command=Message).pack()

root.configure(bg="light grey")
root.geometry("200x100+100+150")
root.mainloop()


#Ques_3
window=Tk()
window.title("Ques_3")
frame=Frame(window,bg="light grey")
frame.pack()
var_t=StringVar()
label_3=Label(frame,textvariable=var_t).pack()
var_t.set("            Ques_3             ")

b_1=Button(frame,text="Exit",command=window.destroy).pack(side=BOTTOM)

def label_change():
    var_t.set("Ques_3 Completed!!")

b_2=Button(frame,text="Change Label",command=label_change).pack(side=TOP)

window.geometry("200x100+100+150")
window.mainloop()


#Ques_4
name= Tk()
Label(name, text="First Name").grid(row=0)
Label(name, text="Last Name").grid(row=1)

e1 = Entry(name)
e2 = Entry(name)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

from tkinter import messagebox                #Printing the Data entered using Dialog Box
def Printing_Name():
    messagebox.showinfo("User_info","First name:  %s \nLast name:  %s"%(e1.get(),e2.get()))

ExitButton=Button(name,text="Exit",command=name.destroy).grid(row=3,column=0)
PrintButton=Button(name,text="Print",command=Printing_Name).grid(row=3,column=1)

name.mainloop( )

