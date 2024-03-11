from flask import Flask
from flask import render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

# terminal command to environment variable: set FLASK_APP=hello.py (it is on documentation)
@app.route("/") # second command is flask run

def hello_world():
    current_year = datetime.now().year
    random_number = random.randint(1, 100)
    return render_template("index.html", num=random_number, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)