from flask import Flask, render_template
import requests
from post import Post

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(BLOG_URL)
blog_data = response.json()

post_objects = []

for post in blog_data:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = post_objects)

@app.route('/post/<int:post_id>')
def blog_post(post_id):
    requested_post = None
    for blog in post_objects:
        if blog.id == post_id:
            requested_post = blog
    return render_template("post.html", post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)
