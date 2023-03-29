from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    return dict(
        title='Contact',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    return dict(
        title='About',
        year=datetime.now().year
    )


@route('/articles')
@view('articles')
def articles():
    return dict(
        title='Articles',
        year=datetime.now().year
    )


@route('/brewing')
@view('brewing')
def brewing():
    return dict(
        title="Brewing",
        year=datetime.now().year
    )


@route('/beans')
@view('beans')
def beans():
    return dict(
        title="beans",
        year=datetime.now().year
    )


@route('/roasting')
@view('roasting')
def roasting():
    return dict(
        title="roasting",
        year=datetime.now().year
    )