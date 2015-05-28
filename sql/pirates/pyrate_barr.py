import random
import sqlite3
from flask import Flask, render_template, request
pyrate_barr = Flask(__name__) # the name of the app's file is initiated with Flask needs to match app.run under python initialization so flask can find the app

# The goal is to make a web app that can replicate the functionality of our pirate bar from week 1, 
# but using the database (and stock levels) to serve up one drink at a time until an item is out of stock. 

# 1) Don't forget to run the import first on the command line! Otherwise you won't have the database to work with
# sqlite3 bar.db < bar_ingredients.sql

DBFILE = 'bar.db'   # database bar.db is stored in a variable for use in this python app.
# questions and answers from Week 1 challenge: Pirate Bar 


#dictionary of questions from Pirate Bartender exercise from week1.
#questions = {key = 'strong': value= "Do ye lke yer drinks strong?"}
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

#questions = {key = 'strong': value= [list of ingredients]}
cocktails = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


# Opens sql database to return database as db for use in python
def connect_to_db():
	""" Get a connection and a cursor. """
	conn = sqlite3.connect(DBFILE) #connects to database
	db = conn.cursor() # applies cursor that moves through database
	return (conn, db)  

@pyrate_barr.route('/') # routes pyrate_barr app to index.hmtl
def index():
	return render_template('index.html')
	

@pyrate_barr.route('/hello', methods=['POST']) #routes pyrate_barr to hello.html
def name():
	print request.form #applies request function imported from flask to get information <form> tag in 
	entered_name = "Mate-y" #default value for entered_name
	drink_answer = "unknown" #set default value for drink_answer

	entered_name = request.form.get('entered_name') #stores value from form named "entered_name" for use in function
	
	drink_question = random.choice(questions.values()) #selects a
	drink_greeting = "You're a true Pirate, {}! What be yer fancy?".format(entered_name)
	#return render_template('hello.html',drink_question = drink_question)
	
	

	for key, question in questions.iteritems(): #loop through dicti"Do ye like yer drinks strong?"onary of questions to select out key ('strong', 'salty' etc) and individual questions ("Do ye like yer drinks strong?") #iteritems() function searches through keys and values simlutaneosly
		drink_answer = request.form.get('drink_answer') #stores value from form name 'drink_answer' from html
		print drink_answer
		
		if drink_answer == "Yes": #if conditional for 'yes' answer from drink_question
			question == drink_question #matches if drink_question matches specific question from dictinoary "questions"
			drink_type = key   #when drink_questions matches question, drink_type will store the key for the specific question

			for taste, ingredients in cocktails.iteritems(): #starts loop through dictionary "cocktails" with iteritems() to search keys & values 
			 	if taste == drink_type: #checks for match in value stored in drink_type through keys of cocktails ('strong', 'salty', etc)
			 		recommended_drink = ingredients # sets variable to cocktails dictionary value 'ingredients', will store the list of ingredients
			 		recommended_drink = ", ".join(ingredients) # converts list of ingredients to a string separated by commas
			 		yes_drink = "Righto, Let me get you something with: ".format(entered_name) + recommended_drink #msg for selected drinkg to be returned to user 
			 		return render_template('hello.html', yes_drink=yes_drink) #returns html page with drink recommendation
		
		if drink_answer == "No": #if conditional for 'no' answer from drink_question
	 		no_drink = "Didn't like that? hmmm, let's try again?".format(entered_name) #msg for "no drink"
			return render_template('hello.html',drink_question = drink_question, no_drink=no_drink) #return new random choice question and 'no_drink' msg to user
		
	if drink_answer == "unknown": #if conditional set for default value
		return render_template('hello.html',drink_question = drink_question) #returns a new randomly chosen drink_question

		
			
@pyrate_barr.route('/update', methods=['POST'])
def ingredients(db):
	query = """SELECT * FROM ingredients;"""
	db.execute(query)
	results = db.fetchall()

	for result in results:
		if yes_drink == True:
			more_drink = 'Would you be wanting another libation?'center 
			msg = "We have {} {}s in stock.".format(result[3], result[1])

	return render_template('update.html', msg = msg) # index.htmls the form 

	print request.form
	more_drink = request.form.get('more_drink')
	remove_fr_stock = list(recommended_drink)
	print remove_fr_stock

	for item in remove_fr_stock:
		for ingredient in query:
			if item in ingredient:
				remove_item = """DELETE '{}' FROM ingredients;""".format(item)


	my_command = "UPDATE ingredients SET stock={} WHERE id={}".format(new_stock_level, item_id)
	


	conn.commit()









def main():
	(conn, db) = connect_to_db() #sets values to function connect_to_db()
	recommended_drink = name() # uses variable set in name()
	list_ingredients(db) #initializes function to use database 'db'
	update_ingredients(db) #initializes function to update database 'db'
	conn.close() #function close() closes database connection

if __name__=='__main__':
    pyrate_barr.run(debug=True, port=5000) #app.run needs to match app = Flask(__name__) so flask can find the app