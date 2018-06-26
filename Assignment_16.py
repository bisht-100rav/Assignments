import sqlite3


#Ques_1
book=sqlite3.connect("Books.db")
print("Data-base was opened successfully!!!!")
'''
book.execute("Create Table Books_1(BOOK_ID INT PRIMARY KEY NOT NULL,TITLE INT NOT NULL,LOCATION CHAR(50),GENRE TEXT)")
book.execute("Create Table Titles_1(TITLE_ID INT PRIMARY KEY NOT NULL,ISBN INT,PUBLISHER_ID INT,PUBLICATION_YEAR REAL)")
book.execute("Create Table Publisher(PUB_ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,ADDRESS CHAR(50))")
book.execute("Create Table Zip_1(ZIP_ID INT PRIMARY KEY NOT NULL,CITY TEXT,STATE TEXT,ZIP_CODE REAL)")
book.execute("Create Table AuthorsTitles_1(AUTHOR_ID INT PRIMARY KEY NOT NULL,AUTHOR_TITLE TEXT,AUTHOR_NAME TEXT)")
book.execute("Create Table Author(AUTH_ID INT PRIMARY KEY NOT NULL,FIRST_NAME TEXT,MIDDLE_NAME TEXT,LAST_NAME TEXT)")

'''
print("Tables were Created Successfully!!!!")


'''
#Ques_2
book.execute("INSERT INTO Books_1(BOOK_ID,TITLE,LOCATION,GENRE) VALUES(0,2,'Morgan Country','Horror')")
book.execute("INSERT INTO Titles_1(TITLE_ID,ISBN,PUBLISHER_ID,PUBLICATION_YEAR) VALUES(1,21256,89,1993)")
book.execute("INSERT INTO Publisher(PUB_ID,NAME,ADDRESS) VALUES(2,'Haunted House','United-Kingdom')")
book.execute("INSERT INTO Zip_1(ZIP_ID,CITY,STATE,ZIP_CODE) VALUES(3,'Pilottown','Plaquemines',70081)")
book.execute("INSERT INTO AuthorsTitles_1(AUTHOR_ID,AUTHOR_TITLE,AUTHOR_NAME) VALUES(4,'Goosebumps','R.L. Stine')")
book.execute("INSERT INTO Author(AUTH_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME) VALUES(5,'Jovial','Bob','Stine')")
book.commit()
'''


#Simple Loading bar for fun :)
print("The records are being Inserted, please Wait!!")
import time
def wait():
    print(".")
    time.sleep(0.35)
    print(".")
    time.sleep(0.45)
    print(".")
    time.sleep(0.55)
i=25
while i<=100:
    wait()
    print("%d"%i,"% done")
    time.sleep(1)
    i=i+25
print("\nData entry inside the Tables was successfully!!!!")


#Ques_3
A=book.execute("SELECT BOOK_ID,TITLE,LOCATION,GENRE FROM Books_1")
print("Values Before Updating!!!!==============================================================")
print("Records from Table_1 -------------------------------------------------------------------")
for row in A:
    print("Book_ID: ", row[0])
    print("Title: ",row[1])
    print("Location: ",row[2])
    print("Genre: ",row[3],"\n")

B=book.execute("SELECT TITLE_ID,ISBN,PUBLISHER_ID,PUBLICATION_YEAR FROM Titles_1")
print("Records from Table_2 -------------------------------------------------------------------")
for row in B:
    print("Title: ",row[0])
    print("Isbn: ",row[1])
    print("Publish ID: ",row[2])
    print("Publishing Year: ",row[3],"\n")

C=book.execute("SELECT PUB_ID,NAME,ADDRESS FROM Publisher")
print("Records from Table_3 -------------------------------------------------------------------")
for row in C:
    print("Publishing Id: ",row[0])
    print("Name: ",row[1])
    print("Address: ",row[2],"\n")

