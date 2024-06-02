from .models import Grimorio
import random


def validar_solicitud(data):
    """
    Valida los datos de una solicitud de ingreso.

    Args:
        data (dict): Diccionario con los datos de la solicitud.

    Returns:
        bool: True si la solicitud es válida, False en caso contrario.
    """
    if not isinstance(data.get('nombre'), str) or len(data['nombre']) > 20:
        return False
    if not isinstance(data.get('apellido'), str) or len(data['apellido']) > 20:
        return False
    if not isinstance(data.get('identificacion'), str) or len(data['identificacion']) > 10:
        return False
    if not isinstance(data.get('edad'), int) or data['edad'] < 10 or data['edad'] > 99:
        return False
    if data.get('afinidad_magica') not in ['Oscuridad', 'Luz', 'Fuego', 'Agua', 'Viento', 'Tierra']:
        return False
    return True


def asignar_grimorio():
    """
    Asigna un grimorio a una solicitud aprobada de forma aleatoria,
    utilizando ponderaciones basadas en la rareza del grimorio.

    Returns:
        Grimorio: El grimorio asignado.
    """
    grimorios = Grimorio.query.all()
    ponderaciones = [1, 2, 3, 4, 5]  # Ajustar según la rareza
    return random.choices(grimorios, weights=ponderaciones, k=1)[0]
