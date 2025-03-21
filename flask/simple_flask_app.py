"""
Import Flask, request, url_for by hovering over 'flask' and on the pop-up click 'install package'.
Once the package has been installed, create a requirements.txt file and add flask as a requirement.
The requirements page should now have 'flask~=3.1.0' written inside.
"""
from flask import Flask, request, url_for

# Instantiate an object 'app' from Flask.
app = Flask(__name__)

# @app.route is a Flask decorator that tells Flask to map the function hello_from_flask() to the URL '/hello'
# When a request comes to the /hello URL, call the function immediately after the URL.
# Example: after you run this block of code, go on Google and paste the link http://127.0.0.1:5000/hello
#          If this doesn't work, paste http://127.0.0.1:5001/hello
@app.route('/hello')
def hello_from_flask():
    return "★ Hello from Flask ★"

# http://127.0.0.1:5001/bye returns the following message on the browser.
@app.route('/bye')
def bye_from_flask():
    return "★ Goodbye from Flask ★"

# http://127.0.0.1:5000/get/strawberry
@app.route('/get/text')
def get_text():
    return "★ This is a HTTP GET request ★"

# Use postman for this and the rest:
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
