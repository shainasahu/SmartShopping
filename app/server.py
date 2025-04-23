from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from urllib.parse import unquote

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


if __name__ == '__main__':
   app.run(debug = True, port=5001)

'''
Site Colors

Main - ?

Accent - ?

Light gray - #B2B6BD

Dark gray - #717884
'''