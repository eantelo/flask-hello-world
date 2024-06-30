from flask import Flask, render_template
import datetime
import requests

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
    api_key = "1bfa9f67da0f41609cc42654243006"
    city = "Santa Cruz de la Sierra"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url).json()
    weather = {
        "city": city,
        "temperature": response["current"]["temp_c"],
        "description": response["current"]["condition"]["text"],
        "icon": response["current"]["condition"]["icon"],
    }
    return render_template("dashboard.html", weather=weather)
