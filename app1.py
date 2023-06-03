#!/usr/bin/python3
import sqlite3
from flask import Flask, request, render_template, redirect, url_for, json, jsonify, send_from_directory
app = Flask(__name__)

conn = sqlite3.connect('database.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE students(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     rollno INTEGER,
#     email TEXT,
#     contact INTEGER,
#     branch TEXT,
#     address TEXT
# );''')


conn.commit()

conn.close()
# @app.route("/")
# def mainPage() -> str:
# 	return render_template("home.html")


@app.route('/')
def addPage():
    return render_template("home.html")


@app.route('/students.html')
def students():
    return render_template("students.html")

@app.route('/search1.html')
def search1():
    return render_template("search1.html")

@app.route('/faculties.html')
def faculties():
    return render_template("faculties.html")

@app.route('/search2.html')
def search2():
    return render_template("search2.html")

@app.route('/edit.html')
def edit():
    return render_template("edit.html")

@app.route('/edit2.html')
def edit2():
    return render_template("edit2.html")

@app.route('/home.html')
def home():
    return render_template("home.html")

@app.route("/students", methods=['POST'])
def addStudent() -> str:
    data = {"name": "", "email": "", "rollno": "",
            "contact": "", "program": ""}
    name = request.form.get("name")
    rollno = request.form.get("rollno")
    email = request.form.get("email")
    contact = request.form.get("contact")
    program = request.form.get("branch")

    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()

        query = f"SELECT rollno FROM students WHERE rollno = {rollno}"
        cursor.execute(query)
        data = cursor.fetchall()

        if len(data) != 0:
            return render_template("fail.html")
        else:
            cursor.execute("INSERT INTO students (name, rollno, email, contact, branch) VALUES (?, ?, ?, ?, ?)",
                           (name, rollno, email, contact, program))
            database.commit()

            return redirect(url_for("display"))



@app.route("/faculties", methods=['POST'])
def add_faculty() -> str:
    name = request.form.get("name")
    faculty_id = request.form.get("faculty_id")
    email = request.form.get("email")
    phone_number = request.form.get("phone_no")
    qualifications = request.form.get("qualifications")
    print(name)

    # Validate input
    # if not (name and faculty_id and email and phone_number and qualifications):
    #     return render_template("fail.html")

    with sqlite3.connect('database.db') as database:
        cursor1 = database.cursor()

        # Use parameterized query to avoid SQL injection
        query = f"SELECT faculty_id FROM faculties WHERE faculty_id = {faculty_id}"
        print(cursor1.execute(query))

        data = cursor1.fetchall()

        if len(data) != 0:
            return render_template("fail.html")
        else:
        # Use parameterized query to avoid SQL injection
            query = f"INSERT INTO faculties (name, faculty_id, email, phone_number, qualifications) VALUES (?, ?, ?, ?, ?)"
            cursor1.execute(query, (name, faculty_id, email,int(phone_number), qualifications))
            database.commit()

            return redirect(url_for("display1"))


@app.route('/display.html')
def display():
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        return render_template("display.html", students=students)


@app.route("/students/delete", methods=["POST"])
def deleteStudent():
    id = request.form.get("id")
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (id,))
        database.commit()
    return redirect(url_for("display"))


@app.route('/display1.html')
def display1():
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute("SELECT * FROM faculties")
        faculties = cursor.fetchall()

        return render_template("display1.html", faculties=faculties)


@app.route("/faculties/delete", methods=["POST"])
def deleteStudent1():
    id = request.form.get("id")
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute("DELETE FROM faculties WHERE id = ?", (id,))
        database.commit()
    return redirect(url_for("display1"))

@app.route('/search1', methods=[ 'POST'])
def search():
    
        name = request.form['name']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name=?", (name,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return render_template('search1.html', data=result)
        else:
            return render_template('search1.html')

@app.route('/search2', methods=[ 'POST'])
def search3():
    
        name = request.form['name']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM faculties WHERE name=?", (name,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return render_template('search2.html', data=result)
        else:
            return render_template('search2.html')
        
@app.route('/edit', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form.get('email', None)
        branch = request.form.get('branch', None)
        contact = request.form.get('contact', None)
        rollno = request.form.get('rollno', None)

        # Open database connection
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Update database
        if rollno:
            c.execute("UPDATE students SET rollno=? WHERE name=?", (rollno, name))
        if email:
            c.execute("UPDATE students SET email=? WHERE name=?", (email, name))
        if contact:
            c.execute("UPDATE students SET contact=? WHERE name=?", (contact, name))
        if branch:
            c.execute("UPDATE students SET branch=? WHERE name=?", (branch, name))

        # Commit changes and close connection
        conn.commit()
        conn.close()

        return redirect(url_for('edit'))

    else:
        return render_template('edit.html')

@app.route('/edit2', methods=['GET', 'POST'])
def update2():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form.get('email', None)
        qualifications = request.form.get('qualifications', None)
        phone_no = request.form.get('phone_no', None)
        faculty_id = request.form.get('faculty_id', None)

        # Open database connection
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Update database
        if faculty_id:
            c.execute("UPDATE faculties SET faculty_id=? WHERE name=?", (faculty_id, name))
        if email:
            c.execute("UPDATE faculties SET email=? WHERE name=?", (email, name))
        if phone_no:
            c.execute("UPDATE faculties SET phone_number=? WHERE name=?", (phone_no, name))
        if qualifications:
            c.execute("UPDATE faculties SET qualifications=? WHERE name=?", (qualifications, name))

        # Commit changes and close connection
        conn.commit()
        conn.close()

        return redirect(url_for('edit2'))

    else:
        return render_template('edit2.html')
    
if __name__ == "__main__":
    app.run(debug=True, port=5500)