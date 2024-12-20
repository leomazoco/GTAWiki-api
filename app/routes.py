import time

from app import app, api
from app.resources.veiculos import VeiculoResource

from flask import jsonify, request

# routa veículos
api.add_resource(VeiculoResource, '/veiculos')

@app.after_request
def after_request(response):
    # Obtenha a origem da solicitação (ou '*')
    origin = request.headers.get('Origin', '*')

    # Defina o cabeçalho Access-Control-Allow-Origin para a origem da solicitação
    response.headers['Access-Control-Allow-Origin'] = origin

    # Defina outros cabeçalhos e métodos permitidos
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'

    return response

@app.route('/', methods=['GET'])
def index():
    return f"Server time: {time.time()}", 200