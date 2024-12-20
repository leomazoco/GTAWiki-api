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

                veiculo_id = request.args.get('id', type=int)

                if veiculo_id:

                    veiculo = Veiculo.query.get(veiculo_id)

                    if veiculo:
                        return {
                            'id': veiculo.id,
                            'modelo': veiculo.modelo,
                            'marca': veiculo.marca,
                            'tipo': veiculo.tipo,
                            'capacidade': veiculo.capacidade,
                            'veiculo': veiculo.veiculo,
                            'preco': float(veiculo.preco),
                            'imagem': veiculo.imagem,
                            'jogo': veiculo.jogo,
                            'descricao': veiculo.descricao
                        }, 200
                    else:
                        return {'message': 'Veículo não encontrado'}, 404

                else:

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
                                'veiculo': veiculo.veiculo,
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

    @staticmethod
    def post():

        token_recebido = request.headers.get('Authorization')

        token_enviado = Token.query.with_entities(Token.token,
                                                  Token.valid).filter_by(token=token_recebido).first()

        if token_enviado:
            token_retornado, valid = token_enviado
            if valid:
                payload = request.get_json()

                veiculo = Veiculo(
                    modelo = payload['modelo'],
                    marca = payload['marca'],
                    tipo = payload['tipo'],
                    capacidade = payload['capacidade'],
                    veiculo = payload['veiculo'],
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

    @staticmethod
    def put():

        token_recebido = request.headers.get('Authorization')

        token_enviado = Token.query.with_entities(Token.token,
                                                  Token.valid).filter_by(token=token_recebido).first()

        if token_enviado:
            token_retornado, valid = token_enviado
            if valid:
                payload = request.get_json()

                id_veiculo = payload['id']
                veiculo = Veiculo.query.filter_by(id = id_veiculo).first()

                if veiculo:

                    veiculo.modelo = payload['modelo']
                    veiculo.marca = payload['marca'],
                    veiculo.tipo = payload['tipo'],
                    veiculo.capacidade = payload['capacidade'],
                    veiculo.veiculo = payload['veiculo'],
                    veiculo.preco = payload['preco'],
                    veiculo.imagem = payload['imagem'],
                    veiculo.jogo = payload['jogo'],
                    veiculo.descricao = payload['descricao']

                    try:
                        db.session.commit()
                        return {'message': 'Veículo atualizado com sucesso'}
                    except Exception as e:
                        return {
                            'message': 'Erro ao atualizar veículo',
                            'detalhes': str(e)
                        }

    @staticmethod
    def delete():

        token_recebido = request.headers.get('Authorization')

        token_enviado = Token.query.with_entities(Token.token,
                                                  Token.valid).filter_by(token=token_recebido).first()

        if token_enviado:
            token_retornado, valid = token_enviado
            if valid:
                veiculo_id = request.args.get('id', type=int)

                if not veiculo_id:
                    return {'message': 'É necessário passar o ID do veículo'}
                else:
                    veiculo = Veiculo.query.get(veiculo_id)

                    if veiculo:
                        try:
                            db.session.delete(veiculo)
                            db.session.commit()

                            return {'message': 'Veículo excluido com sucesso'}
                        except Exception as e:
                            return {
                                'message': 'Erro ao deletar o veículo',
                                'detalhes': str(e)
                            }