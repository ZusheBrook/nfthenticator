from flask import Flask, render_template

# create the application object
app = Flask(__name__)
app.root_path = '/users'


@app.route('/add')
def add():
    return render_template('static.html')  # render a template


@app.route('/get')
def get():
    return "Hello, World!" 


@app.route('/list')
def get_all():
    return []


@app.route('/delete')
def delete():
    pass


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
