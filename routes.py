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


@route('/history-page')
@view('history-page')
def roasting():
    return dict(
        title="history-page",
        year=datetime.now().year
    )


@route('/varieties-coffee')
@view('varieties-coffee')
def roasting():
    return dict(
        title="varieties-coffee",
        year=datetime.now().year
    )


@route('/how-to-choose-coffee')
@view('how-to-choose-coffee')
def roasting():
    return dict(
        title="how-to-choose-coffee",
        year=datetime.now().year
    )


@route('/making-coffee-at-home')
@view('making-coffee-at-home')
def roasting():
    return dict(
        title="making-coffee-at-home",
        year=datetime.now().year
    )


@route('/the-benefits-of-drinking-coffee')
@view('the-benefits-of-drinking-coffee')
def roasting():
    return dict(
        title="the-benefits-of-drinking-coffee",
        year=datetime.now().year
    )


@route('/coffee-and-health')
@view('coffee-and-health')
def roasting():
    return dict(
        title="coffee-and-health",
        year=datetime.now().year
    )