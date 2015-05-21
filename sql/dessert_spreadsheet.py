from flask import Flask, render_template, request
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
app = Flask(__name__)


# function opens Google Spreadsheets by the name of spreadsheet in the URL
#loads authentication requirements for google spreadsheets, 
#opens google spreadsheets as allvall for use in this app
#see ref: https://github.com/burnash/gspread
def get_spreadsheet_data():
    json_key = json.load(open('spreadsheet_credentials.json'))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
    gc = gspread.authorize(credentials)

    sh = gc.open("Simple Sheet")
    sh = sh.sheet1
    allval = sh.get_all_values()
    return allval

@app.route("/") #flask opens route to index.html
def index():
    return render_template("index.html")


@app.route("/submit", methods=['POST'])
def submit():
    print request.form   #prints what is entered on form from index.html
    entered_name=request.form.get('entered_name') #sets variable entered_name to information from form name='entered_name' from index.html
    data = get_spreadsheet_data() #calls data from get_spreadsheet_data() for use in submit()
    dessert = "unknown"  #default value for dessert
    for row in data: #loops through data
        entered_name = entered_name.lower() #converts entered_name to lowercase to ensure matching strings
        database_name = row[0].lower() #converts row[0] to name variable and to lowercase

        if database_name == entered_name:  #compares value of 'entered_name' against row[0] = the names in the data
            dessert = row[1]  #stores the  matching dessert in variable
            msg = "{} loves {}!".format(entered_name, dessert) # format(entered_name, dessert) renders sentence "{entered_name} loves {dessert}
            return render_template("submit.html", entered_name=entered_name, dessert=dessert, msg=msg)

            if dessert == "unknown"  : #if name  wasn't found in the database
                msg = "Sorry, {} was not found in our database".format(entered_name) # format(entered_name) insert entered_name variable into {}
                return render_template("submit.html", entered_name=entered_name, dessert=dessert, msg=msg)        
        
        else: #error condition case, returns index.html with an error message
            error = "Let's try that again. What's your name again?"
            return render_template("index.html", error = error) 


if __name__=='__main__':
    app.run(debug=True)