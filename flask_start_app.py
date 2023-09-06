# flask = module, Flask = class
from flask import Flask,render_template

# app Flask class object
app = Flask(__name__)

#@ = decorator, route = path
@app.route("/")

def hello_world():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)