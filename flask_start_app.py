# flask = module, Flask = class
from flask import Flask,render_template,jsonify

# app Flask class object
app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Berlin',
        'salary':'55000'
    },
        {
        'id':2,
        'title':'Data Scientist',
        'location':'Berlin',
        'salary':'65000'
    },
    {
        'id':3,
        'title':'Software Devloper' ,
        'location':'Berlin',
        'salary':'60000'
    }
]

#@ = decorator, route = path
@app.route("/")

def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)