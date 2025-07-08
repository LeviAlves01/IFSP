from flask import Flask, render_template, request, redirect, url_for, make_response, session

app = Flask(__name__)

usuario_cadastrado = "ana"
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
            mensagem = "Usuário ou senha inválidos. Tente novamente."
    
    return render_template('login.html', error=mensagem)

@app.route('/bemvindo', methods=['GET', 'POST'])
def bemvindo():
    
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1

    username = request.cookies.get('username')

    if not username:
        return redirect(url_for('login'))
    
    return render_template('index.html', user=username, counter=str(session['counter']))

@app.route('/logout')
def logout():
    resposta = make_response(redirect(url_for('login')))

    resposta.set_cookie('username', '', expires=0)

    return resposta

@app.route('/noticias')
def noticias():
    global bemvindo
    bemvindo = False
    username = request.cookies.get('username')

    if not username:
        return redirect(url_for('login'))
    
    return render_template('noticias.html', user=username)

@app.route('/esportes')
def esportes():
    global bemvindo
    bemvindo = False
    username = request.cookies.get('username')

    if not username:
        return redirect(url_for('login'))
    
    return render_template('esportes.html', user=username)

@app.route('/entretenimento')
def entertainment():
    global bemvindo
    bemvindo = False
    username = request.cookies.get('username')

    if not username:
        return redirect(url_for('login'))
    
    return render_template('entretenimento.html', user=username)

@app.route('/lazer')
def lazer():
    global bemvindo
    bemvindo = False
    username = request.cookies.get('username')

    if not username:
        return redirect(url_for('login'))
    
    return render_template('lazer.html', user=username)

if __name__ == '__main__':
    app.run(debug=True)