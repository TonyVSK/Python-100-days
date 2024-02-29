from flask import Flask
from random import randint

computer = randint(1, 100)


app = Flask(__name__)



# terminal command to environment variable: set FLASK_APP=hello.py (it is on documentation)
@app.route("/") # second command is flask run
def hello_world():
    return f"<h1>Guess a number between 0 and 9</h1>\
    <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"



@app.route("/<strnumber>")
def greet(strnumber):
    number = int(strnumber)
    if number < computer:            
        return f"<h1 style='color: red'>Too low, try again!</h1>\
        <img src='https://www.publicdomainpictures.net/pictures/190000/nahled/sad-dog-1468499671wYW.jpg'>"
    elif number > computer:
        return f"<h1 style='color: purple'>Too high, try again!</h1>\
        <img src='https://cdn12.picryl.com/photo/2016/12/31/sad-dog-child-road-dog-emotions-4c1c74-1024.jpg'>"
    else:
        return f"<h1 style='color: green'>You found me!</h1>\
        <img src='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2021/12/30151747/Pembroke-Welsh-Corgi-smiling-and-happy-outdoors.jpeg'>"


# or, you can avoid create an local environment and run the commands just doing this:
if __name__ == "__main__":
    app.run(debug=True)