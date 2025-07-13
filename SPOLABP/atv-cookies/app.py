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
            resposta = make_response(redirect(url_for(request.cookies.get('redirect_depois_login', 'bemvindo'))))
            resposta.set_cookie('username', usuario, max_age=60*10)
            return resposta
        else:
            mensagem = "Usuário ou senha inválidos. Tente novamente."
    
    return render_template('login.html', error=mensagem)

@app.route('/bemvindo', methods=['GET', 'POST'])
def bemvindo():
    username = request.cookies.get('username')
    tema = request.cookies.get('tema', 'light')

    if not username:
        return redirect(url_for('login'))
    
    visitas = int(request.cookies.get('visitas', 0)) + 1
    resposta = make_response(render_template(
        'bemvindo.html',
        user=username,
        visitas=visitas,
        tema=request.cookies.get('tema', 'light')
    ))
    resposta.set_cookie('visitas', str(visitas), max_age=60*30)
    return resposta

@app.route('/logout')
def logout():
    resposta = make_response(redirect(url_for('login')))
    ultima_categoria = request.cookies.get('ultima_categoria', 'noticias')

    if not ultima_categoria:
        ultima_categoria = url_for('noticias')

    resposta.set_cookie('username', '', expires=0)
    resposta.set_cookie('redirect_depois_login', ultima_categoria, max_age=60*5)
    resposta.set_cookie('visitas', '', expires=0)
    return resposta

@app.route('/noticias')
def noticias():
    username = request.cookies.get('username')
    tema = request.cookies.get('tema', 'light')
    ultima_categoria = request.cookies.get('ultima_categoria', 'esportes')  # Pega a última categoria
    
    if not username:
        return redirect(url_for('login'))
    
    resposta = make_response(render_template(
        'noticias.html',
        user=username,
        tema=tema,
        ultima_categoria=ultima_categoria 
    ))
    return resposta


@app.route('/categorias')
def categorias():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    
    return render_template('noticias.html', user=username, tema=request.cookies.get('tema', 'light'))

@app.route('/esportes')
def esportes():
    username = request.cookies.get('username')
    tema = request.cookies.get('tema', 'light')

    if not username:
        return redirect(url_for('login'))
    
    resposta = make_response(render_template('esportes.html', user=username, tema=tema))
    resposta.set_cookie('ultima_categoria', 'esportes', max_age=60*60*24)
    return resposta

@app.route('/entretenimento')
def entretenimento():
    username = request.cookies.get('username')
    tema = request.cookies.get('tema', 'light')

    if not username:
        return redirect(url_for('login'))
    
    resposta = make_response(render_template('entretenimento.html', user=username, tema=tema))
    resposta.set_cookie('ultima_categoria', 'entretenimento', max_age=60*60*24)
    return resposta

@app.route('/lazer')
def lazer():
    username = request.cookies.get('username')
    tema = request.cookies.get('tema', 'light')

    if not username:
        return redirect(url_for('login'))
    
    resposta = make_response(render_template('esportes.html', user=username, tema=tema))
    resposta.set_cookie('ultima_categoria', 'lazer', max_age=60*60*24)
    return resposta

@app.route('/mudartema', methods=['POST'])
def mudartema():
    pagina_anterior = request.referrer or url_for('bemvindo')
    resposta = make_response(redirect(pagina_anterior))
    
    tema_atual = request.cookies.get('tema', 'light')
    novo_tema = 'dark' if tema_atual == 'light' else 'light'
    resposta.set_cookie('tema', novo_tema, max_age=30*60)
    
    return resposta

if __name__ == '__main__':
    app.run(debug=True)