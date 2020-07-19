from flask import Flask, render_template, request

from ebtables import ebtables

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/conf', methods=['POST', 'GET'])
def conf():
    if request.method == 'POST':
        src = request.form['src']
        dev = request.form['dev']
        conf_table(dev, src)
    return render_template('conf.html')

@app.route('/add_conf', methods=['POST', 'GET'])
def conf_add():
    return render_template('conf_add.html')

def conf_table(device_ip, src_ip):
    print("")

if __name__ == '__main__':
    app.run(debug=True, port=5001)