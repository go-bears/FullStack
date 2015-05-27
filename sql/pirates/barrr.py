import sqlite3

# Don't forget to run the import first.
# sqlite3 bar.db < bar_ingredients.sql

DBFILE = 'bar.db'

def connect_to_db():
    """ Get a connection and a cursor. """
    conn = sqlite3.connect(DBFILE)
    db = conn.cursor()
    return (conn, db)


def list_ingredients(db):
    query = """SELECT * FROM ingredients;"""
    db.execute(query)
    results = db.fetchall()
    for result in results:
        print "There are {} {}s in stock.".format(result[3], result[1])
        # Why [1] and [3]?

def update_ingredients(db):
    my_command = "UPDATE ingredients SET stock={} WHERE id={}".format(new_stock_level, item_id)

def main():
    (conn, db) = connect_to_db()
    list_ingredients(db)
    conn.close()


if __name__=="__main__":
    main()