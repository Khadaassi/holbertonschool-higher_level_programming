<p align="center">
    <img [SQL - Introduction] src="https://sqldbaschool.com/wp-content/uploads/2015/06/shutterstock_sql.jpg">
</p>

----------

# <p align="center">SQL - Introduction</p>

----------

## ➤ Menu:

* [➤ Description](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/SQL_introduction#-description)
* [➤ Resources](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/SQL_introduction#-resources)
* [➤ General](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/SQL_introduction#-general)
* [➤ Requirements](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/SQL_introduction#-requirements)
* [➤ Tasks](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/SQL_introduction#0-list-databases)
* [➤ Author](https://github.com/khadaassi/holbertonschool-higher_level_programming/tree/main/SQL_introduction#-author)

----------

## ➤ Description:

SQL (Structured Query Language) is a programming language used to communicate with relational databases. It enables data stored in these databases to be manipulated and managed in an efficient, structured way. Here are a few key points to remember about SQL:

1. **Structured query language:** SQL is a structured query language that uses clear and precise syntax to interact with databases.

2. **Data manipulation:** SQL allows you to perform various operations on data, such as inserting, modifying, deleting and retrieving data.

3. **Database creation and management:** SQL lets you create and manage databases, as well as create tables, indexes and other data structures.

4. **Declarative language:** SQL is a declarative language, which means that SQL queries describe the desired result, but do not specify how this result is to be obtained. This allows the database management system (DBMS) to choose the most efficient execution method.

5. **Compatibility with various DBMS:** SQL is a standard language supported by most relational database management systems (RDBMS), such as MySQL, PostgreSQL, SQLite, Oracle, Microsoft SQL Server, etc.

6. **Use of multiple clauses and commands:** SQL offers a variety of clauses and commands for performing complex operations on data, such as SELECT, INSERT, UPDATE, DELETE, JOIN, WHERE, GROUP BY, HAVING, ORDER BY, etc.

In short, SQL is an essential tool for interacting with relational databases, whether for managing data, creating database structures or executing complex queries to analyze data.

----------

## ➤ Resources:

Read or watch:

* [What is Database & SQL?](https://intranet.hbtn.io/rltoken/jRAhwW4u4YvZtLtMGU2_6g)
* [Install MySQL (MySQL Server)](https://intranet.hbtn.io/rltoken/s3m_emsaSthyY041Wacgxg)
* [A Basic MySQL Tutorial](https://intranet.hbtn.io/rltoken/m_0RMf4RcC5NrHyjY1xN3w)
* [Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)](https://intranet.hbtn.io/rltoken/-Qrnbp5eKmo7ajPDZekjfg)
* [Basic queries: SQL and RA](https://intranet.hbtn.io/rltoken/wXN5s1qexSTMh--NkTF1_w)
* [SQL technique: functions](https://intranet.hbtn.io/rltoken/7khGjnehvjHnqNZ9yizggg)
* [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/xnJcopQTZyUke3LdAkOwow)
* [What makes the big difference between a backtick and an apostrophe?](https://intranet.hbtn.io/rltoken/QEr3XcBPhIR-E8NSSn1nzg)
* [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/DGejihlnOkkNq-qJFM15MA)
* [MySQL 8.0 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/ePNUeloWxfiXwec7HeKe7Q)

----------

## ➤ General:

* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

----------

## ➤ Requirements:

General

* Allowed editors: vi, vim, emacs
* All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (SELECT, WHERE…)
* A README.md file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using wc

## ➤ More Info:

**Comments for your SQL file:**

```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

**Install MySQL 8.0 on Ubuntu 20.04 LTS

```sql
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

**Connect to your MySQL server:**

```sql
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

**Use the sandbox to run MySQL**
In the container, credentials are root/root

* Ask for container Ubuntu 20.04
* Connect via SSH
* OR connect via the Web terminal
* In the container, you should start MySQL before playing with it:

```sql
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```

In the container, credentials are root/root


----------

<details>
<summary>Tasks:</summary>

### 0. List databases

Write a script that lists all databases of your MySQL server.

```sql
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 0-list_databases.sql
 
### 1. Create a database

Write a script that creates the database hbtn_0c_0 in your MySQL server.

* If the database hbtn_0c_0 already exists, your script should not fail
* You are not allowed to use the SELECT or SHOW statements

```sql
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$
``` 

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 1-create_database_if_missing.sql
 
### 2. Delete a database

Write a script that deletes the database hbtn_0c_0 in your MySQL server.

* If the database hbtn_0c_0 doesn’t exist, your script should not fail
* You are not allowed to use the SELECT or SHOW statements

```sql
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                                                                                                  
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 2-remove_database.sql
 
### 3. List tables

Write a script that lists all the tables of a database in your MySQL server.

* The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

```sql
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql                                                                              
columns_priv                                                                                 
component                                                                                    
db                                                                                           
default_roles                                                                                
engine_cost                                                                                  
func                                                                                         
general_log                                                                                  
global_grants                                                                                
gtid_executed                                                                                
help_category                                                                                
help_keyword                                                                                 
help_relation                                                                                
help_topic                                                                                   
innodb_index_stats                                                                           
innodb_table_stats                                                                           
password_history                                                                             
plugin                                                                                       
procs_priv                                                                                   
proxies_priv                                                                                 
replication_asynchronous_connection_failover                                                 
replication_asynchronous_connection_failover_managed                                         
role_edges                                                                                   
server_cost                                                                                  
servers                                                                                      
slave_master_info                                                                            
slave_relay_log_info                                                                         
slave_worker_info                                                                            
slow_log                                                                                     
tables_priv                                                                                  
time_zone                                                                                    
time_zone_leap_second                                                                        
time_zone_name                                                                               
time_zone_transition                                                                         
time_zone_transition_type                                                                    
user
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 3-list_tables.sql
 
### 4. First table

Write a script that creates a table called first_table in the current database in your MySQL server.

* first_table description:
 * id INT
 * name VARCHAR(256)
* The database name will be passed as an argument of the mysql command
* If the table first_table already exists, your script should not fail
* You are not allowed to use the SELECT or SHOW statements

```sql
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 4-first_table.sql
 
### 5. Full description

Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.

* The database name will be passed as an argument of the mysql command
* You are not allowed to use the DESCRIBE or EXPLAIN statements

```sql
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci        
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 5-full_table.sql
 
### 6. List all in table

Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

* All fields should be printed
* The database name will be passed as an argument of the mysql command

```sql
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 6-list_values.sql
 
### 7. First add

Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

* New row:
 * id = 89
 * name = Best School
* The database name will be passed as an argument of the mysql command

```sql
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
89  Best School
89  Best School
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 7-insert_value.sql

### 8. Count 89

Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

* The database name will be passed as an argument of the mysql command

```sql
guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 8-count_89.sql
 
### 9. Full creation

Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

* second_table description:
 * id INT
 * name VARCHAR(256)
 * score INT

* The database name will be passed as an argument to the mysql command
* If the table second_table already exists, your script should not fail
* You are not allowed to use the SELECT and SHOW statements
* Your script should create these records:
 * id = 1, name = “John”, score = 10
 * id = 2, name = “Alex”, score = 3
 * id = 3, name = “Bob”, score = 14
 * id = 4, name = “George”, score = 8

```sql
guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 9-full_creation.sql
 
### 10. List by best

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the mysql command

```sql
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 10-top_score.sql
 
### 11. Select the best

Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the mysql command

```sql
guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 11-best_score.sql
 
### 12. Cheating is bad

Write a script that updates the score of Bob to 10 in the table second_table.

* You are not allowed to use Bob’s id value, only the name field
* The database name will be passed as an argument of the mysql command

```sql
guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 12-no_cheating.sql
 
### 13. Score too low

Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

* The database name will be passed as an argument of the mysql command

```sql
guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 13-change_class.sql
 
### 14. Average

Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

* The result column name should be average
* The database name will be passed as an argument of the mysql command

```sql
guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 14-average.sql
 
### 15. Number by score

Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

* The result should display:
 * the score
 * the number of records for this score with the label number
* The list should be sorted by the number of records (descending)
* The database name will be passed as an argument to the mysql command

```sql
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 15-groups.sql
 
### 16. Say my name

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

* Don’t list rows without a name value
* Results should display the score and the name (in this order)
* Records should be listed by descending score
* The database name will be passed as an argument to the mysql command

In this example, new data have been added to the table second_table.

```sql
guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$
```

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: SQL_introduction
* File: 16-no_link.sql


</details>

----------

## ➤ Author:

- Khadija AASSI