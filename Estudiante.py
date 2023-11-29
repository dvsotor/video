from db import db


class Estudiante(db.Model):
    __tablename__="Estudiante"

    id=db.Column(db.Integer, primary_key=True)

    nombre=db.Column(db.String(50))
    email=db.Column(db.String(80))
    codigo=db.Column(db.String(15))


    def __init__(self, nombre, email, codigo):
        self.nombre=nombre
        self.email=email
        self.codigo=codigo
