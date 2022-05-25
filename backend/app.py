import flask

import services


# create the application object
app = flask.Flask(__name__)


@app.route('/users/add', methods=['POST'])
def add():
    data = services.add(flask.request.get_data(as_text=True))
    services.add(user_id=data['user_id'])


@app.route('/is_valid')
def is_valid(user_id: str):
    pass


@app.route('/delete')
def delete(user_id: is_valid):
    pass


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
