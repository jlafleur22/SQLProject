import mysql.connector
import commands
import login

#database login for MySQL
db = mysql.connector.connect(
    host=login.host,
    user=login.user,
    passwd=login.passwd,
    database=login.database#uncomment after step 1
)

mycursor = db.cursor()



""" #Step 1 - Create Database
commands.createDB(mycursor)
#After Step 1, uncomment database = on line 10, then block comment all of Step 1 """



""" #Step 2 - Create First Table
commands.table1(mycursor)
#proof
commands.showTables(mycursor) """



""" #Step 3 - Fill Table
commands.insertTable1(mycursor)
db.commit()
#proof
commands.showTableContentStudents(mycursor) """



""" #Step4 - Create Second Table
commands.table2(mycursor)
#proof
commands.showTables(mycursor) """



""" #Step5 - Fill Second Table
commands.insertTable2(mycursor)
db.commit()
#proof
commands.showTableContentExamScores(mycursor) """



""" #Step6 - get average of a student
#to edit the student, change the value on commands page
commands.getStudentName(mycursor)
commands.getStudentScoresQuarterAvg(mycursor)
commands.getStudentScoresTotalAvg(mycursor) """



""" #Step7 - Add new student
commands.singleInsertTable1(mycursor, 'Wington', 'Georgie', 'O', '2032')
db.commit()
commands.showTableContentStudents(mycursor) """



""" #Step 8 - Add student scores
commands.singleInsertTable2(mycursor)
db.commit()
commands.showTableContentExamScores(mycursor) """



""" #Step9 -  Add column to a table (Student)
commands.table1ColumnAdd(mycursor)
db.commit()
commands.showTableHeaderStudents(mycursor) """



""" #Step10 - Delete Column added.
commands.table1ColumnDelete(mycursor)
db.commit()
commands.showTableHeaderStudents(mycursor) """



""" #Step11 - Perform Inner Join of the tables
commands.joinTables(mycursor)
 """

#Delete Database
#mycursor.execute("DROP DATABASE schoolDB")



#close the cursor and database
mycursor.close()
db.close()
