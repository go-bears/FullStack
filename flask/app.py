from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def index():
    return 'Hello'

@app.route('/hello')
def hello_cat():
    return render_template('kittens.html')


@app.route('/hello/<name>')
def more_hello(name):
	return "Hello, " + name
	return render_template('error.html')

@app.route('/count')
def count():
    numbers = range(10)   # the range(n) function generates a list:
                         # [1, 2, .. n]
    return render_template('counter.html', numbers=numbers)


if __name__=='__main__':
    app.run(debug=True)
