from flask import Flask, render_template, url_for, request, redirect, flash, session
from flask_mysqldb import MySQL
from flask_login import current_user
import json
from werkzeug.utils import secure_filename
import os
from flask import jsonify
import secrets
from datetime import timedelta

from flask_mail import Message
from flask_mail import Mail

def send_email(subject, body, recipients):
    message = Message(subject=subject, body=body, recipients=recipients)
    mail.send(message)

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'auth_db'

# configure email settings
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '141f0a4b49154c'
app.config['MAIL_PASSWORD'] = '86b4308a10a063'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'yqemrpfpnugvofk@bugfoo.com'

mail = Mail(app)

mysql = MySQL(app)
# check if connection is established
print(mysql.connection)

@app.route("/")
def home():
    
    return render_template("home.html")

# login.html
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get form data from request object
        username = request.form['username']
        fpassword = request.form['fpassword']
        question1 = request.form['question1']
        question1_answer = request.form['question1-answer-input']
        question2 = request.form['question2']
        question2_answer = request.form['question2-answer-input']
        question3 = request.form['question3']
        question3_answer = request.form['question3-answer-input']
        tpassword = request.form['tpassword']
        if username == "admin" and fpassword == "admin":
            return redirect(url_for("admin"))
        else:
            cur = mysql.connection.cursor()
            get_user = "SELECT * FROM users WHERE username = %s AND fpassword = %s AND question1 = %s AND question1_answer = %s AND question2 = %s AND question2_answer = %s AND question3 = %s AND question3_answer = %s AND picture_pass = %s"
            if cur.execute(get_user, [username, fpassword, question1, question1_answer, question2, question2_answer, question3, question3_answer, tpassword]):
                user = cur.fetchone()
                user_dict = {
                    'id': user[0],
                    'username': user[5],
                }
                session['loggedin'] = True
                session['id'] = user_dict['id']
                session['username'] = user_dict['username']
                flash(message="You have successfully logged in!", category="success")
                return redirect(url_for("home"))
            else:
                flash(message="Incorrect username or password", category="danger")
                return redirect(url_for("login"))
    return render_template("login.html")
# register.html
# Define route for handling user registration
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get form data from request object
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        dob = request.form['dob']
        username = request.form['username']
        fpassword = request.form['fpassword']
        question1 = request.form['question1']
        question1_answer = request.form['question1-answer-input']
        question2 = request.form['question2']
        question2_answer = request.form['question2-answer-input']
        question3 = request.form['question3']
        question3_answer = request.form['question3-answer-input']
        tpassword = request.form['tpassword']

        # Create cursor object to execute queries
        cursor = mysql.connection.cursor()

        # Execute INSERT query to add user to database
        insert_query = "INSERT INTO users (fullname, email, phone, dob, username, fpassword, question1, question1_answer, question2, question2_answer, question3, question3_answer, picture_pass) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        insert_values = (fullname, email, phone, dob, username, fpassword, question1, question1_answer, question2, question2_answer, question3, question3_answer, tpassword)
        cursor.execute(insert_query, insert_values)
        mysql.connection.commit()

        # Close cursor and database connection
        cursor.close()
        
        flash(message="User added successfully!", category="success")

    # Return success message to user
    return render_template("register.html")

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   session.pop('account_type', None)
   # Redirect to login page
   return redirect(url_for('login'))

@app.route('/submit_data', methods=['POST'])
def submit_data():
    date = request.form['date']
    bs_fast = request.form['bs_fast']
    breakfast_time = request.form['breakfast_time']
    breakfast_menu = request.form['breakfast_menu']
    lunch_time = request.form['lunch_time']
    lunch_menu = request.form['lunch_menu']
    dinner_time = request.form['dinner_time']
    dinner_menu = request.form['dinner_menu']
    bs_dinner = request.form['bs_dinner']
    user_ID = session['id']

    # connect to the database
    cur = mysql.connection.cursor()

    # insert the data into the database
    cur.execute("INSERT INTO diabetes (user_id, date, bs_fast, breakfast_time, breakfast_menu, lunch_time, lunch_menu, dinner_time, dinner_menu, bs_dinner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [user_ID, date, bs_fast, breakfast_time, breakfast_menu, lunch_time, lunch_menu, dinner_time, dinner_menu, bs_dinner])
    mysql.connection.commit()

    # close the connection
    cur.close()
    flash(message="Data has been saved!", category="success")
    return redirect(url_for('home'))

# profile
@app.route('/profile', methods=["GET", "POST"])
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE id = %s', [session['id']])
        user = cur.fetchone()
        if request.method == "POST":
            old_password = request.form['old_password']
            new_password = request.form['new_password']
            confirm_password = request.form['confirm_password']
            
            if new_password == confirm_password:
                if old_password == user[6]:
                    cur.execute("UPDATE users SET fpassword = %s WHERE id = %s", [new_password, session['id']])
                    mysql.connection.commit()
                    flash(message="Password changed successfully!", category="success")
                    return redirect(url_for('profile'))
                else:
                    flash(message="Old password is incorrect!", category="danger")
                    return redirect(url_for('profile'))
            else:
                flash(message="New password and confirm password do not match!", category="danger")
                return redirect(url_for('profile'))
        return render_template('profile.html', user=user)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# reset-password
@app.route('/reset-password', methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        # generate a random password and save it to the database
        email = request.form['email']
        new_password = secrets.token_hex(4) # generates a 8-character password using hex digits
        # save the new_password to the database reset_password table for the user with email 'email'
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO reset_password (email, temp_password) VALUES (%s, %s)", (email, new_password))
        mysql.connection.commit()
        cur.close()

        # send email to the provided email with how to reset
        subject = "Reset Your Password"
        body = f"Hello,\n\nYou have requested to reset your password. Your temporary password is {new_password}. Please follow the instructions provided in the email to reset your password.\n\nThank you.\n"
        send_email(subject, body, [email])

        # Return success message to user
        flash(message="A temporary password has been sent to your email.", category="success")
        return redirect(url_for('login'))

    return render_template("reset-password.html")

from flask import jsonify

# print
@app.route('/print', methods=["GET", "POST"])
def print():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM diabetes WHERE user_id = %s', [session['id']])
        rows = cur.fetchall()
        
        # Convert timedelta objects to their string representation
        def convert_timedelta(val):
            if isinstance(val, timedelta):
                return str(val)
            return val
        
        # Convert rows (tuple) to list of dictionaries
        data = [dict(zip([column[0] for column in cur.description], [convert_timedelta(value) for value in row])) for row in rows]
        
        return render_template('print.html', data=data)
        # return jsonify(data=data)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
