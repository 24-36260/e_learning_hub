from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# -----------------------
# User Model
# -----------------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# -----------------------
# Course Model
# -----------------------
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    lessons = db.relationship('Lesson', backref='course', lazy=True)
    quizzes = db.relationship('Quiz', backref='course', lazy=True)


# -----------------------
# Lesson Model
# -----------------------
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)


# -----------------------
# Quiz Model
# -----------------------
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    questions = db.relationship('Question', backref='quiz', lazy=True)


# -----------------------
# Question Model
# -----------------------
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), nullable=False)
    choice_a = db.Column(db.String(150), nullable=False)
    choice_b = db.Column(db.String(150), nullable=False)
    choice_c = db.Column(db.String(150), nullable=False)
    choice_d = db.Column(db.String(150), nullable=False)
    correct_choice = db.Column(db.String(1), nullable=False)  # 'A', 'B', 'C', 'D'
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
