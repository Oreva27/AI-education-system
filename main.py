from fastapi import FastAPI

app = FastAPI()  # This is the ASGI app instance

@app.get("/")  
def home():  
    return {"message": "AI Education System API is running!"}
from fastapi import FastAPI

app = FastAPI()

# 📌 1. User Authentication
@app.post("/register")
def register_user():
    return {"message": "User registered successfully"}

@app.post("/login")
def login_user():
    return {"message": "User logged in successfully"}

# 📌 2. Courses
@app.get("/courses")
def get_courses():
    return {"courses": ["Mathematics", "Science", "History"]}

@app.post("/courses")
def create_course():
    return {"message": "Course created successfully"}

# 📌 3. Lessons
@app.get("/courses/{course_id}/lessons")
def get_lessons(course_id: int):
    return {"lessons": [f"Lesson 1 of course {course_id}", f"Lesson 2 of course {course_id}"]}

@app.post("/courses/{course_id}/lessons")
def add_lesson(course_id: int):
    return {"message": f"Lesson added to course {course_id}"}

# 📌 4. Quizzes
@app.get("/quizzes")
def get_quizzes():
    return {"quizzes": ["Quiz 1", "Quiz 2"]}

@app.post("/quizzes")
def create_quiz():
    return {"message": "Quiz created successfully"}

# 📌 5. Progress
@app.get("/progress/{user_id}")
def get_progress(user_id: int):
    return {"progress": f"Progress for user {user_id}"}

@app.post("/progress")
def update_progress():
    return {"message": "User progress updated"}
