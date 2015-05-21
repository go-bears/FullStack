import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from flask import Flask, render_template, request
app = Flask(__name__)

#lines 9-13 are the Oauthentication credentials to work with Google spreadsheets
#see ref: https://github.com/burnash/gspread

json_key = json.load(open('spreadsheet_credentials.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)

#opens Google Spreadsheets by the key in the URL
#see ref: https://github.com/burnash/gspread
sh = gc.open_by_key('199UgYhHYOIYRgQez85NNXEE8wGO34IhdkIejd1su1Og') 

worksheet = sh.sheet1  #stores online spreadsheet into variable to work with in python code

    #Assignment: Can you figure out from the GSpread Readme how to open the spreadsheet 
    #called "Simple Sheet" and print out the contents of Sheet1 in sentences,
     #e.g. "Black Widow loves ice cream"?

# @app.route("/") #opens flask route to index.html page, route command needs to sit on top of related function
# def index():
	#Assignment: task commented out 
	# loves = [] #list that stores the sentences "x-hero loves y-dessert"

	# for row in worksheet.get_all_values(): #for loop through opened worksheet, now stored in variable called data
	#     # do something. row is a list; try printing row, row[0], etc.
		  #print row, each row has two column elements of row[0] = superhero name and row[1] =dessert
	#     love = row[0] + " loves "  +  row[1]  #stores created sentences in a variable
	#     loves.append(love)  # appends the sentences to list outside for loop named loves 'loves'
	#return render_template("index.html", loves = loves) #renders template index.html and passes list loves to index.html via {{ loves }} 

#----------------------------------------------------------------------------------------------------------------------------------------	
    #Web App Assignment: 
    #step 1) Create a flask app with a page where the user can enter the hero name into a form
    #step 2) create a page that receives the submitted form and prints out the result
	#index.html and submit.html are interlinked with spreadsheets.py for complete solution

@app.route("/") #opens flask route to index.html page, which should be in templates folder in the same working directory as the flask app.
def index(): #function that opens the index.html page
	entered_name = request.form.get('entered_name') #stores input from form on index.html into entered_name variable
	
	return render_template("index.html", entered_name= entered_name) #renders index.html, and returns entered_name variable collected from index.html


def get_spreadsheet_data(entered_name): #function that checks input name against database of names
	
	data = get_spreadsheet_data() # local variable 'data' stores the results of the get_spreadsheet_data() to work with while within the function
	dessert = 'unknown'  # sets a default dessert value
	
	#Firstly, the "did we find [matching dessert] " way:
	for row in worksheet:  #loop through global 'data' variable in line 20, which is storing information from "Simple Sheet"
		if entered_name == row[0]: #if condition that checks entered_name from index.html to row[0], which is current list of names in [x-hero, y-dessert] speadsheet database 
			dessert = row[1]#if entered_name matched name from database spreadsheet, dessert variable stores row[1], which is the matching dessert for name in row[0]

	if dessert == 'unknown':  # we can't find hero in current database spreadsheet
	   msg = "Sorry, {} was not found".format(entered_name) # format(entered_name) insert entered_name variable into {}
	else: #we found the matching dessert!
	   msg = "{} loves {}!".format(entered_name, dessert) # format(entered_name, dessert) renders sentence "{entered_name} loves {dessert}
	
	return render_template("submit.html", msg=msg)
	

#Secondly, the "for/else" way - is pretty neat :D

	# for row in worksheet:  #initializes for loop on data variable from line 20
	#     if entered_name == row[0]: #compares entered_name to database
	#         dessert = row[1] #if entered_name is found in row[0], the matching value in row[1] is stored in variable 'dessert'
	#         msg = "{} loves {}!".format(entered_name, dessert) #formats variables into sentence for variable 'msg'
	#         break   # this is needed to trigger the 'else'
	# else:
	#     msg = "Sorry, {} was not found".format(entered_name) #formats entered_name into sentence for variable 'msg'

	# return render_template("submit.html", msg=msg) #returns submit.html with relevant msg to {{msg}} on submit.html page


@app.route("/submit", methods=['POST'])
def submit(): #function that dynamically populates submit.html

	return render_template("submit.html", entered_name=entered_name, msg=msg)


if __name__=='__main__':
    app.run(debug=True, )
