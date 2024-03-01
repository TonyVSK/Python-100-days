from flask import Flask, render_template
# IF I WANT TO USE MY index.html FILE, I NEED TO CREATE A FOLDER DIRECTORY CALLED TEMPLATES, IT IS FLASK REQUISITE
app = Flask(__name__)

# terminal command to environment variable: set FLASK_APP=server.py (it is on documentation)
@app.route("/") # second command is flask run
def hello_world():
    return render_template("index.html") # I need to insert the name of the file who lives in templates folder


# or, you can avoid command run flask of local environment and run the commands just doing this:
if __name__ == "__main__":
    app.run(debug=True)