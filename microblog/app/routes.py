from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Freddie'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in London'
        },
        {
            'author': {'username': 'Steven'},
            'body': 'Matrix 4 review'
        }
            
    ]
    return render_template('index.html', title="Microblog", user=user, posts=posts)
