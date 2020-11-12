from flask import Flask
from flask import render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/detalhe/<string:time>")
def detalhe(time):
    return render_template("detalhe_" + time + ".html") 

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)