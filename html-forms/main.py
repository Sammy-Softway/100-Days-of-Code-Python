from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password']:
        username = request.form['username']
        password = request.form['password']
        return f"<h1>Name:{username}, Password: {password}</h1>"
    else:
        error = 'Invalid username/password'
        return f"<h1>{error}</h1>"


if __name__ == '__main__':
    app.run(debug=True)