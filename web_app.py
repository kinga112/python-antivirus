from flask import Flask, render_template, request
import mysql.connector
from ebtables import ebtables

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/conf', methods=['POST', 'GET'])
def conf():
    if request.method == 'POST':
        dev_ip = request.form['ip']
        dev = request.form['devices']
        print('device ip: {}, device: {}'.format(dev_ip, dev))

    if request.method == 'Get':
        print("get")

    return render_template('conf.html')

def sql(dev_ip, dev):
    mycursor = mydb.cursor()

    sql = "INSERT INTO whitelist (dev_ip, dev) VALUES (%s, %s)"
    val = (dev_ip, dev)
    mycursor.execute(sql, val)
    mydb.commit()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
