from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <h1>:D</h1>
    <a href="/about"> Перейти на ABOUT </a>"""

@app.route("/about")
def about():
    return """<h1>Hello</h1>
    <a href="/facts"> Перейти на FACTS </a>"""

@app.route("/facts")
def facts():
    facts_list = [
        "/secret",
        "Привет!",
        "Пока",
        "ss_groove",
        ":P",
        "Где-то секретная страничка!"
    ]
    return f"""<h1>{random.choice(facts_list)}</h1>
    <a href="/"> Перейти на HELLO_WORLD </a>"""

@app.route("/secret")
def secret():
    return """<h1>Секретная страница!</h1>
    <a href="/about"> Перейти на ABOUT </a>
    <a href="/facts"> Перейти на FACTS </a>
    <img src="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/aliviya/phpGWdNyf.png" alt="Error-404">"""
    

app.run(debug=True)
