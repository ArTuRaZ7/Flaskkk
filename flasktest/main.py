from flask import Flask, render_template, request
from user import User
import random
import string
import csv

users = []

app = Flask(__name__)

citi = {"Челябинск": 1187960, "Москва":1200000, "Екатеринбург": 1493600}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/cities')
def cities():
    return render_template('cities.html')


@app.route("/cities/millionaires")
def millionaires():
    with open('millionairesCities.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        dict = {rows[0]:rows[1] for rows in reader}
    return render_template('millionaires.html', h='Список городов миллионеров', a=dict)


@app.route("/cities/biggest")
def biggest():
    with open('biggestCities.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        dict = {rows[0]:rows[1] for rows in reader}
    return render_template('millionaires.html', h='Список крупнейших городов', a=dict)


@app.route("/cities/large")
def large():
    with open('largeCities.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        dict = {rows[0]:rows[1] for rows in reader}
    return render_template('millionaires.html', h='Список больших городов', a=dict)


@app.route("/cities/big")
def big():
    with open('bigCities.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        dict = {rows[0]:rows[1] for rows in reader}
    return render_template('millionaires.html', h='Список крупных городов', a=dict)


@app.route("/cities/medium")
def medium():
    with open('mediumCities.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        dict = {rows[0]:rows[1] for rows in reader}
    return render_template('millionaires.html', h='Список средних городов', a=dict)


@app.route("/cities/small")
def small():
    with open('smallCities.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        dict = {rows[0]:rows[1] for rows in reader}
    return render_template('millionaires.html', h='Список малых городов', a=dict)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/add', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        surname = request.form.get('surname')
        password = request.form.get('password')
        users.append(User(email, name, surname, password))
        print("Пользователь добавлен")
        print(users[0].name)
    return render_template('add.html')


@app.route('/persons')
def persons():
    return render_template('persons.html', p=users)


if __name__ == '__main__':
    app.run()