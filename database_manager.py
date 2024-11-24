import sqlite3 as sql


def listExtension():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension").fetchall()
    con.close()
    return data

def listStudents():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM students").fetchall()
    con.close()
    return data

def insertStudent(firstname, lastname, dob):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute("INSERT INTO students (firstname,lastname,dob) VALUES (?,?,?)", (firstname, lastname, dob))
    con.commit()
    con.close()
