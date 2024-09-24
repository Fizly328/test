import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    current_year = datetime.datetime.now().strftime("%Y")
    context = {
        "page_name": "Главная",
        "age": int(current_year) - 2011}
    return render_template('index.html', **context )


@app.route("/blog/")
def blog():
    current_year = datetime.datetime.now().strftime("%Y")
    context = {
        "page_name": 'Блог',
        "year": current_year
    }
    return render_template('blog.html', **context)

@app.route("/contacts/")
def contacts():
    context = {
        "page_name": 'Контакты'
    }
    return render_template('contacts.html', **context)

if __name__ == "__main__":
    app.run()
