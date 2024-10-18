import sqlite3

# Connecting to the Users database
con = sqlite3.connect('users.db')
# Creating a cursor
cur = con.cursor()

def get_all_users():
    '''
    Gets all the users information

    Return: all users information as a tuple
    '''
    cur.execute("SELECT * FROM Users")
    return cur.fetchall()

def add_user(nom, prenom, mdp, username):
    '''
    Adds a new user into the users database
    '''
    cur.execute(f"""
                INSERT INTO Users (nom, prenom, mdp, username)
                VALUES ({nom}, {prenom}, {mdp}, {username})
                """)
    con.commit()

con.close()
