import json

from bottle import route, view, request, template, redirect
from datetime import datetime

from myform import load_reviews


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


def load_orders():
    with open('orders.json', 'r') as file:
        return json.load(file)


def save_orders(orders):
    with open('orders.json', 'w') as file:
        json.dump(orders, file)


@route('/pending_orders')
def pending_orders():
    orders = load_orders()
    return template('pending_orders', orders=orders)


@route('/add_order', method='POST')
def add_order():
    username = request.forms.get('username')
    deadline = request.forms.get('deadline')
    description = request.forms.get('description')
    phone = request.forms.get('phone')

    new_order = {
        'username': username,
        'deadline': deadline,
        'description': description,
        'phone': phone
    }

    orders = load_orders()
    orders.append(new_order)
    save_orders(orders)

    redirect('/pending_orders')


@route('/reviews')
@view('reviews')
def roasting():
    return dict(
        title="reviews",
        year=datetime.now().year, reviews=load_reviews()
    )
