from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) # Creating flask object
app.config['DEBUG'] = True # Launching the debugger

# Initializing a users list
users_list = [
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

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/users_list")
def users():
    return render_template('users_list.html', users=users_list)

@app.route("/add_user", methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']

        users_list.append(
            {
                'id': users_list[-1]['id'] + 1,
                'nom': nom,
                'prenom': prenom
            }
        )

        return redirect(url_for('index'))

    return render_template('add_user.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

app.run(host='0.0.0.0', port=8000)
