from flask import Flask, jsonify, request,render_template
import datetime
app = Flask(__name__)


@app.route('/process', methods=['POST'])
def process():
    date = days(request.form['date'])
    return render_template("process.html",date=date)
@app.route("/Calcuday")
def about():
    return render_template("Calcuday.html")

def days(Targetdate):
    today = datetime.datetime.now()
    targetd = datetime.datetime.strptime(Targetdate,"%Y-%m-%d")
    return str(targetd-today).split(' days')[0]

if __name__ == '__main__':
    app.run(debug=True)