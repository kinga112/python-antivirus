from flask import Flask, render_template, request, redirect, flash
import mysql.connector
from ebtables import add_rule, delete_rule

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="whitelist",
    auth_plugin='mysql_native_password'
)

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="db",
#     password="password",
#     database="whitelist"
# )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/conf', methods=['POST', 'GET'])
def conf():
    error = ''
    if request.method == 'POST':
        dev_ip = request.form['ip']
        dev = request.form['devices']
        error = add_sql(dev_ip, dev)
        print("ERROR:", error)

    dev_ip_list, dev_list = get_sql()
    
    return render_template('conf.html', len=len(dev_ip_list), dev_ip_list=dev_ip_list, dev_list=dev_list, error=error)

@app.route('/conf/del/<id>', methods=['POST'])
def delete_conf(id):
    dev = id.split(',')[0]
    dev_ip = id.split(',')[1]
    del_sql(dev_ip, dev)
    return redirect('/conf')

def add_sql(dev_ip, dev):
    error = ''
    stat = add_rule(dev_ip, dev)
    print(stat)
    mycursor = mydb.cursor(buffered=True)
    sql = "INSERT INTO whitelist (device_ip, device) VALUES (%s, %s)"
    val = (dev_ip, dev)
    
    try:
        mycursor.execute(sql, val)
        error = 'none'
    except mysql.connector.errors.IntegrityError as error:
        if 'Duplicate entry' in str(error):
            error = 'duplicate'

    mydb.commit()
    return error

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
    stat = delete_rule(dev_ip, dev)
    print(stat)
    mycursor = mydb.cursor()
    sql = "DELETE FROM whitelist where device_ip = '{}'".format(dev)
    mycursor.execute(sql)
    mydb.commit()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
