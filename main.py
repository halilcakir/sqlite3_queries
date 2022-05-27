import sqlite3

# connecting to the database
connection = sqlite3.connect("database.db")

# cursor
crsr = connection.cursor()
#### Write the SQL queries to display the total amount earned by each employee's name and surname.

#### Creating Table of Employee #############################################################################
crsr.execute("""CREATE TABLE IF NOT EXISTS Employee('Employee_ID','FirstName','Last_Name','City','State')""")
crsr.execute("INSERT INTO Employee VALUES(10330,'Jhon','Jhon','NY','NY')")
crsr.execute("INSERT INTO Employee VALUES(10449,'Sarah','Lebat','Melbourne','Bourke')")
crsr.execute("INSERT INTO Employee VALUES(11012,'Jon','Dallas','NY','NY')")
crsr.execute("INSERT INTO Employee VALUES(11013,'Georghe','Honey','NY','NY')")
crsr.execute("INSERT INTO Employee VALUES(11014,'Anton','Savar','NY','NY')")

##### Creating Table of Payments ############################################################
crsr.execute("""CREATE TABLE IF NOT EXISTS Payments (EmployeeId,SalaryDate,MonthId,Value)""")

##### Adding Values to the Table################################
crsr.execute("INSERT INTO Payments VALUES(10330,'June',6,128)")
crsr.execute("INSERT INTO Payments VALUES(10330,'June',7,158)")
crsr.execute("INSERT INTO Payments VALUES(10330,'August',8,133)")
crsr.execute("INSERT INTO Payments VALUES(10330,'September',9,120)")
crsr.execute("INSERT INTO Payments VALUES(10330,'October',10,188)")
crsr.execute("INSERT INTO Payments VALUES(10330,'November',11,160)")
crsr.execute("INSERT INTO Payments VALUES(10330,'December',12,105)")
crsr.execute("INSERT INTO Payments VALUES(10449,'September',9,150)")
crsr.execute("INSERT INTO Payments VALUES(10449,'October',10,158)")
crsr.execute("INSERT INTO Payments VALUES(10449,'November',11,160)")
crsr.execute("INSERT INTO Payments VALUES(10449,'December',12,180)")

####### Getting Values of Employee Id:10330
bring_10330 = """SELECT Value FROM Payments WHERE EmployeeId=10330 """
crsr.execute(bring_10330)
data_10330 = crsr.fetchall()

####### Getting Values of Employee Id:10449
bring_10449 = """SELECT Value FROM Payments WHERE EmployeeId=10449 """
crsr.execute(bring_10449)
data_10449 = crsr.fetchall()
connection.commit()


sum_10330 = 0
sum_10449 = 0

i = len(data_10330)-1
i2 = len(data_10449)-1

####### Sum of all Values for 10330 and 10449
for row in data_10330:
   sum_10330 = data_10330[i][0]+ sum_10330
   i=i-1

for row in data_10449:
    sum_10449 = data_10449[i][0] + sum_10449
    i2 = i2-1

###### Getting Employee Name From Table
name_10330 = crsr.execute("SELECT FirstName ,Last_Name FROM Employee WHERE Employee_ID=10330").fetchall()
name_10449 = crsr.execute("SELECT FirstName ,Last_Name FROM Employee WHERE Employee_ID=10449").fetchall()

###### Output
print(name_10449[0][0],name_10449[0][1],":",sum_10449,"\n",name_10330[0][0],name_10330[0][1],":",sum_10330)


#### Display all employees that have their names starting with the J letter
names_s_j = "SELECT * FROM Employee WHERE FirstName Like 'J%' "
crsr.execute(names_s_j)
connection.commit()
names_j =crsr.fetchall()
print(names_j)

connection.close()