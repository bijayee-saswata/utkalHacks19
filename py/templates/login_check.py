from flask import Flask, render_template, request
import psycopg2
conn = psycopg2.connect(
    database = "testdb", 
    user = "postgres", 
    password = "postgres", 
    host = "127.0.0.1", 
    port = "5432"
)
print("Opened database successfully")
cur = conn.cursor()

cur.execute("SELECT email,password from login")
rows = cur.fetchall()
app = Flask(__name__)

@app.route('/login/verify',methods = ['POST'])
def verify():
    user_email = request.form['em'].strip()
    user_pass = request.form['pass']
    
    print("user_email:",user_email)
    print(type(user_email))
    
    for row in rows:
        print("email:",row[0])
        
        email = row[0].strip()
        print(type(email))
        if user_email == email:
            print("hello")
            return render_template('transact.html')
        else :
            return '<html><body><h1>"Wrong user"</h1></body></html>'



conn.close()
if __name__ == '__main__':
   app.run(debug = True)