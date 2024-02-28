from flask import Flask

app = Flask(__name__)

# terminal command to environment variable: set FLASK_APP=hello.py (it is on documentation)
@app.route("/") # second command is flask run
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "Bye"

# or, you can avoid create an local environment and run the commands just doing this:
if __name__ == "__main__":
    app.run()