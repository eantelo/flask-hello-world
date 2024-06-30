from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Erick el Mejor!"


@app.route("/contacto")
def contacto():
    # get today date and time

    now = datetime.datetime.now()
    # return email and now date and time
    return "eri@hotmail.com" + now.strftime("%Y-%m-%d %H:%M:%S")


@app.route("/dashboard")
def dashboard():
    # Example data for the dashboard
    data = {
        "visitors": 1234,
        "page_views": 5678,
        "user_feedback": [
            {"date": "2023-04-01", "feedback": "Great site!"},
            {"date": "2023-04-02", "feedback": "Needs more content."},
        ],
    }
    return render_template("dashboard.html", data=data)
