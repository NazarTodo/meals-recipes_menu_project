from flask import Flask, render_template, request, url_for, redirect
import sys, random

sys.path.append("..")
from main import main

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == "POST":
            return redirect(url_for('q1'))
        return render_template('index.html')
    except:
        return render_template('index.html')


@app.route("/q1/", methods=["GET", "POST"])
def q1():
    global breakfast_lst
    try:
        if request.method == "POST":
            breakfast_lst = request.form.getlist("breakfast")
            return redirect(url_for('q2'))
        return render_template('q1.html')
    except:
        return render_template('q1.html')


@app.route('/q2/', methods=["GET", "POST"])
def q2():
    global lunch_lst
    try:
        if request.method == "POST":
            veg = request.form.getlist("choice3")
            if len(veg) > 3:
                veg = random.sample(veg, 3)
            lunch_lst = request.form.getlist("choice2") + request.form.getlist("choice1") + veg + request.form.getlist(
                "choice4")

            return redirect(url_for('q3'))
        return render_template('q2.html')
    except:
        return render_template('q2.html')


@app.route('/q3/', methods=["GET", "POST"])
def q3():
    global dinner_lst
    try:
        if request.method == "POST":
            dinner_lst = request.form.getlist("deserts")
            return redirect(url_for('menu'))
        return render_template('q3.html')
    except:
        return render_template('q3.html')


@app.route('/menu/', methods=["GET", "POST"])
def menu():
    breakfast = main(breakfast_lst)
    lunch = main(lunch_lst)
    dinner = main(dinner_lst)
    menu = {}
    for e in [breakfast, lunch, dinner]:
        menu.update(e)
    return render_template('menu.html',
                           menu=menu)


if __name__ == "__main__":
    app.debug = True
    app.run()
