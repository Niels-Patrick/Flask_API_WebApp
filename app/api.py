import flask
from flask import request, jsonify

app = flask.Flask(__name__) # Creating flask object
app.config['DEBUG'] = True # Launching the debugger

# Initializing a users list
users = [
    {
        'id': 1,
        'nom': 'Stormcloak',
        'prenom': 'Ulfric'
    },
    {
        'id': 2,
        'nom': 'Freeman',
        'prenom': 'Gordon'
    },
    {
        'id': 3,
        'nom': 'Croft',
        'prenom': 'Lara'
    }
]

@ app. route("/", methods=['GET'])
def get_all_users():
    '''
    Gets all users in the list

    Return: the list of users in JSON format
    '''
    return jsonify(users)

@ app. route("/add_user", methods=['POST'])
def add_user():
    '''
    Adds a new user in the users list

    Return: a message to inform that the new user has been added successfully
    '''
    new_user = {
                'id': [request.args.get('id', 0, type=int)],
                'nom': [request.args.get('nom', "", type=str)],
                'prenom': [request.args.get('prenom', "", type=str)]
                }

    users.append(new_user)

    return jsonify({'message': 'User added successfully!', 'user': new_user})

app.run(host='0.0.0.0', port=5000)
