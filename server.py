from flask import Flask

app  = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


@app.route('/about')
def about():
    return "This is about page"


@app.route('/blog')
def blog():
    return "This is my blog"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)



if __name__ == '__main__':
    app.run()