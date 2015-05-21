from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def index():
    return 'Hello'

@app.route('/hello')
def hello_cat():
    return render_template('index.html')


@app.route('/hello/<name>')
def more_hello(name):
	return "Hello, " +  name + render_template('error.html', name = name)

@app.route('/count')
def count():
	#assignment: introducing dynamic variables via "for" loops
	#generates list of numbers into counter.html page via numbers argument, this works"""
    # num_list = range(10)   # the range(n) function generates a list:
    #                      # [1, 2, .. n]
    # return render_template('counter.html', num_list=num_list)
	

	#add-on: "Can you make it say "ah ah ah!" after each number?"
	#generates list of number with text into counter.html page via num_list
    # num_list = []   
    # for integers in range(10): 	 
    # 		num_string = str(integers) + " , ah"
    # 		num_list.append(num_string)
    # return render_template('counter.html', num_list=num_list)
    
    #add-on: "Can you use the {% if %} statement in the template to only say "ah ah ah!" sometimes?""
   #server side solution in python
    # num_list = []   
    # for integers in range(10): 	 
    # 	if integers % 2 == 0:	 
    # 		num_string = str(integers) + " , ah"
    # 		num_list.append(num_string)
    # 	else:
    # 		num_string = str(integers) + " , meow"
    # 		num_list.append(num_string)

    #python script for Jinga's client side solution
    #Can you use the {% if %} statement in the template to only say "ah ah ah!" sometimes?
    num_list = range(10)   # the range(n) function generates a list:
                         # [1, 2, .. n]
    return render_template('counter.html', num_list=num_list)

if __name__=='__main__':
    app.run(debug=True, port=8000)
