from user import User
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, Length, regexp, number_range
import csv

users = []

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hahaha'


class AddForm(FlaskForm):
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


@app.route("/cities/<string:t>")
def millionaires(t):
    dictOfHeadlines = {'millionaires': 'Список городов миллионеров', 'biggest': 'Список крупнейших городов',
                       'large': 'Список больших городов', 'big': 'Список крупных городов',
                       'medium': 'Список средних городов', 'small': 'Список малых городов'}

    with open(f'csv/{t}Cities.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        dictOfCities = {rows[0]: rows[1] for rows in reader}

    return render_template('millionaires.html', h=dictOfHeadlines[t], a=dictOfCities)


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
    form = AddForm()
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