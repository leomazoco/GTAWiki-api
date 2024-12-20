from app import db

class Veiculo(db.Model):
    __tablename__ = 'aeronaves'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    modelo = db.Column(db.String(80), nullable = False)
    marca = db.Column(db.String(80), nullable = False)
    tipo = db.Column(db.String(80), nullable = False)
    capacidade = db.Column(db.String(80), nullable = False)
    tipo_veiculo = db.Column(db.String(50), nullable = False)
    preco = db.Column(db.Double(10, 2))
    imagem = db.Column(db.String(200),)
    jogo = db.Column(db.String(80), nullable = False)
    descricao = db.Column(db.Text)

    __table_args__ = {'schema': 'gtawiki'}