from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired



# Following the documentation to use Flask Form WTF, the class needs to be in this format:
    # class MyForm(FlaskForm):
    #     name = StringField('name', validators=[DataRequired()])



class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log in", validators=[DataRequired()])


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"





@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
