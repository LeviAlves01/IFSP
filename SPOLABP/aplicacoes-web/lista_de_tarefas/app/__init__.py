from flask import Flask, request
import logging

#Configuração de logs
logging.basicConfig(level=logging.INFO)

# Criação da instância da aplicação
app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-forte'

# Middleware de log
@app.before_request
def log_request_info():
    app.logger.info('Requisição recebida: %s %s', request.method, request.path)

# Importa as rotas no final para evitar importação circular
from app import routes

