from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Course, Lesson, Quiz, Question, db
from .forms import LoginForm, RegisterForm, CourseForm, LessonForm, QuizForm, QuestionForm

main_routes = Blueprint("main", __name__)

# -----------------------
# Home & Auth
# -----------------------
@main_routes.route("/")
def index():
    courses = Course.query.all()
    return render_template("index.html", courses=courses)

@main_routes.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please login.", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

@main_routes.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for("main.dashboard"))
        else:
            flash("Invalid credentials", "danger")
    return render_template("login.html", form=form)

@main_routes.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.index"))

@main_routes.route("/dashboard")
@login_required
def dashboard():
    if current_user.is_admin:
        return render_template("admin/admin_dashboard.html")
    return render_template("dashboard.html")

@main_routes.route("/course/<int:course_id>")
def course_detail(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template("course_detail.html", course=course)
