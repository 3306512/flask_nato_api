from flask import Flask, jsonify, abort
from napi import get_and_give_response

app = Flask('__filename__')


@app.route('/<string:date>')
def index(date):
    to_return = get_and_give_response(date)
    print(to_return)
    if to_return:
        return jsonify(to_return)


if __name__ == "__main__":
    app.run()

