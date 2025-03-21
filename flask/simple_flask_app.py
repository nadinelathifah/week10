from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/hello')
def hello_from_flask():
    return "★ Hello from Flask ★"


@app.route('/bye')
def bye_from_flask():
    return "★ Goodbye from Flask ★"


@app.route('/get/text')
def get_text():
    return "★ This is a HTTP GET request ★"


@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return "★ This is a POST request. The data you sent was: " + data_sent


@app.route('/echo/<word>')
def echo(word):
    return "★ Echo: " + word.upper()


@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    line = "Your number squared is " + str(squared)
    return line


@app.route('/sayhello/<string:name>')
def hello_name(name):
    greeting = "★ Hello " + name.title()
    return greeting


@app.route('/<string:name>')
def home(name):
    return """
    <html>
        <head>
            <title>Simple Flask App</title>
        </head>
        <body>
            <h1>Home Page</h1>
            <p>★ Hey {}! ★ (˶ˆᗜˆ˵)♡ 𐦍⋆</p>
        </body>
        
    </html>
    """.format(name)


@app.route('/index/<string:name>/<int:age>')
def index(name, age):
    url = url_for('get_text')
    return """
    <html>
        <head>
            <title>About Page</title>
        </head>
        <body>
            <h1>Index Page</h1>
            <p>★ Hey {}! ★ (˶ˆᗜˆ˵)♡ 𐦍⋆</p>
            <p>This year you're {} year(s) old. Here's to another year of sparkles!</p>
            <hr>
            <a href="{}">Welcome</a>
        </body>

    </html>
    """.format(name, age, url)



if __name__ == "__main__":
    app.run(port=5001, debug=True)
