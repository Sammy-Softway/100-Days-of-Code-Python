from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def inner():
        return f"<b>{func()}</b>"
    return inner

def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

def make_underline(func):
    def inner():
        return "<u>" + func() + "</u>"
    return inner

@app.route('/')
def hello_world():
    #Rendering HTML Elements
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'

#Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, you are number {number}!"

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
