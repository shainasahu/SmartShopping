from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
from urllib.parse import unquote
from flask import session

app = Flask(__name__)

learning = [
    {
        "id": 1.1,
        "title": "Charm Pricing",
        "description": "Numbers that end in .99 feel cheaper—even though it's just a one-cent difference. Our brains focus on the first digit and think it's a better deal.",
        "image": "/static/img/1.1.png",
        "price": "$2.99! used to be $3.00"
    },
    {
        "id": 1.2,
        "title": "Phonetic Pricing",
        "description": "Prices like $27.82 (five syllables) feel cheaper than $28.16 (six syllables), even if they're basically the same.",
        "image": "/static/img/1.2.png",
        "price": "twenty-seven eighty-two vs. twenty-eight sixteen"
    },
    {
        "id": 1.3,
        "title": "Visual Compression",
        "description": "Removing the comma makes prices feel smaller and less intimidating.",
        "image": "/static/img/1.1.png",
        "price": "$1699 vs. $1,699"
    },
    {
        "id": 2.1,
        "title": "Labeling",
        "description": "Labeling using words like “high performance” or “luxury” boost perceived value—even without added features.",
        "image": "/static/img/2.1.png",
        "price": "$5.99 - Regular Cereal vs. $7.99 - Premium Cereal"
    },
    {
        "id": 2.2,
        "title": "Payment Framing",
        "description": "Showing the price in installments makes it feel more affordable, even if it's the same amount. $1/day feels cheaper than $365/year.",
        "image": "/static/img/2.2.png",
        "price": "Just $4.00! vs Just 17¢ per serving! (actually $5.00)"
    },
    {
        "id": 2.3,
        "title": "Unit Price Confusion",
        "description": "Bigger packages can seem like better value, but they often cost more per unit (like per ounce). Most people don't check the fine print and end up paying more for less.",
        "image": "/static/img/2.1.png",
        "price": "$2.99 for 12 oz vs. $4.99 for 20 oz"
    },
    {
        "id": 3.1,
        "title": "Odd Even Pricing",
        "description": "Prices like $4.97 feel cheaper than $5.00. The odd number makes it seem like you're getting a deal because we round down in our minds.",
        "image": "/static/img/3.1.png",
        "price": "$4.97 vs. $5.00"
    },
    {
        "id": 3.2,
        "title": "Visual Contrast in Sale Prices",
        "description": "Striking out the old price and using bold fonts/colors on sale prices make discounts feel more exciting than they actually are.",
        "image": "/static/img/3.2.png",
        "price": "$25 (imagine this was smaller and in red)! used to be $50"
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
        "price": "$3 vs. $6 with buy 1 get 1 FREE"
    },
    {
        "id": 4.2,
        "title": "Social Proof",
        "description": "If a product is labeled as a “Best Seller” or has hundreds of good reviews, we assume its a good choice. We tend to follow the crowd, especially when making quick decisions.",
        "image": "/static/img/4.2.png",
        "price": "$6.99 - Best Seller vs $4.99 - Regular"
    },
    {
        "id": 4.3,
        "title": "Anchoring",
        "description": "We compare prices based on the first number we see, even if it's inflated. A fake “original price” makes a regular deal feel like a huge bargain.",
        "image": "/static/img/4.1.png",
        "price": "$4.00! used to be $6.00. vs. $5.00"
    },
        {
        "id": 5.1,
        "title": "Decoy Pricing",
        "description": "Introducing a higher-priced 'decoy' option makes the mid-tier product seem more reasonable, nudging us to spend more than we planned.",
        "image": "/static/img/5.1.png",
        "price": "$3 small | $6 medium | $6.50 large (you pick medium!)"
    },
    {
        "id": 5.2,
        "title": "Price Placement",
        "description": "Prices placed to the left of the product feel cheaper than those on the right. It’s a layout trick that subtly changes our perception.",
        "image": "/static/img/5.2.png",
        "price": "Left: $4.99 | Right: $4.99 (left feels cheaper!)"
    },
    {
        "id": 5.3,
        "title": "Font & Size Psychology",
        "description": "Smaller, lighter fonts make prices seem lower—even when the number itself doesn't change. Bigger, bold fonts feel expensive.",
        "image": "/static/img/5.1.png",
        "price": "Small thin $6.99 vs. Big bold $6.99"
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
        "price": "$4.00 + FREE sticker vs. $3.99 alone"
    },
    {
        "id": 6.3,
        "title": "Misleading Size Comparisons",
        "description": "Different container shapes (taller, narrower) can make products look like they contain more, tricking you into paying more for less.",
        "image": "/static/img/6.1.png",
        "price": "$2.99 tall bottle (10 oz) vs. $2.79 short (12 oz)"
    },
    {
        "id": 7.1,
        "title": "Pre-selected Options",
        "description": "Default choices are often the most expensive ones. People tend to go with the default to save time or avoid decision fatigue.",
        "image": "/static/img/7.1.png",
        "price": "$6.99 size pre-selected (vs. $4.99 small)"
    },
    {
        "id": 7.2,
        "title": "Bundle Bias",
        "description": "Bundling items together makes you feel like you're saving, even when individual prices might be cheaper separately.",
        "image": "/static/img/7.2.png",
        "price": "$12 meal deal vs. $3 + $4 + $2 = $9"
    },
    {
        "id": 7.3,
        "title": "Time vs. Money Framing",
        "description": "Saying 'Save Time' rather than 'Save Money' appeals more emotionally, making purchases feel worthwhile beyond the price.",
        "image": "/static/img/7.1.png",
        "price": "$5.49 - Skip the wait!"
    }
]

# ROUTES

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