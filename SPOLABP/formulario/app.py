from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

usuario_cadastrado = "luis"
senha_cadastrada = "123"

@app.route('/', methods=['GET', 'POST'])
def login():
    mensagem = ""

    if request.method == "POST":
        mensagem = 'Logado com sucesso'
        usuario = request.form['username']
        senha = request.form['password']
        
        if usuario == usuario_cadastrado and senha == senha_cadastrada:
            resposta = make_response(redirect(url_for('bemvindo')))
            resposta.set_cookie('username', usuario, max_age=60*10)

            return resposta
        else:
            mensagem = "Uusário ou senha inválidos. Tente novamente."
    
    return render_template('login.html', error=mensagem)

@app.route('/bemvindo')
def bemvindo():
    username = request.cookies.get('username')

    if not username:
        return redirect(url_for('login'))
    
    return render_template('bemvindo.html', user=username)

@app.route('/logout')
def logout():
    resposta = make_response(redirect(url_for('login')))

    resposta.set_cookie('username', '', expires=0)

    return resposta

if __name__ == '__main__':
    app.run(debug=True)