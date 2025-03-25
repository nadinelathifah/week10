from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/Daphne')
def daphne_page():
    return render_template('index1.html')


@app.route('/Daphne2')
def daphne_page2():
    return render_template('index2.html')

if __name__ == "__main__":
    app.run(port=5001, debug=True)

