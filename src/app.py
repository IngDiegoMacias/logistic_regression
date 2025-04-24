from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("../models/logistic_regression_GS.sav", "rb"))


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        val1 = float(request.form["durat"])
        val2 = float(request.form["pdays"])
        val3 = float(request.form["varem"])
        val4 = float(request.form["eurib"])
        val5 = float(request.form["numem"])

        data = [[val1, val2, val3, val4, val5]]
        prediction = int(model.predict(data)[0])

    else:
        prediction = 0
    return render_template("index.html", prediction = prediction)
