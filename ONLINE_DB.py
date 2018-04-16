import MySQLdb as mdb
#import sys
con = mdb.connect('sql12.freemysqlhosting.net' , 'sql12232725' , '8lqrdZ8ULu', 'sql12232725' , 3306);
cur = con.cursor()
#argList = sys.argv

#def create_table_Students():
#	cur.execute("DROP TABLE IF EXISTS Students")
#	cur.execute("CREATE TABLE Students(Roll_Number INT , Name varchar(25), Stream varchar(10), Sex varchar(1), Aggregate FLOAT, Backlogs INT)")
###################################################Students###################################################################
def insert_student(Roll_Number,Name,Stream,Sex,Aggregate,Backlogs):
	query = "INSERT INTO Students(Roll_Number,Name,Stream,Sex,Aggregate,Backlogs) " \
            "VALUES(%s,%s,%s,%s,%s,%s)"
    
   	args = (Roll_Number,Name,Stream,Sex,Aggregate,Backlogs)
   	cur.execute(query, args)
	con.commit()
	
def show_table_Students():
	cur.execute("SELECT * FROM Stdents")
	rows = cur.fetchall()
	for row in rows:
		print row


def delete_student(Roll_Number):
	query ="DELETE FROM Students WHERE Roll_Number = %s"
	cur.execute(query,(Roll_Number,))
	con.commit()
	
##########################################################Teachers#################################################################

def insert_Teachers(Name,Age,Qualifications,Dept,Post,Salary):
	query = "INSERT INTO Teachers(Name,Age,Qualifications,Dept,Post,Salary) " \
            "VALUES(%s,%s,%s,%s,%s,%s)"
    
   	args = (Name,Age,Qualifications,Dept,Post,Salary)
   	cur.execute(query, args)
	con.commit()

def show_table_Teachers():
	cur.execute("SELECT * FROM Teachers")
	rows = cur.fetchall()
	for row in rows:
		print row

def delete_teacher(Name):
	query ="DELETE FROM Teachers WHERE Name = %s"
	cur.execute(query,(Name,))
	con.commit()

######################################################Other Personnel####################################################################	


def insert_personnel(Name,Age,Position,Salary):
	query = "INSERT INTO Other_personnel(Name,Age,Position,Salary) " \
            "VALUES(%s,%s,%s,%s)"
    
   	args = (Name,Age,Position,Salary)
   	cur.execute(query, args)
	con.commit()

def show_table_personnel():
	cur.execute("SELECT * FROM Other_personnel")
	rows = cur.fetchall()
	for row in rows:
		print row

def delete_personnel(Name):
	query ="DELETE FROM Other_personnel WHERE Name = %s"
	cur.execute(query,(Name,))
	con.commit()

######################################################################################################################################
while(1):
	choice1 = raw_input("Which table do you want to edit, enter your choice:\n1).'1' for Teachers\n2).'2' for Students\n3).'3' for Other personnel\n")
	if choice1 == '1':
		choice2 = raw_input("Enter your choice:\n1).'1' for Inserting the record\n2).'2' for Showing the record\n3).'3' for deleting the record\n")
		if choice2 == '1':
			Name = raw_input("Enter the name of the teacher : ")
			Age = input("Enter the age of the teacher: ")
			Qualifications = raw_input("Enter the position of the teacher: ")
			Dept = raw_input("Enter the dept. in which the teacher is teaching: ")
			Post = raw_input("Enter the post of the teacher: ")
			Salary = input("Enter the salary: ")
			insert_Teachers(Name,Age,Qualifications,Dept,Post,Salary)
			print("________________________________________________________________________________________________________________________")
			break

		elif choice2 == '2':
			show_table_Teachers()
			print("________________________________________________________________________________________________________________________")
			break
		
		elif choice2 == '3':
			Name = raw_input("Enter the name of the teacher : ")
			delete_teacher(Name)
			print("________________________________________________________________________________________________________________________")
			break
	
	elif choice1 == '2':
		choice2 = raw_input("Enter your choice:\n1).'1' for Inserting the record\n2).'2' for Showing the record\n3).'3' for deleting the record\n")
		if choice2 == '2':
			show_table_Students()
			print("________________________________________________________________________________________________________________________")
			break

		elif choice2 == '1':
			Roll_Number = input("Enter the roll number: ")
			Name = raw_input("Enter the name: ")
			Stream = raw_input("Enter the stream: ")
			Sex = raw_input("Enter 'M' for male and 'F' for female: ")
			Aggregate = input("Enter the percentage: ")
			Backlogs = input("Enter the backlogs: ")
			insert_student(Roll_Number,Name,Stream,Sex,Aggregate,Backlogs)
			print("________________________________________________________________________________________________________________________")
			#show_table()
			break
		
		elif choice2 == '3':
			Roll_Number = input("Enter the roll number of the student which you want to remove: ")
			delete_student(Roll_Number)
			print("________________________________________________________________________________________________________________________")
			break
	
	elif choice1 == '3':
		choice2 = raw_input("Enter your choice:\n1).'1' for Inserting the record\n2).'2' for Showing the record\n3).'3' for deleting the record\n")
		if choice2 == '1':
			Name = raw_input("Enter the name of the personnel : ")
			Age = input("Enter the age of the personnel: ")
			Position = raw_input("Enter the post of the personnel: ")
			Salary = input("Enter the salary: ")
			insert_personnel(Name,Age,Position,Salary)
			print("________________________________________________________________________________________________________________________")
			break

		elif choice2 == '2':
			show_table_personnel()
			print("________________________________________________________________________________________________________________________")
			break
		
		elif choice2 == '3':
			Name = raw_input("Enter the name of the teacher : ")
			delete_personnel(Name)
			print("________________________________________________________________________________________________________________________")
			break
