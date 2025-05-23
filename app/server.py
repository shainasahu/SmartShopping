from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
from urllib.parse import unquote
from flask import session
import time
import re

app = Flask(__name__)
app.secret_key = 'zoe-smart-shopping-secret'

quiz_data = [
    {
        "id": 1, 
        "images": ["/static/img/1.1.png", "/static/img/1.2.png"],
        "description": "Buy some fresh apple juice…",
        "options": ["$7.00", "$7.99"], 
        "hint": "Numbers ending in .99 feel cheaper.", 
        "correct_price": ["$7.00",7.00],
        "incorrect_price": ["$7.99",7.99]
    },
    {
        "id": 2, 
        "images": ["/static/img/2.1.png", "/static/img/2.2.png"],
        "description": "Buy some bananas…",
        "options": ["$2.99 - Regular", "$3.99 - Premium Organic"], 
        "hint": "Labels boost perceived value.", 
        "correct_price": ["$2.99 - Regular", 2.99],
        "incorrect_price": ["$3.99 - Premium Organic", 3.99]
    },
    {
        "id": 3, 
        "images": ["/static/img/3.1.png", "/static/img/3.2.png"],
        "description": "Buy some milk…",
        "options": ["$6.49", "$6.99 - was $10.9"], 
        "hint": "A higher 'original price' makes a deal feel better.", 
        "correct_price": ["$6.49", 6.49],
        "incorrect_price": ["$6.99 - was $10.99", 6.99]
    },
    {
        "id": 4, 
        "images": ["/static/img/4.1.png", "/static/img/4.2.png"],
        "description": "Buy some eggs…",
        "options": ["$4.49 for 400g", "$3.99 for 250g"], 
        "hint": "Check the cost per unit.", 
        "correct_price": ["$4.49 for 400g", 4.49],
        "incorrect_price": ["$3.99 for 250g", 6.384] # this is the price of 400g
    },
    {
        "id": 5, 
        "images": ["/static/img/5.1.png", "/static/img/5.2.png"],
        "description": "Buy some delicious jam…",
        "options":  ["1 for $2.99 - Strawberry Jam", "1 for $5.99 - Buy 1 Get 1 50% Off"], 
        "hint": "BOGO deals sound more exciting than they are.", 
        "correct_price": ["1 for $2.99 - Strawberry Jam", 2.99],
        "incorrect_price": ["1 for $5.99 - Buy 1 Get 1 50% Off", 5.99]
    },
    {
        "id": 6, 
        "images": ["/static/img/6.1.png", "/static/img/6.2.png"],
        "description": "Buy some chips…",
        "options": ["$3.99 - Crispy Chips!", "$4.49 - Best Selling Chips!"], 
        "hint": "We tend to follow the crowd.", 
        "correct_price": ["$3.99 - Crispy Chips!", 3.99],
        "incorrect_price": ["$4.49 - Best Selling Chips!", 4.49]
    },
    {
        "id": 7, 
        "images": ["/static/img/7.1.png", "/static/img/7.2.png"],
        "description": "Buy some soda…",
        "options": ["$4.99 - Soda", "$5.99 - Only 2 left!"], 
        "hint": "Some phrases create fear of missing out.", 
        "correct_price": ["$4.99 - Soda", 4.99],
        "incorrect_price": ["$5.99 - Only 2 left!", 5.99]
    }
]

