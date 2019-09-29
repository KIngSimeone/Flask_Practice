from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, AnyOf, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Mysecret!'

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('A username is required!'), Length(min=4, max=8, message='Must be between 4 and 8 characters')])
    password = PasswordField('password', validators=[InputRequired('Password is required!'), AnyOf(values=['secret', 'password'])])
    age = IntegerField('age')
    true = BooleanField('true')
    email = StringField('email', validators=[Email()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>Username: {} Password: {} Age: {} True: {} Email: {}</h1>'.format(form.username.data, form.password.data, form.age.data, form.true.data, form.email.data)

    return render_template('flask_wtf.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)