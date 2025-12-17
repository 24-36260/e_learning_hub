from app import db, User, Course, Lesson, Quiz, Question, create_app

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create default users
    admin = User(name="Admin User", email="admin@elearn.local", role="admin")
    admin.set_password("adminpass")
    student = User(name="Student User", email="student@elearn.local")
    student.set_password("studentpass")
    db.session.add_all([admin, student])

    # Create courses
    c1 = Course(title="Introduction to HTML and CSS",
                short_desc="Learn basic web development with HTML and CSS.",
                content="HTML structures pages, CSS styles them.")
    c2 = Course(title="Programming Basics (Python)",
                short_desc="Syntax, variables, control flow, functions.",
                content="Learn Python from scratch.")
    db.session.add_all([c1, c2])
    db.session.commit()

    # Add lessons
    l1 = Lesson(title="HTML Basics", content="HTML stands for Hypertext Markup Language.", course_id=c1.id)
    l2 = Lesson(title="CSS Basics", content="CSS is used for styling HTML elements.", course_id=c1.id)
    db.session.add_all([l1, l2])
    db.session.commit()

    # Add quizzes
    qz1 = Quiz(title="Python Basics Quiz", course_id=c2.id)
    db.session.add(qz1)
    db.session.commit()

    # Add questions
    q1 = Question(text="What is the keyword to define a function in Python?", correct_answer="def", quiz_id=qz1.id)
    db.session.add(q1)
    db.session.commit()

    print("Database seeded successfully!")
