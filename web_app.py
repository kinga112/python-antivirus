from flask import Flask, render_template, request
import mysql.connector
from ebtables import ebtables

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/conf', methods=['POST', 'GET'])
def conf():
    if request.method == 'POST':
        dev_ip = request.form['ip']
        dev = request.form['devices']
        print('device ip: {}, device: {}'.format(dev_ip, dev))
        add_sql(dev_ip, dev)

    if request.method == 'Get':
        print("get")

    try:
        dev_ip_list, dev_list = get_sql()
    except:
        dev_ip_list = []
        dev_list = []
    
    return render_template('conf.html', len=len(dev_ip_list), dev_ip_list=dev_ip_list, dev_list=dev_list)

def add_sql(dev_ip, dev):

    mydb = mysql.connector.connect(
        host="localhost:3306",
        user="db",
        password="password",
        database='whitelist'
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO whitelist (device_ip, device) VALUES (%s, %s)"
    val = (dev_ip, dev)
    mycursor.execute(sql, val)
    mydb.commit()

def get_sql():
    cursor.execute("SELECT device_ip, device FROM whitelist")
    data = cursor.fetchall()
    dev_ip_list = []
    dev_list = []
    for row in data:
        dev_ip_list.append(row['device_ip'])
        dev_list.append(row['device'])
    return dev_ip_list, dev_list

if __name__ == '__main__':
    app.run(debug=True, port=5001)
