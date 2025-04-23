from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from urllib.parse import unquote

app = Flask(__name__)

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

 
if __name__ == '__main__':
   app.run(debug = True, port=5001)

'''
Site Colors

Main - ?

Accent - ?

Light gray - #B2B6BD

Dark gray - #717884
'''