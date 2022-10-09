from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "hello python virtualments"

@app.route('/test')
def test():
    return "hello python test1"

@app.route('/<name>')
def name(name):
    return f"hello python {escape(name)}"

@app.route('/demo')
def demo():
    return render_template('demo.html')

if __name__ == '__main__':
    app.run(debug=True)