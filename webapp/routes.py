"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from webapp import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/portfolio')
def portfolio():
    """Renders the portfolio page."""
    return render_template(
        'portfolio.html',
        title='Portfolio',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/privacy')
def privacy():
    """Renders the privacy page."""
    return render_template(
        'privacy.html',
        title='Privacy',
        year=datetime.now().year,
        message='Your application description page.'
    )