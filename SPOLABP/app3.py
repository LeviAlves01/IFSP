from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/user/<username>')

def profile(username):
    return render_template('profile.html', user=username)

#Def login():
#  usernames = []
#    userpasswords = []
#
 #   username = request.form['username']
  #  userpassword = request.form['password']
#
 #   usernames.append(username)
  #  userpasswords.append(userpassword)
#
 #   session['username'] = username
#
 #   produtos = ["Maça", "Banana", "Laranja"]
#
 #   logado = True
#
 #   return render_template("login.html", produtos=produtos, logado=logado)

@app.route('/logar', methods=['POST'])

def validar_login():
    usernames = ['levi123']
    userpasswords = ['1234']

    username = request.form['username']
    userpassword = request.form['password']

    for user in usernames:
        for user in userpasswords:

            if (username == usernames) and (userpassword == userpasswords):
                logado = True
                return render_template("home.html", produtos=produtos, logado=logado)
            else:
                logado = False
                return redirect(url_for('profile'))


@app.route('/home')

def home():

    produtos = ["Maça", "Banana", "Laranja"]

    logado = True

    return render_template("home.html", produtos=produtos, logado=logado)

if __name__ == '__main__':

    app.run(debug=True)