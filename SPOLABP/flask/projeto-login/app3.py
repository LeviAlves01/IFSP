from flask import Flask, session, redirect, url_for, request, render_template, flash

app = Flask(__name__)

@app.route('/user/<username>')
def profile(username):
    return render_template('profile.html', user=username)

@app.route('/logar', methods=['GET', 'POST'])
def validar_login():
    if request.method == 'POST':
        usernames = ['levi123']
        userpasswords = ['1234']

        username = request.form['username']
        userpassword = request.form['password']

        if username in usernames and userpassword in userpasswords:
            return redirect(url_for('profile', logado=True, username=username))
        else:
            return redirect(url_for('validar_login', mensagem="Usuário ou senha inválidos"))

    return render_template('login.html')

@app.route('/home')
def home():
    produtos = ["Maça", "Banana", "Laranja"]
    logado = True
    return render_template("home.html", produtos=produtos, logado=logado)

if __name__ == '__main__':
    app.run(debug=True)