#!:usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
  host="hbtn_0e_0_usa",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
