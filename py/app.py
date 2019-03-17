from flask import Flask,render_template,request
import psycopg2
from sklearn.externals import joblib
from pandas import read_csv

clf = joblib.load("file.sav")
data = read_csv("foo.csv")
app = Flask (__name__)

conn1 = psycopg2.connect(
    database = "testdb", 
    user = "postgres", 
    password = "postgres", 
    host = "127.0.0.1", 
    port = "5432"
)


cur1 = conn1.cursor()
cur1.execute("SELECT email,password from login")
rows = cur1.fetchall()
#routing
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/login/verify',methods = ['POST'])
def loginVerify():
    user_email = request.form['email']
    for row in rows:
        # print("email:",row[0])
        
        email = row[0].strip()
        # print(type(email))
        if user_email == email:
            # print("hello")
            return render_template('transaction.html')
        else :
            return '<html><body><h1>"Wrong user"</h1></body></html>'
    return render_template('transaction.html')
@app.route('/transaction',methods = ['POST'])
def transaction():
    date = request.form['date']
    conn2 = psycopg2.connect(
        database = "testdb", 
        user = "postgres", 
        password = "postgres", 
        host = "127.0.0.1", 
        port = "5432"
    )
    cur2 = conn2.cursor()
    cur2.execute("SELECT id, date, name, email, location, salary  from TRANSACTION where date = '"+date+"'")
    row = cur2.fetchall()
    conn2.close()
    X = data[data["date"] == date]
    X_test = X.iloc[:,1:31].values
    predicted = clf.predict(X_test)
    i = 0
    return render_template('transaction_detail.html', result = row, predicted = predicted)

conn1.close()

if __name__ == '__main__':
    app.run(debug=True)