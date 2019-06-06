from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about_me():
    return  render_template("about_Me.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/portfolio/google")
def google():
    return render_template("google.html")

@app.route("/portfolio/Peluqueria")
def Peluqueria():
    return render_template("Peluqueria.html")

if __name__ == "__main__":
    app.run(debug=True)