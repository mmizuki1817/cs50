import os
import time

from cs50 import SQL
from flask import Flask, render_template, redirect, request

# list
TIMERS = []

# ファイル内変数
HOUR_TO_SEC = 3600
MIN_TO_SEC = 60
HOUR_TO_MIN = 60

# Configure application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        # 値が入力されてるか確認
        if not request.form.get("hour"):
            return render_template("apology.html", message="作業時間を入力してください")
        if not request.form.get("minute"):
            return apology("please input minute", messa)
        if not request.form.get("interval"):
            return apology("please input interval", 400)
        if not request.form.get("cycle"):
            return apology("please input set", 400)
        if not request.form.get("rest"):
            return apology("please input rest", 400)
        if not request.form.get("rest_times"):
            return render_template("apology.html", message="help")

        # listTIMERS
        hour = int(request.form.get("hour"))
        minute = int(request.form.get("minute"))
        interval = int(request.form.get("interval"))
        cycle = int(request.form.get("cycle"))
        rest = int(request.form.get("rest"))
        rest_times = int(request.form.get("rest_times"))
        if hour == 0 and minute == 0:
            return render_template()

        # listTIMERSに追加
        TIMERS.insert(0, int(request.form.get("hour"))) # 0 時間
        TIMERS.insert(1, int(request.form.get("minute"))) # 1 分
        TIMERS.insert(2, int(request.form.get("interval"))) # 2 分
        TIMERS.insert(3, int(request.form.get("cycle"))) # 3 セット

        if (rest >= 1 and rest_times >= 1):
            TIMERS.insert(4, int(request.form.get("rest"))) # 4 分
            TIMERS.insert(5, int(request.form.get("rest_times"))) # 5 回

            return render_template("home.html", hour=hour, minute=minute, interval=interval, cycle=cycle, rest=rest, rest_times=rest_times,
            py_js_hour=TIMERS[0], py_js_minute=TIMERS[1], py_js_interval=TIMERS[2], py_js_cycle=TIMERS[3], py_js_rest=TIMERS[4], py_js_rest_times=TIMERS[5])

        else: # 後で作成
            return render_template("home1.html",hour=hour, minute=minute, interval=interval, cycle=cycle,
            py_js_hour=TIMERS[0], py_js_minute=TIMERS[1], py_js_interval=TIMERS[2], py_js_cycle=TIMERS[3])

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    else: # startボタンが押される
        return render_template("home.html")

@app.route("/home1", methods=["GET", "POST"])
def home1():
    if request.method == "GET":
        return render_template("index.html")

    else: # startボタンが押される
        return render_template("home1.html")

@app.route("/apology", methods=["GET", "POST"])
def apology():
    if request.method == "GET":
        return render_template("apology.html")
    else:
        return render_template("index.html")



#CREATE TABLE timer
#( id INTEGER PRIMARY KEY AUTOINCREMENT,
#hour INTEGER NOT NULL,
#minute INTEGER NOT NULL,
#interval INTEGER NOT NULL,
#cycle INTEGER NOT NULL,
#rest INTEGER NOT NULL,
#rest_times INTEGER NOT NULL)