learning = [
    {
        "id": 1.1,
        "title": "Charm Pricing",
        "description": "Numbers that end in .99 feel cheaper—even though it's just a one-cent difference. Our brains focus on the first digit and think it's a better deal.",
        "image": "/static/img/1.1.png",
        "price": "$2.99 | $3.00"
    },
    {
        "id": 1.2,
        "title": "Phonetic Pricing",
        "description": "Prices like $27.82 (five syllables) feel cheaper than $28.16 (six syllables), even if they're basically the same.",
        "image": "/static/img/1.2.png",
        "price": "twenty-seven eighty-two | twenty-eight sixteen"
    },
    {
        "id": 1.3,
        "title": "Visual Compression",
        "description": "Removing the comma makes prices feel smaller and less intimidating.",
        "image": "/static/img/1.1.png",
        "price": "$1699 | $1,699"
    },
    {
        "id": 2.1,
        "title": "Labeling",
        "description": "Labeling using words like “high performance” or “luxury” boost perceived value—even without added features.",
        "image": "/static/img/2.1.png",
        "price": "$5.99 - Regular Cereal | $7.99 - Premium Cereal"
    },
    {
        "id": 2.2,
        "title": "Payment Framing",
        "description": "Showing the price in installments makes it feel more affordable, even if it's the same amount. $1/day feels cheaper than $365/year.",
        "image": "/static/img/2.2.png",
        "price": "Just $4.00! | Just 17¢ per serving! (actually $5.00)"
    },
    {
        "id": 2.3,
        "title": "Unit Price Confusion",
        "description": "Bigger packages can seem like better value, but they often cost more per unit (like per ounce). Most people don't check the fine print and end up paying more for less.",
        "image": "/static/img/2.1.png",
        "price": "$2.99 for 12 oz | $4.99 for 20 oz"
    },
    {
        "id": 3.1,
        "title": "Odd Even Pricing",
        "description": "Prices like $4.97 feel cheaper than $5.00. The odd number makes it seem like you're getting a deal because we round down in our minds.",
        "image": "/static/img/3.1.png",
        "price": "$4.97 | $5.00"
    },
    {
        "id": 3.2,
        "title": "Visual Contrast in Sale Prices",
        "description": "Striking out the old price and using bold fonts/colors on sale prices make discounts feel more exciting than they actually are.",
        "image": "/static/img/3.2.png",
        "price": "$25! $50"
    },
    {
        "id": 3.3,
        "title": "Scarcity Urgency",
        "description": "Phrases like “Only 2 left!” or “Limited Time Offer!” create pressure and fear of missing out, pushing us to make fast decisions or spend unwisely.",
        "image": "/static/img/3.1.png",
        "price": "$7.99. Only 1 left!"
    },
    {
        "id": 4.1,
        "title": "BOGO deals",
        "description": "Buy-one-get-one offers sound exciting, but they often push you to spend more than planned. You think you're saving money, but only if you actually needed the second item.",
        "image": "/static/img/4.1.png",
        "price": "$3 | $6 with buy 1 get 1 free"
    },
    {
        "id": 4.2,
        "title": "Social Proof",
        "description": "If a product is labeled as a “Best Seller” or has hundreds of good reviews, we assume its a good choice. We tend to follow the crowd, especially when making quick decisions.",
        "image": "/static/img/4.2.png",
        "price": "$6.99 - Best Seller | $4.99 - Regular"
    },
    {
        "id": 4.3,
        "title": "Anchoring",
        "description": "We compare prices based on the first number we see, even if it's inflated. A fake “original price” makes a regular deal feel like a huge bargain.",
        "image": "/static/img/4.1.png",
        "price": "$4.00 $6.00. | $4.49"
    },
        {
        "id": 5.1,
        "title": "Decoy Pricing",
        "description": "Introducing a higher-priced 'decoy' option makes the mid-tier product seem more reasonable, nudging us to spend more than we planned.",
        "image": "/static/img/5.1.png",
        "price": "$3 small | $6 medium | $6.50 large"
    },
    {
        "id": 5.2,
        "title": "Price Placement",
        "description": "Prices placed to the left of the product feel cheaper than those on the right. It’s a layout trick that subtly changes our perception.",
        "image": "/static/img/5.2.png",
        "price": "$4.99 | $4.99"
    },
    {
        "id": 5.3,
        "title": "Font & Size Psychology",
        "description": "Smaller, lighter fonts make prices seem lower—even when the number itself doesn't change. Bigger, bold fonts feel expensive.",
        "image": "/static/img/5.1.png",
        "price": "$6.99 | $6.99"
    },
    {
        "id": 6.1,
        "title": "Emotion-Based Pricing",
        "description": "Words like 'Treat Yourself' or 'Deserve This' make us justify impulse purchases emotionally rather than logically.",
        "image": "/static/img/6.1.png",
        "price": "$5.99 — Treat yourself!"
    },
    {
        "id": 6.2,
        "title": "Zero Price Effect",
        "description": "Free add-ons feel disproportionately valuable—even if the added item is cheap or unnecessary.",
        "image": "/static/img/6.2.png",
        "price": "$4.00 + free sticker | $3.99 alone"
    },
    {
        "id": 6.3,
        "title": "Time vs. Money Framing",
        "description": "Saying 'Save Time' rather than 'Save Money' appeals more emotionally, making purchases feel worthwhile beyond the price.",
        "image": "/static/img/6.1.png",
        "price": "$5.49 - Skip the wait!"
    },
    {
        "id": 7.1,
        "title": "Pre-selected Options",
        "description": "Default choices are often the most expensive ones. People tend to go with the default to save time or avoid decision fatigue.",
        "image": "/static/img/7.1.png",
        "price": "$6.99 default | $4.99 small"
    },
    {
        "id": 7.2,
        "title": "Bundle Bias",
        "description": "Bundling items together makes you feel like you're saving, even when individual prices might be cheaper separately.",
        "image": "/static/img/7.2.png",
        "price": "$12 meal deal | $3 + $4 + $2 separate products ($9)"
    },
    {
        "id": 7.3,
        "title": "Misleading Size Comparisons",
        "description": "Different container shapes (taller, narrower) can make products look like they contain more, tricking you into paying more for less.",
        "image": "/static/img/7.1.png",
        "price": "$2.99 tall bottle (10 oz) | $2.79 short bottle (12 oz)"
    }
]

# ROUTES

@app.route('/track_learn_time')
def track_learn_time():
    lesson_id = request.args.get('lesson_id')
    time_spent = float(request.args.get('time_spent', 0))
    
    # Initialize the session tracking if it doesn't exist
    if 'learn_times' not in session:
        session['learn_times'] = {}
    
    # Store or accumulate time for this lesson
    if lesson_id in session['learn_times']:
        session['learn_times'][lesson_id] += time_spent
    else:
        session['learn_times'][lesson_id] = time_spent
    
    return '', 204

@app.route('/')
def landingpage():
    return render_template('landingpage.html')

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

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Initialize session variables if they don't exist
    if 'step' not in session:
        session['step'] = 0
        session['total_spent'] = 0.0

    # Handle GET request (display current quiz step)
    if request.method == 'GET':
        if session['step'] >= len(quiz_data):
            return redirect(url_for('quiz_result'))
        current_item = quiz_data[session['step']]
        return render_template('quiz.html', current_item=current_item)

    # Handle POST request (user's selection)
    elif request.method == 'POST':
        current_step = session['step']
        current_item = quiz_data[current_step]
        result = request.form.get('result')

        # Determine if selected option is correct and get its value
        price_value = current_item['correct_price'][1] if result == 'correct' else current_item['incorrect_price'][1]

        session['total_spent'] += price_value

        session['step'] += 1

        # Check if quiz is complete
        if session['step'] >= len(quiz_data):
            return redirect(url_for('quiz_result'))

        return redirect(url_for('quiz'))

@app.route('/quiz-result')
def quiz_result():
    best_value = 32.94
    
    return render_template('quiz_result.html', 
        total_spent=session.get('total_spent', 0),
        best_value=best_value
    )

if __name__ == '__main__':
   app.run(debug = True, port=5001)