from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/molly")
def molly():
    n1 = 10
    n2 = 20
    sum = n1 + n2
    return str(sum)

@app.route("about") 
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)




