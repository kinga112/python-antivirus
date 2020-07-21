from flask import Flask, render_template, request, redirect
import mysql.connector
from ebtables import ebtables

app = Flask(__name__)

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="db",
        password="password",
        database="whitelist"
    )
except:
    print("cannot connect to MySQL Server")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/conf', methods=['POST', 'GET'])
def conf():
    if request.method == 'POST':
        dev_ip = request.form['ip']
        dev = request.form['devices']
        add_sql(dev_ip, dev)
    
    if request.method == 'Get':
        print("get")

    dev_ip_list, dev_list = get_sql()
    
    return render_template('conf.html', len=len(dev_ip_list), dev_ip_list=dev_ip_list, dev_list=dev_list)

@app.route('/conf/del/<id>', methods=['POST'])
def delete_conf(id):
    dev = id.split(',')[0]
    dev_ip = id.split(',')[1]
    del_sql(dev_ip, dev)
    return redirect('/conf')

def add_sql(dev_ip, dev):
    stat = ebtables(dev_ip, dev)
    mycursor = mydb.cursor(buffered=True)
    sql = "INSERT INTO whitelist (device_ip, device) VALUES (%s, %s)"
    val = (dev_ip, dev)
    mycursor.execute(sql, val)
    mydb.commit()

def get_sql():
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute("SELECT device_ip, device FROM whitelist")
    data = mycursor.fetchall()
    dev_ip_list = []
    dev_list = []

    for row in data:
        dev_ip_list.append(row[0])
        dev_list.append(row[1])

    return dev_ip_list, dev_list

def del_sql(dev_ip, dev):
    mycursor = mydb.cursor(buffered=True)
    # mycursor.execute("DELETE FROM whitelist WHERE device_ip in ('{}')".format(dev_ip))
    # mycursor.execute("DELETE FROM whitelist WHERE device = '{}'".format(dev))
    sql = """DELETE FROM whitelist where device_ip = %s"""
    mycursor.execute(sql, (dev_ip,))
    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
