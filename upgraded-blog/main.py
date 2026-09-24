from flask import Flask, render_template
import requests

NPOINT_URL = "https://api.npoint.io/0f185497b97a7fc55af9"
response = requests.get(NPOINT_URL)
blog_data = response.json()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', blog_list=blog_data)

@app.route('/post/<int:post_id>')
def post(post_id):
    requested_blog = None
    for blog in blog_data:
        if blog['id'] == post_id:
            requested_blog = blog
    return render_template('post.html', blog=requested_blog)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)