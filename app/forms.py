from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from .models import User

# -----------------------
# Registration & Login
# -----------------------
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email already registered.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# -----------------------
# Admin Forms
# -----------------------
class CourseForm(FlaskForm):
    title = StringField('Course Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Save')

class LessonForm(FlaskForm):
    title = StringField('Lesson Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    course_id = SelectField('Course', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Save')

class QuizForm(FlaskForm):
    title = StringField('Quiz Title', validators=[DataRequired()])
    course_id = SelectField('Course', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Save')

class QuestionForm(FlaskForm):
    text = StringField('Question Text', validators=[DataRequired()])
    choice_a = StringField('Choice A', validators=[DataRequired()])
    choice_b = StringField('Choice B', validators=[DataRequired()])
    choice_c = StringField('Choice C', validators=[DataRequired()])
    choice_d = StringField('Choice D', validators=[DataRequired()])
    correct_choice = SelectField('Correct Choice', choices=[('A','A'),('B','B'),('C','C'),('D','D')], validators=[DataRequired()])
    quiz_id = SelectField('Quiz', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Save')
