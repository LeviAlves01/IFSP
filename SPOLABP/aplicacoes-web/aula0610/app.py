from flask import Flask, request, render_template, abort
import math

app = Flask(__name__)

PRODUTOS = [

    {"id": 1, "nome": "Notebook Gamer X", "preco": 5200.00},
    {"id": 2, "nome": "Mouse sem Fio", "preco": 150.00},
    {"id": 3, "nome": "Teclado Mecânico RGB", "preco": 350.00},
    {"id": 4, "nome": "Monitor de 27 polegadas", "preco": 1800.00},
    {"id": 5, "nome": "Celular de 128 GB", "preco": 1800.00},
    {"id": 6, "nome": "Mouse", "preco": 140.00},
    {"id": 7, "nome": "Playstation 4", "preco": 2000.00},
    {"id": 8, "nome": "Celular 256GB", "preco": 2100.00},
    {"id": 9, "nome": "Camiseta tamanho M", "preco": 70.00},
    {"id": 10, "nome": "Calça Jeans tamanho G", "preco": 250.00},

    ]

@app.route('/produtos')
def listar_produtos():
    return render_template('produtos.html', produtos=PRODUTOS)

@app.route('/produtos-paginados')
def listar_produtos_paginados():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    start = (page - 1) * per_page
    end = start + per_page
    total_pages = math.ceil(len(PRODUTOS)/per_page)

    produtos_da_pagina = PRODUTOS[start:end]

    return render_template('produtos_paginados.html', produtos=produtos_da_pagina, page=page, total_pages=total_pages)


@app.route('/produto/<int;produto_id>')
def detalhe_produto():
    produto_encontrado = None

    for produto in PRODUTOS:
        if produto("id") == produto_id:
            produto_encontrado = produto
            break

        if produto_encontrado is None:
            abort(404)

        return render_template('detalhe_produto.html', produto=produto_encontrado)

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def pagina_nao_encontrada(error):
    return render_template('403.html'), 403

@app.errorhandler(401)
def pagina_nao_encontrada(error):
    return render_template('401.html'), 401

from flask import request, jsonify

@app.route('/api/buscar-produto', methods=['POST'])
def buscar_produto():
    dados = request.get_json()
    nome_produto = dados.get('nome',).lower()

    resultado = [p for p in PRODUTOS if nome_produto in p['nome'].lower()]
    return jsonify({'produtos_encontrados': resultado})

if __name__ == '__main__':
    app.run(debug=True)