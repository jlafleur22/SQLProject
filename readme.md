# Overview
I wanted to begin to learn how to create and manipulate a relational database using SQL. The Program I wrote uses Python to issue create two tables, store and manipulate data within them. This includes the ability to insert, modify, delete and query data. I will demonstrate the ability to utilize the information within the database to get student averages, and join the two tables together.

[Software Demo Video](https://youtu.be/OrrtYiTNb2g)

# Relational Database

I created a relational database of Students information and their associated test scores. The Primary table is the Student table, and it assigns a Unique Primary Key for each Student in incremental order by ones. The Second table stores the student test scores by the student ID. By joining the two tables based off of the student ID, I can pull information on a specific student and calculate the average for a quarter or the total time at the school if necssary.

Table 1 has 5 columns: ID, Last Name, First Name, Gender, Graduation Year. Table 2 also has 4 Columns: StudentID, Quarter, Score, Test, and Exam Type.

# Development Environment

I used MySQL for windows to create and store the database and tables for this project. I downloaded version 8.0.31, x86, 32-bit from [dev.mysql.com](https://dev.mysql.com/downloads/installer/). I used VSCode version 1.73, for my IDE obtained from [code.visualstudio.com](https://code.visualstudio.com/).

To run the database I used Python version 3.10.7 obtained from [https://www.python.org/downloads/](https://www.python.org/downloads/), accessed via the VSCode python extension version 2022.18.2 published by Microsoft, and pylance version 2022.11.40. The video is an effective tutorial for how to run the database for, but essentially you would do each step one at a time to build, populate and work within the database.

# Useful Websites


* [Geeks for Geeks](https://www.geeksforgeeks.org/python-programming-language/?ref=shm)
* [w3schools](https://www.w3schools.com/SQl/default.asp)
* [MySQLTutorial](https://www.mysqltutorial.org/)

# Future Work


* add third table to normalize data and increase uitility of information
* create method for comparing test scores between quarters
* add User Interface to make additions to info more accessible/useful