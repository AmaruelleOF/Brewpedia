from bottle import Bottle, request, template
import json
import datetime
import re
import bottle
import pdb

app = Bottle()


@bottle.post('/home', method='POST')
def home():
    name = request.forms.get('name')
    email = request.forms.get('email')
    review = request.forms.get('review')

    data = {
        'name': name,
        'email': email,
        'review': review
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


