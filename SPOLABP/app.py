from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/bemvindo/<nome>')
def bemvindo(nome):
    return render_template('bemvindo.html', usuario=nome)

# @app.route('/') # Barrinha significa raiz
# def ola_mundo():
#    return 'Olá, Mundo com Flask!'

if __name__ == '__main__':
    app.run(debug=True)