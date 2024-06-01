from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Estudiante, Grimorio, db
from flask_paginate import Pagination, get_page_args

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

@web.route('/asignaciones')
def asignaciones():
    grimorios = Grimorio.query.all()
    return render_template('asignaciones.html', grimorios=grimorios)

@web.route('/solicitudes')
def solicitudes():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page', offset_parameter='offset')
    per_page = 10
    offset = (page - 1) * per_page
    total = Estudiante.query.count()
    estudiantes = Estudiante.query.offset(offset).limit(per_page).all()
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template('solicitudes.html', estudiantes=estudiantes, page=page, per_page=per_page, pagination=pagination)

@web.route('/crear-solicitud', methods=['GET', 'POST'])
def crear_solicitud():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        identificacion = request.form.get('identificacion')
        edad = request.form.get('edad')
        afinidad_magica = request.form.get('afinidad_magica')
        grimorio_id = request.form.get('grimorio_id')

        # Validar datos
        if not nombre.isalpha() or len(nombre) > 20:
            flash('Nombre no válido. Debe contener solo letras y tener máximo 20 caracteres.', 'danger')
            return redirect(url_for('web.crear_solicitud'))
        if not apellido.isalpha() or len(apellido) > 20:
            flash('Apellido no válido. Debe contener solo letras y tener máximo 20 caracteres.', 'danger')
            return redirect(url_for('web.crear_solicitud'))
        if not identificacion.isalnum() or len(identificacion) > 10:
            flash('Identificación no válida. Debe contener solo números y letras, y tener máximo 10 caracteres.', 'danger')
            return redirect(url_for('web.crear_solicitud'))
        if not edad.isdigit() or not (10 <= int(edad) <= 99):
            flash('Edad no válida. Debe ser un número de dos dígitos entre 10 y 99.', 'danger')
            return redirect(url_for('web.crear_solicitud'))
        if afinidad_magica not in ['Oscuridad', 'Luz', 'Fuego', 'Agua', 'Viento', 'Tierra']:
            flash('Afinidad mágica no válida.', 'danger')
            return redirect(url_for('web.crear_solicitud'))

        grimorio = Grimorio.query.get(grimorio_id)
        nueva_solicitud = Estudiante(
            nombre=nombre,
            apellido=apellido,
            identificacion=identificacion,
            edad=int(edad),
            afinidad_magica=afinidad_magica,
            grimorio=grimorio
        )

        db.session.add(nueva_solicitud)
        db.session.commit()
        flash('Solicitud creada exitosamente!', 'success')
        return redirect(url_for('web.solicitudes'))

    grimorios = Grimorio.query.all()
    return render_template('crear_solicitud.html', grimorios=grimorios)

@web.route('/modificar-solicitud/<int:id>', methods=['GET', 'POST'])
def modificar_solicitud(id):
    estudiante = Estudiante.query.get_or_404(id)
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        identificacion = request.form.get('identificacion')
        edad = request.form.get('edad')
        afinidad_magica = request.form.get('afinidad_magica')
        grimorio_id = request.form.get('grimorio_id')

        # Validar datos
        if not nombre.isalpha() or len(nombre) > 20:
            flash('Nombre no válido. Debe contener solo letras y tener máximo 20 caracteres.', 'danger')
            return redirect(url_for('web.modificar_solicitud', id=id))
        if not apellido.isalpha() or len(apellido) > 20:
            flash('Apellido no válido. Debe contener solo letras y tener máximo 20 caracteres.', 'danger')
            return redirect(url_for('web.modificar_solicitud', id=id))
        if not identificacion.isalnum() or len(identificacion) > 10:
            flash('Identificación no válida. Debe contener solo números y letras, y tener máximo 10 caracteres.', 'danger')
            return redirect(url_for('web.modificar_solicitud', id=id))
        if not edad.isdigit() or not (10 <= int(edad) <= 99):
            flash('Edad no válida. Debe ser un número de dos dígitos entre 10 y 99.', 'danger')
            return redirect(url_for('web.modificar_solicitud', id=id))
        if afinidad_magica not in ['Oscuridad', 'Luz', 'Fuego', 'Agua', 'Viento', 'Tierra']:
            flash('Afinidad mágica no válida.', 'danger')
            return redirect(url_for('web.modificar_solicitud', id=id))

        estudiante.nombre = nombre
        estudiante.apellido = apellido
        estudiante.identificacion = identificacion
        estudiante.edad = int(edad)
        estudiante.afinidad_magica = afinidad_magica
        estudiante.grimorio_id = grimorio_id

        db.session.commit()
        flash('Solicitud modificada exitosamente!', 'success')
        return redirect(url_for('web.solicitudes'))

    grimorios = Grimorio.query.all()
    return render_template('modificar_solicitud.html', estudiante=estudiante, grimorios=grimorios)

@web.route('/eliminar-solicitud/<int:id>', methods=['POST'])
def eliminar_solicitud(id):
    estudiante = Estudiante.query.get_or_404(id)
    db.session.delete(estudiante)
    db.session.commit()
    flash('Solicitud eliminada exitosamente!', 'success')
    return redirect(url_for('web.solicitudes'))
