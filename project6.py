import shutil
columns = shutil.get_terminal_size().columns


	

def view_contact():
	print("\n\n")
	print("**********************".center(columns))
	print("   VIEW ALL CONTACT   ".center(columns))
	print("**********************".center(columns))
	print("\t\t\t\t\t\t\t\t=========================================")	
	mycursor.execute("SELECT * FROM phonebook")
	myresult = mycursor.fetchall()
	for x in myresult:
  		print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",x)

	print("\t\t\t\t\t\t\t\t=========================================")
	print("\n")	


def search_contact():
	print("\n\n")
	print("**********************".center(columns))
	print("    SEARCH CONTACT    ".center(columns))
	print("**********************".center(columns))
	s=input("ENTER THE NAME OF THE PERSON".center(columns))

	sql="SELECT * FROM phonebook WHERE NAME = %s", (s,)
	#val=(s)
	mycursor.execute(*sql)
	res=mycursor.fetchone()
	#for x in res:
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",res)
	#else:
		#print("NOT FOUND")



def add_contact():
	print("\n\n")
	print("**********************".center(columns))
	print("   ADD NEW CONTACT    ".center(columns))
	print("**********************".center(columns))
	newN=input("ENTER THE NAME".center(columns))
	sql="SELECT * FROM phonebook WHERE NAME = %s",(newN,)
	#val=(newN)
	mycursor.execute(*sql)
	res=mycursor.fetchone()
	if res:
		print("THIS NAME IS ALREADY EXISTING")
		add_contact()
	else:	
		newNO=int(input("ENTER THE PHONE NUMBER".center(columns)))
		sql="SELECT * FROM phonebook WHERE NUMBERS = %s", (newNO,)
		#val=(newNO)
		mycursor.execute(*sql)
		resu=mycursor.fetchone()
		if resu:
			print("THIS NUMBER IS ALREADY EXISTING".center(columns))
			add_contact()
		else:	
			sql="INSERT INTO phonebook (NAME,NUMBERS) VALUES (%s,%s)"
			val=(newN,newNO)
			mycursor.execute(sql,val)
			mydb.commit()

		
	
def delete_contact():
	print("\n\n")
	print("***********************".center(columns))
	print("   DELETE AN CONTACT   ".center(columns))
	print("***********************".center(columns))
	nameDEL=input("ENTER THE NAME OF THE CONTACT TO DELETE".center(columns))
	sql="SELECT * FROM phonebook WHERE NAME=%s", (nameDEL,)
	#val=(nameDEL)
	mycursor.execute(*sql)
	res=mycursor.fetchone()
	if res:
		sql="DELETE FROM phonebook WHERE NAME=%s", (nameDEL,)
		#val=(nameDEL)
		mycursor.execute(*sql)
		mydb.commit()
		print("contact deleted")
		

		
def update_contact():
	print("\n\n")
	print("***********************".center(columns))
	print("   UPDATE AN CONTACT   ".center(columns))
	print("***********************".center(columns))
	nameU=input("ENTER THE NAME OF THE CONTACT TO UPDATE".center(columns))
	print("Enter UPDATE criteria".center(columns))
	print("1: Name".center(columns))
	print("2: Number".center(columns))
	ch = int(input("Please enter: ".center(columns))) 
	if ch==1:
		sql="SELECT * FROM phonebook WHERE NAME=%s", (nameU,)
		#val=(nameU)
		mycursor.execute(*sql)
		res=mycursor.fetchall()
		if res:
			UPname=input("ENTER THE NEW NAME".center(columns))
			sql="SELECT * FROM phonebook WHERE NAME=%s", (UPname,)
			#val=(UPname)
			mycursor.execute(*sql)
			resu=mycursor.fetchall()
			if resu:
				print("THIS NAME IS ALREADY EXISTING IN THE CONTACT BOX".center(columns))
				update_contact()
			else:	
				sql="UPDATE phonebook SET NAME=%s WHERE NAME=%s"
				val=(UPname,nameU)
				mycursor.execute(sql,val)
				mydb.commit()
				print("CONTACT UPDATED".center(columns))
	elif ch==2:
		sql="SELECT * FROM phonebook WHERE NAME=%s", (nameU,)
		#val=(nameU)
		mycursor.execute(*sql)
		res=mycursor.fetchall()
		if res:
			UPnumb=int(input("ENTER THE NEW NUMBER".center(columns)))
			sql="SELECT * FROM phonebook WHERE NUMBERS=%s", (UPnumb,)
			#val=(UPnumb)
			mycursor.execute(*sql)
			resu=mycursor.fetchall()
			if resu:
				print("THIS NUMBER IS ALREADY EXISTING IN THE CONTACT BOX".center(columns))
				update_contact()
			else:
				sql="UPDATE phonebook SET NUMBERS=%s WHERE NAME=%s"
				val=(UPnumb,nameU)
				mycursor.execute(sql,val)
				mydb.commit()
				print("CONTACT UPDATED".center(columns))

						
		
def exit_contact():
	exit()




import shutil
columns = shutil.get_terminal_size().columns
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="class",
)
mycursor = mydb.cursor()

print("\n")
print("**********************".center(columns))
print("     CONTACT BOX      ".center(columns))
print("**********************".center(columns))
print("\n")


op='y'
while(op=='y'):
	print("\n")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t***************************")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t** 1 : VIEW CONTACT BOX  **")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t** 2 : SEARCH            **")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t** 3 : ADD NEW CONTACT   **")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t** 4 : DELETE AN CONTACT **")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t** 5 : UPDATE AN CONTACT **")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t** 6 : EXIT              **")
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t***************************")
	print("\n")

	try:
		n=int(input("ENTER YOUR OPTION :".center(columns)))


	except:
		print("PLEASE PROVIDE CORRECT INPUT".center(columns))	
		CONTINUE
	
	if n==1:
		view_contact()
	elif n==2:
		search_contact()
	elif n==3:
		add_contact()
	elif n==4:
		delete_contact()
	elif n==5:
		update_contact()
	elif n==6:
		exit_contact()
	else:
		print("INVALID OPTION ".center(columns))



	op=input("DO YOU WISH TO CONTINUE (y/n)".center(columns))	


