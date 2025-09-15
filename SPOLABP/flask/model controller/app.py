from flask import Flask, render_template, request, redirect, url_for
from models import UsuarioModel

app = Flask(__name__)
usuario_model = UsuarioModel()

@app.route('/usuarios')
def listar_usuarios():
    usuarios = usuario_model.get_todos()
    return render_template('usuarios.html', lista_de_usuarios=usuarios)

@app.route('/login')
def pagina_inicial():
    return render_template('login.html')

@app.route('/login/novo', methods=['POST'])
def adicionar_usuario():
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]
    usuario_model.salvar(nome, email, senha)
    return redirect(url_for("listar_usuarios"))

@app.route('/usuarios/remover', methods=['POST'])
def remover_usuario():
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]
    usuario_model.remover(nome, email, senha)
    return redirect(url_for("pagina_inicial"))

if __name__ == '__main__':
    app.run(debug=True)