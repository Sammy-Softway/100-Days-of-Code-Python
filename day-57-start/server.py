from flask import Flask, render_template
import random
from datetime import datetime
import os
from dotenv import load_dotenv
import requests

load_dotenv()

GENDARIZE_URL = os.getenv("GENDARIZE_URL")
GENDARIZE_API_KEY = os.getenv("GENDARIZE_API_KEY")
AGIFY_URL = os.getenv("AGIFY_URL")

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.now().year
    return render_template("index.html", number = random_number, year=current_year)

@app.route('/guess/<name_input>')
def guess(name_input):
    parameters = {"name": name_input}
    genderize_response = requests.get(GENDARIZE_URL, params=parameters)
    genderize_datas =genderize_response.json()
    gender = genderize_datas["gender"]

    agify_response = requests.get(AGIFY_URL, params=parameters)
    agify_datas = agify_response.json()
    age = agify_datas["age"]

    return render_template("guess.html", name = name_input, gender = gender, age = age)

@app.route('/blog/<num>')
def blog_func(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_data = response.json()
    return render_template("blog.html", posts = blog_data)

if __name__ == "__main__":
    app.run(debug=True)