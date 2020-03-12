"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from webapp import app
from webapp.api.srd_todoist import get_tasks

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

@app.route('/todo')
def todo():
    """Renders the privacy page."""
    return render_template(
        'todo.html',
        title='Tech To Do List',
        year=datetime.now().year,
        message='My Tech To Do List Page'
    )

# WEB APIs
@app.route('/gettasks')
def gettasks():
    """Returns todoist tech project tasks."""
    return get_tasks()