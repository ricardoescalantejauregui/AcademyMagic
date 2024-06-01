import os
import random
import sys

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from faker import Faker
from GrimoireRegistry import create_app, db
from GrimoireRegistry.models import Estudiante, Grimorio

# Configura la aplicación
app = create_app()

# Usa Faker para generar datos falsos
fake = Faker()

# Tipos y rarezas de Grimorios
grimorios_info = [
    {'tipo_trebol': 'Una hoja', 'rareza': 'Común'},
    {'tipo_trebol': 'Dos hojas', 'rareza': 'Común'},
    {'tipo_trebol': 'Tres hojas', 'rareza': 'Poco habitual'},
    {'tipo_trebol': 'Cuatro hojas', 'rareza': 'Inusual'},
    {'tipo_trebol': 'Cinco hojas', 'rareza': 'Muy raro'}
]


# Crear Grimorios
def create_grimorios():
    for info in grimorios_info:
        grimorio = Grimorio(tipo_trebol=info['tipo_trebol'], rareza=info['rareza'])
        db.session.add(grimorio)
    db.session.commit()


# Crear Estudiantes
def create_estudiantes(num_estudiantes=10):
    afinidades_magicas = ['Oscuridad', 'Luz', 'Fuego', 'Agua', 'Viento', 'Tierra']
    grimorios = Grimorio.query.all()

    for _ in range(num_estudiantes):
        nombre = fake.first_name()
        apellido = fake.last_name()
        identificacion = fake.bothify(text='??####')
        edad = random.randint(10, 18)
        afinidad_magica = random.choice(afinidades_magicas)
        grimorio = random.choice(grimorios)

        estudiante = Estudiante(
            nombre=nombre,
            apellido=apellido,
            identificacion=identificacion,
            edad=edad,
            afinidad_magica=afinidad_magica,
            grimorio=grimorio
        )
        db.session.add(estudiante)
    db.session.commit()


# Ejecutar el script
with app.app_context():
    db.create_all()  # Asegurarse de que todas las tablas estén creadas
    # create_grimorios()
    # create_estudiantes()
    print("Base de datos poblada con datos de prueba.")