D=book.execute("SELECT ZIP_ID,CITY,STATE,ZIP_CODE FROM Zip_1")
print("Records from Table_4 -------------------------------------------------------------------")
for row in D:
    print("Zip ID: ",row[0])
    print("City: ",row[1])
    print("State: ",row[2])
    print("Zip Code: ",row[3],"\n")

E=book.execute("SELECT AUTHOR_ID,AUTHOR_TITLE,AUTHOR_NAME FROM AuthorsTitles_1")
print("Records from Table_5 -------------------------------------------------------------------")
for row in E:
    print("Author ID: ",row[0])
    print("Author Title: ",row[1])
    print("Author Name: ",row[2],"\n")

F=book.execute("SELECT AUTH_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME FROM Author ")
print("Records from Table_6 -------------------------------------------------------------------")
for row in F:
    print("Author id: ",row[0])
    print("First Name: ",row[1])
    print("Middle Name: ",row[2])
    print("Last Name: ",row[3],"\n")


#Updating the Values
book.execute("UPDATE Author set FIRST_NAME= 'Mr. Jovial' where AUTH_ID = 5")
book.execute("UPDATE AuthorsTitles_1 set AUTHOR_TITLE = 'Goosebumps(Horror)' where AUTHOR_ID = 4 ")
book.execute("UPDATE Zip_1 set ZIP_CODE = 70081.00 where ZIP_ID = 3")
book.execute("UPDATE Publisher set NAME = 'Haunted Car' where PUB_ID = 2")
book.execute("UPDATE Titles_1 set ISBN = 51249 where TITLE_ID = 1")
book.execute("UPDATE Books_1 set TITLE = 6 where BOOK_ID = 0")
book.commit()

#Simple Loading bar for fun :)
print("The records are being Updated, please Wait!!")
import time
def wait():
    print(".")
    time.sleep(0.35)
    print(".")
    time.sleep(0.45)
    print(".")
    time.sleep(0.55)
i=25
while i<=100:
    wait()
    print("%d"%i,"% done")
    time.sleep(2)
    i=i+25
print("Updating of the records was successful!!!!!!!\n")

print("Values After Updating ==================================================================")
A=book.execute("SELECT BOOK_ID,TITLE,LOCATION,GENRE FROM Books_1")
print("Records from Table_1 -------------------------------------------------------------------")
for row in A:
    print("Book_ID: ", row[0])
    print("Title: ",row[1])
    print("Location: ",row[2])
    print("Genre: ",row[3],"\n")

B=book.execute("SELECT TITLE_ID,ISBN,PUBLISHER_ID,PUBLICATION_YEAR FROM Titles_1")
print("Records from Table_2 -------------------------------------------------------------------")
for row in B:
    print("Title: ",row[0])
    print("Isbn: ",row[1])
    print("Publish ID: ",row[2])
    print("Publishing Year: ",row[3],"\n")

C=book.execute("SELECT PUB_ID,NAME,ADDRESS FROM Publisher")
print("Records from Table_3 -------------------------------------------------------------------")
for row in C:
    print("Publishing Id: ",row[0])
    print("Name: ",row[1])
    print("Address: ",row[2],"\n")

D=book.execute("SELECT ZIP_ID,CITY,STATE,ZIP_CODE FROM Zip_1")
print("Records from Table_4 -------------------------------------------------------------------")
for row in D:
    print("Zip ID: ",row[0])
    print("City: ",row[1])
    print("State: ",row[2])
    print("Zip Code: ",row[3],"\n")

E=book.execute("SELECT AUTHOR_ID,AUTHOR_TITLE,AUTHOR_NAME FROM AuthorsTitles_1")
print("Records from Table_5 -------------------------------------------------------------------")
for row in E:
    print("Author ID: ",row[0])
    print("Author Title: ",row[1])
    print("Author Name: ",row[2],"\n")

F=book.execute("SELECT AUTH_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME FROM Author ")
print("Records from Table_6 -------------------------------------------------------------------")
for row in F:
    print("Author id: ",row[0])
    print("First Name: ",row[1])
    print("Middle Name: ",row[2])
    print("Last Name: ",row[3],"\n")