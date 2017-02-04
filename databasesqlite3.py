'''
Created on Feb 2, 2017

@author: kripa
'''
import sqlite3

con = sqlite3.connect("test.db")

#con.execute('''CREATE TABLE STUDENT
#        (ID INT PRIMARY_KEY NOT NULL,
#        NAME TEXT NOT NULL,
#        AGE INT NOT NULL,
#        FEES REAL);''')
#con.execute('INSERT INTO STUDENT (ID, NAME, AGE,FEES) VALUES (1,"rohan",20,4000.00)')
#con.execute('INSERT INTO STUDENT (ID, NAME, AGE,FEES) VALUES (2,"jemes",22,4000.00)')
#con.execute('INSERT INTO STUDENT (ID, NAME, AGE,FEES) VALUES (3,"ginu",20,4000.00)')
#con.execute('INSERT INTO STUDENT (ID, NAME, AGE,FEES) VALUES (4,"chandan",21,4000.00)')
#con.commit()
#print("records created ............")
obj = con.execute('SELECT ID, NAME, AGE, FEES FROM STUDENT')

for row in obj:
    print("ID is = "+str(row[0]))
    print("Name is = "+str(row[1]))
    print("age is = "+str(row[2]))
    print("fees is = "+str(row[3]))

con.execute('UPDATE STUDENT set FEES = 5000.00 WHERE ID=2')
con.commit()

obj = con.execute('SELECT ID, NAME, AGE, FEES FROM STUDENT')

for row in obj:
    print("ID is = "+str(row[0]))
    print("Name is = "+str(row[1]))
    print("age is = "+str(row[2]))
    print("fees is = "+str(row[3]))


con.execute('DELETE From STUDENT WHERE ID = 1;')    
con.commit()

obj = con.execute('SELECT ID, NAME, AGE, FEES FROM STUDENT')

for row in obj:
    print("ID is = "+str(row[0]))
    print("Name is = "+str(row[1]))
    print("age is = "+str(row[2]))
    print("fees is = "+str(row[3]))


