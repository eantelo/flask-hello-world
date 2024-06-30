from flask import Flask
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
