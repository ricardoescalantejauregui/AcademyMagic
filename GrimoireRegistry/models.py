from . import db
from datetime import datetime


class Estudiante(db.Model):
    """
    The Estudiante model class encapsulates data and features related to a Student object in the system.

    Attributes:
       id: A unique integer value that identifies the student.
       nombre: A string representing student's first name.
       apellido: A string representing student's last name.
       identificacion: A unique string used for student's identification.
       edad: An integer indicating the age of the student.
       afinidad_magica: A string representing student's magical affinity.
       grimorio_id: A foreign key creating a link between student and their grimorio.
       fecha_creacion: A datetime object marking the creation date of the student's data.
    """

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellido = db.Column(db.String(20), nullable=False)
    identificacion = db.Column(db.String(10), nullable=False, unique=True)
    edad = db.Column(db.Integer, nullable=False)
    afinidad_magica = db.Column(db.String(10), nullable=False)
    grimorio_id = db.Column(db.Integer, db.ForeignKey('grimorio.id'))
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        """
        The to_dict method converts the Estudiante object into a Python dictionary.

        Returns:
           A dictionary that represents the Estudiante object's attributes.
        """
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'identificacion': self.identificacion,
            'edad': self.edad,
            'afinidad_magica': self.afinidad_magica,
            'grimorio': self.grimorio.to_dict() if self.grimorio else None,
            'fecha_creacion': self.fecha_creacion
        }


class Grimorio(db.Model):
    """
    The Grimorio model class encapsulates data and features related to a Grimorio object in the system.

    Attributes:
       id: A unique integer value that identifies the Grimorio.
       tipo_trebol: A string representing the type of the Grimorio.
       rareza: A string representing the rarity of the Grimorio.
       estudiantes: A list of Estudiante objects related to this Grimorio.
    """

    id = db.Column(db.Integer, primary_key=True)
    tipo_trebol = db.Column(db.String(20), nullable=False)  # Aumentado de 10 a 20
    rareza = db.Column(db.String(20), nullable=False)  # Aumentado de 10 a 20
    estudiantes = db.relationship('Estudiante', backref='grimorio', lazy=True)

    def to_dict(self):
        """
        The to_dict method converts the Grimorio object into a Python dictionary.

        Returns:
           A dictionary that represents the Grimorio object's attributes.
        """
        return {
            'id': self.id,
            'tipo_trebol': self.tipo_trebol,
            'rareza': self.rareza
        }
