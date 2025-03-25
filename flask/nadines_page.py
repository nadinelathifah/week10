
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/nadine/hello_nadine")
def hello_nadine():
    return render_template('nadine.html')

if __name__ == "__main__":
    app.run(port=5001, debug=True)

