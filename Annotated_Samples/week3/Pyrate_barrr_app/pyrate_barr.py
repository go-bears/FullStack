import sqlite3
from flask import Flask, render_template

pyrate_barr = Flask(__name__) # the name of the app's file is initiated with Flask

# Don't forget to run the import first on the command line!
# sqlite3 bar.db < bar_ingredients.sql

DBFILE = 'bar.db'   #database bar.db is stored in a variable for use in this python app.

# Opens sql database to return database as db for use in python
def connect_to_db():
	""" Get a connection and a cursor. """
	conn = sqlite3.connect(DBFILE) #connects to database
	db = conn.cursor()
	return (conn, db)

@pyrate_barr.route('/') #routes pyrate_barr app to index.hmtl
def index():
	return render_template('index.html')

def list_ingredients(db):
	query = """SELECT * FROM ingredients;"""
	db.execute(query)
	results = db.fetchall()
	for result in results:
		print "There are {} {}s in stock.".format(result[3], result[1])


@pyrate_barr.route('/drink')
def update_ingredients(db):
	results = db.fetchall()
	my_command = "UPDATE ingredients SET stock={} WHERE id={}".format(new_stock_level, item_id)
	conn.commit()


def main():
	(conn, db) = connect_to_db()
	list_ingredients(db)
	update_ingredients(db)
	conn.close()

if __name__=='__main__':
    pyrate_barr.run(debug=True, port=8000)