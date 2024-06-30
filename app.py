from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/contacto")
def contacto():
    # get today date and time

    now = datetime.datetime.now()
    data = now.strftime("%Y-%m-%d %H:%M:%S")
    # return email and now date and time
    return render_template("contacto.html", data=data)


@app.route("/")
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
