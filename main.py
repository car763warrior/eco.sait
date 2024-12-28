from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/bears")
def bears():
    return render_template('bears.html')

@app.route("/penguins")
def penguins():
    return render_template('penguins.html')

@app.route("/trees")
def trees():
    return render_template('trees.html')

app.run(debug=True)