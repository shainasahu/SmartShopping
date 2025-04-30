from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
from urllib.parse import unquote
from flask import session

app = Flask(__name__)
app.secret_key = "your-secret-key"

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

@app.route('/quiz-intro')
def quiz_intro():
    session.clear()
    return render_template('quiz_intro.html')

## Added quiz part
app.secret_key = 'zoe-smart-shopping-secret'
quiz_data = [
    {"id": 1, "images": ["juice_7.99.png", "juice_7.00.png"], "hint": "Buy some fresh apple juice…", "options": ["$7.99", "$7.00"], "tactic": "Charm Pricing", "correct_price": "$7.00"},
    {"id": 2, "images": ["milk_5.99.png", "milk_4.99.png"], "hint": "Buy some milk…", "options": ["$5.99 – “Only 2 left!”", "$4.99"], "tactic": "Scarcity Urgency", "correct_price": "$4.99"},
    {"id": 3, "images": ["banana_3.99.png", "banana_2.99.png"], "hint": "Buy some bananas…", "options": ["$3.99 – Premium Organic", "$2.99 – Regular"], "tactic": "Labeling", "correct_price": "$2.99 – Regular"},
    {"id": 4, "images": ["soda_6.49.png", "soda_6.99.png"], "hint": "Buy some soda…", "options": ["$6.49", "$6.99 – was $10.9"], "tactic": "Anchoring", "correct_price": "$6.49"},
    {"id": 5, "images": ["chips_2.99.png", "chips_5.99.png"], "hint": "Buy some crispy chips…", "options": ["1 for $2.99", "1 for $5.99 – Buy 1 Get 1 50% Off"], "tactic": "BOGO Deals", "correct_price": "1 for $2.99"},
    {"id": 6, "images": ["jam_4.49.png", "jam_3.99.png"], "hint": "Buy some strawberry jam…", "options": ["$4.49 – “Best Seller!”", "$3.99"], "tactic": "Social Proof", "correct_price": "$3.99"},
    {"id": 7, "images": ["eggs_4.49.png", "eggs_3.99.png"], "hint": "Buy some eggs…", "options": ["$4.49 for 400g", "$3.99 for 250g"], "tactic": "Unit Price Confusion", "correct_price": "$3.99 for 250g"}
]

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST' or 'step' not in session:
        if 'step' not in session:  # fresh start
            session['step'] = 0
            session['total_spent'] = 0
            session['choices'] = []

        selected = request.form.get('selected_price')
        current_item = quiz_data[session['step']]
        is_correct = selected == current_item['correct_price']

        # Handle skipped/empty submission
        if not selected:
            price_value = 0
        else:
            try:
                price_value = float(selected.replace('$', '').split()[0])
            except (ValueError, IndexError):
                price_value = 0

        session['choices'].append({
            'item': current_item,
            'selected': selected,
            'is_correct': is_correct
        })
        session['total_spent'] += price_value
        session['step'] += 1

    if session['step'] >= len(quiz_data):
        return redirect(url_for('quiz_result'))

    item = quiz_data[session['step']]
    paired = list(zip(item["options"], item["images"]))
    return render_template('quiz.html', item=item, paired=paired)



@app.route('/quiz-result')
def quiz_result():
    choices = session.get('choices', [])
    total_spent = session.get('total_spent', 0)
    best_value = sum([float(item['correct_price'].replace('$', '').split()[0]) for item in quiz_data])
    correct_count = sum(1 for c in choices if c['is_correct'])
    score_percentage = round(correct_count / len(quiz_data) * 100)
    return render_template('quiz_result.html', 
                           total_spent=total_spent,
                           best_value=best_value,
                           choices=choices,
                           correct_count=correct_count,
                           score_percentage=score_percentage)

if __name__ == '__main__':
   app.run(debug = True, port=5001)
'''
Site Colors

Main - ?

Accent - ?

Light gray - #B2B6BD

Dark gray - #6c757d
'''