from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
from urllib.parse import unquote
from flask import session

app = Flask(__name__)

learning = [
    {
        "id": 1.1,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 1.2,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 1.3,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 2.1,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 2.2,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 2.3,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 3.1,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 3.2,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 3.3,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 4.1,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 4.2,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 4.3,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 5.1,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 5.2,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 5.3,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 6.1,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 6.2,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 6.3,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 7.1,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 7.2,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    },
    {
        "id": 7.3,
        "title": "Trick Name",
        "description": "This is the marketing trick known as...",
        "image": "https://i.pinimg.com/736x/ba/93/8b/ba938bcd4cb55a1a5dc18909ea0272d9.jpg",
        "price": "$"
    }
]

# ROUTES

@app.route('/')
def landingpage():
    return render_template('landingpage.html')

@app.route('/landingpage2')
def landingpage2():
    return render_template('landingpage2.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/learn/<lesson_id>')
def learn(lesson_id):
    lesson_id_float = float(lesson_id)
    product = next((item for item in learning if item["id"] == lesson_id_float), None)
    if product is None:
        return "Product not found", 404
    return render_template("learn.html", product=product, lesson_id=lesson_id)


## Added quiz part
app.secret_key = 'zoe-smart-shopping-secret'
quiz_questions = [
    {"id": 1, "description": "Buy some fresh apple juice…", "options": ["Product 1", "Product 2"], "answer": "Product 1"},
    {"id": 2, "description": "Buy some milk…", "options": ["Product 1", "Product 2"], "answer": "Product 2"},
    {"id": 3, "description": "Buy some bananas…", "options": ["Product 1", "Product 2"], "answer": "Product 1"},
    {"id": 4, "description": "Buy some soda…", "options": ["Product 1", "Product 2"], "answer": "Product 2"},
    {"id": 5, "description": "Buy some crispy chips…", "options": ["Product 1", "Product 2"], "answer": "Product 1"},
    {"id": 6, "description": "Buy some strawberry jam…", "options": ["Product 1", "Product 2"], "answer": "Product 1"},
    {"id": 7, "description": "Buy some eggs…", "options": ["Product 1", "Product 2"], "answer": "Product 2"},
]

@app.route("/quiz/<int:qid>")
def quiz(qid):
    if qid <= len(quiz_questions):
        return render_template("quiz.html", question=quiz_questions[qid - 1], total=len(quiz_questions))
    else:
        return redirect(url_for("quiz_result"))

@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    qid = int(request.form["qid"])
    selected = request.form["selected"]
    correct = quiz_questions[qid - 1]["answer"]
    session.setdefault("score", 0)
    if selected == correct:
        session["score"] += 1
    return redirect(url_for("quiz", qid=qid + 1))

@app.route("/quiz_result")
def quiz_result():
    score = session.get("score", 0)
    total = len(quiz_questions)
    session.clear()
    return render_template("result.html", score=score, total=total)

if __name__ == '__main__':
   app.run(debug = True, port=5001)

'''
Site Colors

Main - ?

Accent - ?

Light gray - #B2B6BD

Dark gray - #6c757d
'''