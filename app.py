from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello python virtualments"

@app.route('/test')
def test():
    return "hello python test"

if __name__ == '__main__':
    app.run(debug=True)