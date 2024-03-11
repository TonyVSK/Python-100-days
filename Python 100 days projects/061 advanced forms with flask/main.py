from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, AnyOf
from flask_bootstrap import Bootstrap5



# Following the documentation to use Flask Form WTF, the class needs to be in this format:
    # class MyForm(FlaskForm):
    #     name = StringField('name', validators=[DataRequired()])



class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), 
                                                   Email(),  
                                                   AnyOf(values=["admin@email.com"])])
    password = PasswordField(label='Password', validators=[DataRequired(),
                                         Length(min=8,
                                                max=20,
                                                message="At least 8 characters")])
    submit = SubmitField(label="Log in")




    

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)




@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    
    login_form = LoginForm()
    login_form.validate_on_submit()
    
    render_template('login.html', form=login_form)

    if request.method == 'GET':
        return render_template('login.html', form=login_form)
    
    if login_form.validate_on_submit():
        return render_template('success.html')
    else:
        return render_template('denied.html')
    
    # return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
