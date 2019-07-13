import mysql.connector

import mysql.connector

class database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
	user = "root",
	passwd = "",
	host = "localhost",
	database = "project_database1",
    )

        self.cursor = self.mydb.cursor()



    def add_clerk(self,tup):
        self.cursor.execute("""INSERT INTO `clerk`(`name`, `gender`, `email`, `password`, `contact`, `address`)
                            VALUES (%s,%s,%s,%s,%s,%s)""",(tup))
        self.mydb.commit()


    def add_dept(self,tup):
        self.cursor.execute("""INSERT INTO `department`(`name`)
                             VALUES (%s)""",(tup))
        self.mydb.commit()


    def add_student(self,tup):
        getid=self.getdeptid(tup[9])
        tup[9]=getid[0]
        getid=self.getcourseid(tup[10])
        tup[10]=getid[0]
        self.cursor.execute("""INSERT INTO `student`(`name`, `gender`, `dob`, `email`, `contact`, `address`,
                `f_name`, `m_name`, `department_id`, `course_id`, `last_qualification`, `course`, `comments`,
                `clerk_id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(tup))
        self.mydb.commit()

    def getdeptid(self,dept_name):
        self.cursor.execute("SELECT * FROM `department` WHERE name=%s",(dept_name,))
        
        return (self.cursor.fetchone())

    def getcourseid(self,course_name):
        self.cursor.execute("SELECT * FROM `course` WHERE name=%s",(course_name,))
        return (self.cursor.fetchone())
        

    def add_course(self,tup):
    
        getid=self.getdeptid(tup[0])
        
        tup[0]=getid[0]
        self.cursor.execute("""INSERT INTO `course`(`department_id`,`name`)
                               VALUES (%s,%s)""",(tup))
        
        self.mydb.commit()
        


    def add_admin(self,tup):
        self.cursor.execute("""INSERT INTO `admin_login`(`email`, `password`)
                              VALUES (%s,%s) """,(tup))
        self.mydb.commit()




class Manage:
    
    def __init__(self):
        self.mydb=mysql.connector.connect(user="root",passwd="",host="localhost",
                                          database="project_database1")
        self.cursor=self.mydb.cursor()

    
        

    def view_s(self):
        x=self.cursor.execute("select * from `student`")
        return(self.cursor.fetchall())
        

    def view_a(self):
        x=self.cursor.execute("select * from `clerk`")
        return(self.cursor.fetchall())
        

    def view_c(self):
        x=self.cursor.execute("SELECT * FROM `admin`")
        return(self.cursor.fetchall())

    def view_d(self):
        x=self.cursor.execute("SELECT * FROM `department`")
        return(self.cursor.fetchall())

    def view_course(self):

        
        x=self.cursor.execute("SELECT * FROM `course` JOIN department on department.department_id=course.department_id")
        return(self.cursor.fetchall())

    def getclerkbyid(self,id_):
        x=self.cursor.execute("select * from `clerk` where clerk_id = %s",(id_,))
        return(self.cursor.fetchone())

    def updateclerk(self,tup):
        self.cursor.execute("""UPDATE `clerk` SET `name`=%s,
                            `gender`=%s,
                    `email`=%s,`password`=%s,`contact`=%s,`address`=%s WHERE `clerk_id`=%s """,tup)
        self.mydb.commit()




    def getcoursebyid(self,id_):
        x=self.cursor.execute("select * from `course` where course_id = %s",(id_,))
        return(self.cursor.fetchone())

    def updatecourse(self,tup):
        self.cursor.execute("""UPDATE `course` SET `department_id`=%s,`name`=%s WHERE `course_id`=%s """,tup)
        self.mydb.commit()


 
        



 


