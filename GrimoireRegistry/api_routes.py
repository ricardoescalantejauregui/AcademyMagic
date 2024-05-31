from flask import Blueprint, request, jsonify
from .models import db, Estudiante, Grimorio
from .utils import validar_solicitud, asignar_grimorio
from flasgger import swag_from

api = Blueprint('api', __name__)


@api.route('/solicitud', methods=['POST'])
@swag_from({
    'responses': {
        201: {
            'description': 'Solicitud creada',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Solicitud creada'
                    }
                }
            }
        },
        400: {
            'description': 'Solicitud no válida',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'Solicitud no válida'
                    }
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {'type': 'string', 'example': 'Juan'},
                    'apellido': {'type': 'string', 'example': 'Pérez'},
                    'identificacion': {'type': 'string', 'example': 'ID1234'},
                    'edad': {'type': 'integer', 'example': 18},
                    'afinidad_magica': {'type': 'string', 'example': 'Fuego'}
                }
            }
        }
    ]
})
def create_solicitud():
    """
    Crea una nueva solicitud de ingreso.
    """
    data = request.get_json()
    if not validar_solicitud(data):
        return jsonify({"error": "Solicitud no válida"}), 400
    estudiante = Estudiante(
        nombre=data['nombre'],
        apellido=data['apellido'],
        identificacion=data['identificacion'],
        edad=data['edad'],
        afinidad_magica=data['afinidad_magica']
    )
    db.session.add(estudiante)
    db.session.commit()
    return jsonify({"message": "Solicitud creada"}), 201


@api.route('/solicitud/<int:id>', methods=['PUT'])
@swag_from({
    'responses': {
        200: {
            'description': 'Solicitud actualizada',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Solicitud actualizada'
                    }
                }
            }
        },
        404: {
            'description': 'Solicitud no encontrada',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'Solicitud no encontrada'
                    }
                }
            }
        }
    }
})
def update_solicitud(id):
    """
    Actualiza una solicitud de ingreso existente.
    """
    data = request.get_json()
    estudiante = Estudiante.query.get_or_404(id)
    if 'nombre' in data:
        estudiante.nombre = data['nombre']
    if 'apellido' in data:
        estudiante.apellido = data['apellido']
    if 'identificacion' in data:
        estudiante.identificacion = data['identificacion']
    if 'edad' in data:
        estudiante.edad = data['edad']
    if 'afinidad_magica' in data:
        estudiante.afinidad_magica = data['afinidad_magica']
    db.session.commit()
    return jsonify({"message": "Solicitud actualizada"}), 200


@api.route('/solicitud/<int:id>/estatus', methods=['PATCH'])
@swag_from({
    'responses': {
        200: {
            'description': 'Estatus actualizado',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Estatus actualizado'
                    },
                    'grimorio': {
                        'type': 'string',
                        'example': 'Tres hojas'
                    }
                }
            }
        },
        404: {
            'description': 'Solicitud no encontrada',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'Solicitud no encontrada'
                    }
                }
            }
        }
    }
})
def update_status(id):
    """
    Actualiza el estatus de una solicitud de ingreso existente.
    """
    estudiante = Estudiante.query.get_or_404(id)
    grimorio = asignar_grimorio()
    estudiante.grimorio = grimorio
    db.session.commit()
    return jsonify({"message": "Estatus actualizado", "grimorio": grimorio.tipo_trebol}), 200


@api.route('/solicitudes', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de solicitudes',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer', 'example': 1},
                        'nombre': {'type': 'string', 'example': 'Juan'},
                        'apellido': {'type': 'string', 'example': 'Pérez'},
                        'identificacion': {'type': 'string', 'example': 'ID1234'},
                        'edad': {'type': 'integer', 'example': 18},
                        'afinidad_magica': {'type': 'string', 'example': 'Fuego'},
                        'grimorio': {
                            'type': 'object',
                            'properties': {
                                'tipo_trebol': {'type': 'string', 'example': 'Tres hojas'},
                                'rareza': {'type': 'string', 'example': 'Poco habitual'}
                            }
                        }
                    }
                }
            }
        }
    }
})
def get_all_solicitudes():
    """
    Obtiene una lista de todas las solicitudes de ingreso.
    """
    solicitudes = Estudiante.query.all()
    return jsonify([solicitud.to_dict() for solicitud in solicitudes]), 200


@api.route('/asignaciones', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de asignaciones',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer', 'example': 1},
                        'tipo_trebol': {'type': 'string', 'example': 'Tres hojas'},
                        'rareza': {'type': 'string', 'example': 'Poco habitual'}
                    }
                }
            }
        }
    }
})
def get_asignaciones():
    """
    Obtiene una lista de todas las asignaciones de grimorios.
    """
    asignaciones = Grimorio.query.all()
    return jsonify([asignacion.to_dict() for asignacion in asignaciones]), 200


@api.route('/solicitud/<int:id>', methods=['DELETE'])
@swag_from({
    'responses': {
        200: {
            'description': 'Solicitud eliminada',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Solicitud eliminada'
                    }
                }
            }
        },
        404: {
            'description': 'Solicitud no encontrada',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'Solicitud no encontrada'
                    }
                }
            }
        }
    }
})
def delete_solicitud(id):
    """
    Elimina una solicitud de ingreso existente.
    """
    estudiante = Estudiante.query.get_or_404(id)
    db.session.delete(estudiante)
    db.session.commit()
    return jsonify({"message": "Solicitud eliminada"}), 200
