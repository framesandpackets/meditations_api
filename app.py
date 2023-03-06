from flask import Flask, jsonify
from api_data import meditations
import json
import random

app = Flask(__name__)


def get_random_book():
    data = json.loads(meditations)
    books = []
    for key in data.keys():
        books.append(key)
    random_book = books[random.randint(0,len(books)-1)]
    return random_book

def get_random_passage():
    data = json.loads(meditations)
    passages = []
    for passage in data[get_random_book()]:
        passages.append(passage["passage"])
    return passages[random.randint(0,len(passages)-1)]



@app.route('/')
def home():
    return ""

@app.route('/meditations/full_book')
def full_book():
    body = json.loads(meditations)
    return jsonify(body)

@app.route('/meditations/book_<book_num>')
def book_select(book_num):
    num_int = int(book_num)
    body = json.loads(meditations)
    if num_int == 1:
        return body["book_one"]
    if num_int == 2:
        return body["book_two"]
    if num_int == 3:
        return body["book_three"]
    if num_int == 4:
        return body["book_four"]
    if num_int == 5:
        return body["book_five"]
    if num_int == 6:
        return body["book_six"]
    if num_int == 7:
        return body["book_seven"]
    if num_int == 8:
        return body["book_eight"]
    if num_int == 9:
        return body["book_nine"]
    if num_int == 10:
        return body["book_ten"]
    if num_int == 11:
        return body["book_eleven"]
    if num_int == 12:
        return body["book_twelve"]
    else:
        return "please enter book_1 - book_12"


@app.route('/meditations/random_passage')
def random_passage():
    passage = get_random_passage()
    return {"random_passage": passage}



if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
