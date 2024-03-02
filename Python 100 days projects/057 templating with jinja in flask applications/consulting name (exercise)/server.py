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




@app.route("/guess/<name>")
def say_bye(name):

    endpoint = f"https://api.agify.io/?name={name}"
    response = requests.get(endpoint)
    response.raise_for_status()
    user_data = response.json()

    gender_endpoint=f"https://api.genderize.io/?name={name}"
    response2 = requests.get(gender_endpoint)
    response2.raise_for_status()
    gender_definitions = response2.json()

    name = user_data["name"]
    age = user_data["age"]
    gender = gender_definitions["gender"]

    return render_template("index.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)