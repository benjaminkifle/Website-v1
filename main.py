from flask import Flask, render_template, redirect, url_for, flash, abort
import secrets


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/resume')
def resume():
    return render_template("resume.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
