from flask import Flask
from flask import render_template
import random
from datetime import datetime
import requests


owm_Endpoint = "https://api.npoint.io/73cf3ccba6affe03411f"
response = requests.get(owm_Endpoint)
response.raise_for_status()
blog = response.json()

year = datetime.now().year



app = Flask(__name__)

# terminal command to environment variable: set FLASK_APP=hello.py (it is on documentation)
@app.route("/") # second command is flask run
def hello_world():
    return render_template("index.html", blog=blog)


@app.route("/index.html")
def index_file():
    return render_template("index.html", blog=blog)


@app.route("/about.html")
def about_file():
    return render_template("about.html")


@app.route("/contact.html")
def contact_file():
    return render_template("contact.html")


@app.route("/post.html")
def post_file():
    return render_template("post.html")



    
@app.route('/post/<identity>')
def get_post(identity):
    post = blog[int(identity)-1]
    return render_template("post.html", post=post, copyright=year)


# if __name__ == "__main__":
#     app.run(debug=True)




if __name__ == "__main__":
    app.run(debug=True)