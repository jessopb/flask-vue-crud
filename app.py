from flask import Flask, jsonify, request
from flask_cors import CORS # so we can CORS(app)

DEBUG = True

app = Flask(__name__) # make an app
app.config.from_object(__name__) # call config.from_object()

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True,
    },
    {
        'title': 'Harry Potter and the Methods of Rationality',
        'author': 'J.K. Rowling',
        'read': False,
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True,
    },
]


# enable CORS globally: research specifics
CORS(app)

# sanity check route

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
