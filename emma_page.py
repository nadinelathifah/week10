
from flask import Flask, request, url_for,render_template

app = Flask (__name__)

@app.route("/emma")
def emma_page():
    return render_template("emmas_page.html")

if __name__ == '__main__':
    app.run(debug=True)
