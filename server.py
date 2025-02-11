from flask import Flask, render_template

app  = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


@app.route('/about')
def about():
    return "This is about page"


@app.route('/blog')
def blog():
    return render_template('blog.html', author = 'Bob', sunny=True)


@app.route('/blog/<blog_id>')
def blogpost(blog_id):
    return "This is a blogpost number " + str(blog_id)
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)



if __name__ == '__main__':
    app.run()