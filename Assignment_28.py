# 1. Create a table (student) with 3 columns (rollno, name, course).

create table student (rollno int, name text, course text, primary key(rollno));

# 2. Insert records for 4 students.

insert into student values(1,"Nishith Kumar","Python")
insert into student values(2,"Rahul Kumar","C")
insert into student values(3,"Raj Kumar","C++")
insert into student values(4,"Raman Kumar","Python")

# 3. Write a Select query to fetch all the students.

select * from student;

# 4. Update the student name of rollno 3 with ‘Mohan’

UPDATE student
SET rollno = 3
WHERE name = 'Mohan';

# 5. Delete any student from table with their rollno.

DELETE FROM table student
WHERE rollno==2
# 6. Delete all the data from student table.

TRUNCATE TABLE students;

# 7. Drop the student table.

drop table student;

# 8. Create Courses table (cid, cname) where cid is a primary key and Student table (rollno, name, cid) where rollno is a primary key and cid is a foreign key.

create table Courses (cid int, cname text,primary key(cid));
create table Student (rollno int, name text, cid int, primary key(rollno), foreign key(cid));

# 9. Insert data in both the tables.

insert into Courses values(121,"Python")
insert into Courses values(123,"C")
insert into Courses values(124,"C++")
insert into Courses values(121,"Python")

insert into Student values(1,"Nishith Kumar",121)
insert into Student values(2,"Rahul Kumar",123)
insert into Student values(3,"Raj Kumar",124)
insert into Student values(4,"Raman Kumar",121)


# 10. Select all the students who are doing a specific course, eg. Python.

select * from student where cousre="Python"
