import mysql.connector
from db import get_connection

con = get_connection()
cur = con.cursor()

print("✅ Database Connected Successfully")
def add_student():
    name = input("Name: ")
    roll = input("Roll No: ")
    marks = int(input("Marks: "))

    percent = (marks / 500) * 100
    result = "Pass" if percent >= 35 else "Fail"

    sql = "INSERT INTO students (name, roll_no, marks, percentage, result) VALUES (%s,%s,%s,%s,%s)"
    val = (name, roll, marks, percent, result)

    cur.execute(sql, val)
    con.commit()
    print("✅ Student Added Successfully")
def view_students():
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()

    for row in data:
        print(row)
def view_students():
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()

    for row in data:
        print(row)
def update_student():
    sid = input("Enter Student ID to Update: ")
    marks = int(input("New Marks: "))

    percent = (marks / 500) * 100
    result = "Pass" if percent >= 35 else "Fail"

    sql = "UPDATE students SET marks=%s, percentage=%s, result=%s WHERE id=%s"
    val = (marks, percent, result, sid)

    cur.execute(sql, val)
    con.commit()
    print("✏️ Student Updated")
def delete_student():
    sid = input("Enter Student ID to Delete: ")
    cur.execute("DELETE FROM students WHERE id=%s", (sid,))
    con.commit()
    print("🗑️ Student Deleted")
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("❌ Invalid Choice")

