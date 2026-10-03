from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
THE_EMAIL = os.getenv("THE_EMAIL")
THE_PASSWORD = os.getenv("THE_PASSWORD")


class LoginForm(FlaskForm):
    name = StringField(label='Name')
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = SECRET_KEY
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == THE_EMAIL and login_form.password.data == THE_PASSWORD:
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)