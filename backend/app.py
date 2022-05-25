import flask
import json

import services


# create the application object
app = flask.Flask(__name__)


@app.route('/users/add', methods=['POST'])
def add():
    data = json.loads(flask.request.get_data(as_text=True))
    services.add(user_id=data['user_id'])
    return "{}", 200


@app.route('/users/is_valid/<user_id>', methods=['GET'])
def is_valid(user_id: str):
    _is_valid = services.is_valid(user_id=user_id)
    return json.dumps({"is_valid": _is_valid})


@app.route('/users/delete/<user_id>', methods=['DELETE'])
def delete(user_id: str):
    services.delete(user_id=user_id)
    return "{}", 200


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
