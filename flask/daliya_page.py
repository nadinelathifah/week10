
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/daliya')
def hello_from_daliya():
    return render_template("index1.html")

@app.route("/daliya/hello1")
def hello_1():
    return render_template("index.html")

# @app.route("/daliya/hello3")
# def hello_3():
#     return render_template("style.css")

@app.route("/daliya/hello2")
def hello_2():
    return render_template("index.html", content="Testing")

@app.route("/daliya/hello3")
def hello_3():
    return render_template("index2.html")

@app.route("/daliya/liya")
def liya():
    return render_template("liya.html")

@app.route("/daliya/nadine/hello_nadine")
def hello_nadine():
    return render_template('nadine.html')

@app.route("daliya/emma")
def emma_page():
    return render_template("emmas_page.html")

# @app.route('/<string:name>')
# def home(name):
#     return """
#      <html>
#         <head>
#         <title>Simple Flask App </title>
#          </head>
#
#         <body>
#             <h1>
#                 Homepage
#             </h1>
#             <p>
#                 Hello {}!
#             </p>
#
#         </body>
#      </html>
#
#
#      """.format(name)


if __name__ == "__main__":
    app.run(port=8000, debug=True)