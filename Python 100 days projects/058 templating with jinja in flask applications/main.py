from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

owm_Endpoint = "https://api.npoint.io/ad2df58d95fa88b81352"
response = requests.get(owm_Endpoint)
response.raise_for_status()
blog = response.json()

year = datetime.now().year

@app.route('/')
def home():

    return render_template("index.html", blog=blog, copyright=year)
    
    
@app.route('/post/<identity>')
def get_post(identity):
    post = blog[int(identity)-1]
    return render_template("post.html", post=post, copyright=year)


if __name__ == "__main__":
    app.run(debug=True)