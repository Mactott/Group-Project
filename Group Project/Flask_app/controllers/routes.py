from flask import render_template, redirect, request, session, make_response, flash
from Flask_app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request')
def request():
    return render_template('modal.html')
    
@app.route('/switchR')
def switchR():
    return render_template('switchFormR.html')

@app.route('/switchS')
def switchS():
    return render_template('switchFormS.html')

@app.route('/bycity')
def city():
    return render_template('city.html')