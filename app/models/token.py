from app import db

class Token(db.Model):
    __tablename__ = 'token_api'

    token = db.Column(db.String(200), primary_key=True)
    valid = db.Column(db.Boolean)

    __table_args__ = {'schema': 'gtawiki'}