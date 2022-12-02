import data
#import mysql

#Database Creation
def createDB(c):
    c.execute("CREATE DATABASE schoolDB")


#Table Creation
def table1(c):
    c.execute("CREATE TABLE Students (id int PRIMARY KEY AUTO_INCREMENT NOT NULL, last_name VARCHAR(50) NOT NULL, first_name VARCHAR(50) NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, graduation_year VARCHAR(4) NOT NULL)")

def table2(c):
    c.execute("CREATE TABLE ExamScores (userID int NOT NULL, quarter int NOT NULL, score int NOT NULL, examType ENUM('T', 'Q') NOT NULL)")

#to determine the column name, change the word after 'COLUMN' to refelect the desired column name, and then change the characteristics as neccessary
def table1ColumnAdd(c):
    c.execute("ALTER TABLE Students ADD COLUMN lunchbalance VARCHAR(6) NOT NULL")

def table2ColumnAdd(c):
    c.execute("ALTER TABLE ExamScores ADD COLUMN late ENUM('Y', 'N')")

#Change name after DROP to reflect the desired column to drop
def table1ColumnDelete(c):
    c.execute("ALTER TABLE Students DROP lunchbalance")

#Change name after DROP to reflect the desired column to drop
def table2ColumnDelete(c):
    c.execute("ALTER TABLE ExamScores DROP late")


#Table Fill
def insertTable1(c):
    c.executemany("INSERT INTO Students (last_name, first_name, gender, graduation_year) VALUES (%s, %s, %s, %s)", data.studentStart)

def insertTable2(c):
    c.executemany("INSERT INTO ExamScores (userId, quarter, score, examType) VALUES (%s, %s, %s, %s)", data.scoresStart)

def singleInsertTable1(c, str1:str, str2:str, str3:str, str4:str):
    c.execute("INSERT INTO Students (last_name, first_name, gender, graduation_year) VALUES (%s, %s, %s, %s)", (str1, str2, str3, str4))

def singleInsertTable2(c):
    c.executemany("INSERT INTO ExamScores (userId, quarter, score, examType) VALUES (%s, %s, %s, %s)", data.transferStudent)

#command can be used to select all (*) info from exam scores table and joining it to the students table using the id's and userId columns
#Table Join
def joinTables(c):
    c.execute("SELECT score, examtype, Students.id, Students.last_name FROM examscores INNER JOIN Students ON examscores.userId = Students.id")
    for x in c:
        print(x)

#Common check commands
def showTables(c):
    c.execute("SHOW TABLES")
    for x in c:
        print(x)

#change '*' to a specific column name to get information from only that column, or column_name1, column_name2 to get info from multiple but not all columns
def showTableContentStudents(c):
    c.execute("SELECT * FROM Students")
    for x in c:
        print(x)

def showTableContentExamScores(c):
    c.execute("SELECT * FROM ExamScores")
    for x in c:
        print(x)

def showTableHeaderStudents(c):
    c.execute("DESCRIBE Students")
    for x in c:
        print(x)

def showTableHeaderExamScores(c):
    c.execute("DESCRIBE ExamScores")
    for x in c:
        print(x)

#Average calculations, and student name retrieval
def averageTotal(q1q1: int, q1q2:int, q1t1:int, q2q1:int, q2q2:int, q2t1:int):
    return ((q1q1 + q1q2 + (q1t1*2) + q2q1 + q2q2 + (q2t1*2))/8)

def averageQuarter(q1:int, q2:int, t1:int):
    return((q1 + q2 + (t1*2))/4)

#to change student, change value of userID and id for both functions
def getStudentName(c):
    c.execute("SELECT first_name, last_name FROM Students WHERE id = 15")
    for x in c:
        print(x)

def getStudentScoresTotalAvg(c):
    c.execute("SELECT score FROM ExamScores WHERE userID = '15'")
    StudentScores = []
    for x in c:
    #iterating through provides the proper values, but I need to utilize them. 
        StudentScores.append(x)
    #print(StudentScores)#Debug check
    #looped for loop to put items into list without extra parenthesis and commas
    StudentScorseList = [item for t in StudentScores for item in t]
    #insert average values and compute average into formula
    #print(StudentScorseList)#DebugCheck
    stavg = averageTotal(int(StudentScorseList[0]), int(StudentScorseList[1]), int(StudentScorseList[2]), int(StudentScorseList[3]), int(StudentScorseList[4]), int(StudentScorseList[5]))
    print(stavg)
    
#the value of quarter will determing which quarter we are calculating    
def getStudentScoresQuarterAvg(c):
    c.execute("SELECT score FROM ExamScores WHERE userID = '15' && quarter = '2'")
    StudentScores = []
    for x in c:
    #iterating through provides the proper values, but I need to utilize them. 
        StudentScores.append(x)
    #print(StudentScores)#Debug check
    #looped for loop to put items into list without extra parenthesis and commas
    StudentScorseList = [item for t in StudentScores for item in t]
    #insert average values and compute average into formula
    #print(StudentScorseList)#DebugCheck
    stavg = averageQuarter(int(StudentScorseList[0]), int(StudentScorseList[1]), int(StudentScorseList[2]))
    print(stavg)

