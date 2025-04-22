from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from urllib.parse import unquote

app = Flask(__name__)

# ROUTES

@app.route('/')
def homepage():
    return render_template('homepage.html')

 
if __name__ == '__main__':
   app.run(debug = True, port=5001)

'''
Site Colors

Main - #CF993F

Accent - #0d6efd

Light gray - #B2B6BD

Dark gray - #717884
'''