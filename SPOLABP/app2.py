from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/formulario_1', methods=['GET', 'POST'])
def formulario_1():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        return redirect(url_for('formulario_2', nome=nome, email=email))
    return render_template('formulario_1.html')

@app.route('/formulario_2', methods=['GET'])
def formulario_2():
    nome = request.args.get('nome')
    email = request.args.get('email')
    return render_template('formulario_2.html', nome=nome, email=email)

if __name__ == '__main__':
    app.run(debug=True)