import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="raghavendra "
)
c=mydb.cursor()
c.execute("update employee set city='machilipatnam' where eid=254")
c.execute("update employee set city='hyderabad' where eid=264")
c.execute("update employee set city='chennai' where eid=274")
mydb.commit()