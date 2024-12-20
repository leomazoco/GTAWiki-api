from flask import request
from flask_restful import Resource, reqparse

from app import db
from app.models.token import Token
from app.models.veiculo import Veiculo

class VeiculoResource(Resource):

    @staticmethod
    def get():

        token_recebido = request.headers.get('Authorization')

        token_enviado = Token.query.with_entities(Token.token,
                                                  Token.valid).filter_by(token = token_recebido).first()

        if token_enviado:
            token_retornado, valid = token_enviado
            if valid:
                veiculos = Veiculo.query.all()
                if veiculos:

                    lista_veiculos = []
                    for veiculo in veiculos:
                        lista_veiculos.append({
                            'id': veiculo.id,
                            'modelo': veiculo.modelo,
                            'marca': veiculo.marca,
                            'tipo': veiculo.tipo,
                            'capacidade': veiculo.capacidade,
                            'preco': float(veiculo.preco),
                            'imagem': veiculo.imagem,
                            'jogo': veiculo.jogo,
                            'descricao': veiculo.descricao
                        })

                    return {'Veículos': lista_veiculos}, 200
                else:
                    return {'message': 'Não foram encontrados veiculos'}
            else:
                return {'message': 'O token é inválido'}
        else:
            return {'message': 'O token não foi encontrado'}

    def post(self):

        token_recebido = request.headers.get('Authorization')

        token_enviado = Token.query.with_entities(Token.token,
                                                  Token.valid).filter_by(token=token_recebido).first()

        if token_enviado:
            token_retornado, valid = token_enviado
            if valid:
                payload = request.get_json()

                veiculo = Veiculo(
                    marca = payload['marca'],
                    tipo = payload['tipo'],
                    capacidade = payload['capacidade'],
                    preco = payload['preco'],
                    imagem = payload['imagem'],
                    jogo = payload['jogo'],
                    descricao = payload['descricao']
                )

                try:
                    db.session.add(veiculo)
                    db.session.commit()

                    return {'message': 'Veículo cadastrado com sucesso'}, 201

                except Exception as e:
                    db.session.rollback()

                    return {
                        'message': 'Erro ao cadastrar veículo',
                        'details': str(e)
                    }, 500
            else:
                return {'message': 'O token enviado não é válido'}, 500

        else:
            return {'message': 'O token de autenticação não encontrado'}