import json

from bottle import route, view, request, template, redirect
from datetime import datetime
from regex import match, regex
from orders import *
from myform import load_reviews
from datetime import *

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
    # Получаем данные из формы
    username = request.forms.get('username')
    deadline = request.forms.get('deadline')
    description = request.forms.get('description')
    phone = request.forms.get('phone')

    # Несколько проверок на разные поля
    if not check_name(username):
        return {'status': 'Invalid username'}

    if not check_phone(phone):
        return {'status': 'Invalid phone'}

    if not check_date(deadline):
        return {'status': 'Invalid deadline'}

    # Если все хорошо - формируем новый заказ
    new_order = {
        'username': username,
        'deadline': deadline,
        'description': description,
        'phone': phone
    }

    # Добавление и запись в файл
    orders = load_orders()
    orders.append(new_order)
    save_orders(orders)

    redirect('/pending_orders')
    return {'status': 'All ok'}


@route('/reviews')
@view('reviews')
def roasting():
    return dict(
        title="reviews",
        year=datetime.now().year, reviews=load_reviews()
    )


# Static fake data
active_users = [
    {
        'username': 'user1',
        'date_registered': '2021-09-01',
        'last_active': '2021-09-30'
    },
    {
        'username': 'user2',
        'date_registered': '2021-09-05',
        'last_active': '2021-09-28'
    },
]


@route('/active_users')
def index():
    return template('active_users', users=active_users)


@route('/add_user', method='POST')
def add_user():
    username = request.forms.get('username')
    date_registered = request.forms.get('date_registered')
    last_active = request.forms.get('last_active')

    active_users.append({
        'username': username,
        'date_registered': date_registered,
        'last_active': last_active
    })

    return template('active_users', users=active_users)
