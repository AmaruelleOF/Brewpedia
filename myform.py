from bottle import Bottle, request, template
import json
import datetime
import re
import bottle
import pdb

app = Bottle()


def is_valid_phone_number(phone_number):
    pattern = r"^(?:\+\d{1,3})?(?:\s?\(\d{3}\)\s?|\d{3}(?:-|\s)?)\d{3}(?:-|\s)?\d{4}$"
    return re.match(pattern, phone_number) is not None


@bottle.post('/home', method='POST')
def home():
    name = request.forms.get('name')
    phone = request.forms.get('phone')
    review = request.forms.get('review')

    data = {
        'name': name,
        'phone': phone,
        'review': review,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    }

    save_review(data)
    reviews = load_reviews()

    return bottle.redirect("/reviews")


def save_review(data):
    reviews = load_reviews()
    data['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    reviews.append(data)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(reviews, file, indent=4, ensure_ascii=False)


def load_reviews():
    reviews = []
    with open('data.json', 'r', encoding='utf-8') as file:
        reviews = json.load(file)
    return reviews


