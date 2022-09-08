from user import User
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, Length, regexp, number_range
import csv
import re

users = []

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your secret key'

class addForm(FlaskForm):
    email = StringField("Email: ", validators=[Email()])
    name = StringField("Name: ", validators=[DataRequired(), Length(1, 20)])
    surname = StringField("Surname", validators=[DataRequired(), Length(1, 20)])
    password = PasswordField("Password", validators=[DataRequired(), regexp('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}')])
    age = IntegerField("Age", validators=[number_range(14, 100)])
    submit = SubmitField("Submit")

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
    form = addForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        surname = form.surname.data
        password = form.password.data
        age = form.age.data
        users.append(User(email, name, surname, age, password))
        return redirect(url_for('new'))
    return render_template('add.html', form=form)


@app.route('/persons')
def persons():
    return render_template('persons.html', p=users)


if __name__ == '__main__':
    app.run()