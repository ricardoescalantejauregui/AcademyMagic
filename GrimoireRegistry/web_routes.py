from flask import Blueprint, render_template
from .models import Estudiante

# Creating a blueprint for the application routes
web = Blueprint('web', __name__)


@web.route('/')
def index():
    """
    Route to the home page.

    Returns:
        Rendered 'index.html' template
    """
    return render_template('index.html')


@web.route('/solicitudes')
def get_solicitudes():
    """
    Route to the solicitudes page. Fetches all Estudiante objects from the database.

    Returns:
        Rendered 'solicitudes.html' template showing all the solicitudes
    """
    solicitudes = Estudiante.query.all()
    return render_template('solicitudes.html', solicitudes=solicitudes)
