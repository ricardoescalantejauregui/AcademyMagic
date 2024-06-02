# GrimoireRegistry

GrimoireRegistry es una aplicación Flask para gestionar solicitudes de estudiantes y la asignación de grimorios en una academia de magia.

## Requisitos

- Python 3.8 o superior
- Virtualenv
- Postgres

## Configuración del Entorno

1. Clona el repositorio:

    ```sh
    git clone https://github.com/ricardoescalantejauregui/AcademyMagic.git
    cd AcademyMagic
    ```

2. Crea y activa un entorno virtual:

    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows: .\venv\Scripts\activate
    ```

3. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno (opcional):

    ```sh
    export FLASK_APP=run.py
    export FLASK_ENV=development
    export SECRET_KEY='adivina'
    ```

## Inicialización de la Base de Datos

1. Inicializa la base de datos:

    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Ejecución de la Aplicación

1. Configurar la conexión de base de datos se debe de declarar una variable de ambiente llamada 'DATABASE_URL' esta debe estar en postgres 'postgresql://myuser:mypassword@localhost:5432/mydatabase'
2. Para poblar la base de datos es necesario correr el script en el folder `scripts/populate_db.py` y descomentar las lineas siguientes: 

   ```python 
   # Ejecutar el script
   with app.app_context():
       db.create_all()  # Asegurarse de que todas las tablas estén creadas
       create_grimorios()     #llenar lista de grimorios
       create_estudiantes()   #llenar lista de solicitudes
       print("Base de datos poblada con datos de prueba.")
   ```
3. 
4. Ejecuta el servidor:

    ```sh
    cd scripts
    python populate_db.py
    ```
   nota: correr solamente una vez, puede generar duplicados en la tabla 'grimorios'
5. Ejecuta el servidor:

    ```sh
    python run.py
    ```
6. Abre tu navegador y navega a `http://127.0.0.1:5000` para ver la aplicación en funcionamiento.


## Estructura del Proyecto

El proyecto está organizado en una estructura típica de aplicación Flask, utilizando SQLAlchemy para la gestión de la base de datos PostgreSQL y Flask-Migrate para las migraciones de la base de datos. A continuación se describe la estructura de los archivos y directorios principales:

* `app.py`: Archivo principal de la aplicación donde se inicializa Flask y se configuran las extensiones.
* `config.py`: Archivo de configuración que contiene la configuración de la base de datos y otras configuraciones de la aplicación.
* `create_tables.py`: Script para crear las tablas en la base de datos PostgreSQL.
* `GrimoireRegistry/`: Directorio que contiene los módulos principales de la aplicación.
* `__init__.py`: Inicializa la aplicación Flask y las extensiones.
* `models.py`: Define los modelos de datos para SQLAlchemy.
* `web_routes.py`: Define las rutas y vistas para la aplicación web.
* `api_routes.py`: Define las rutas y vistas para la API.
* `templates/: Directorio que contiene las plantillas HTML de la aplicación.
* `base.html`: Plantilla base que define la estructura común de las páginas.
* `index.html`: Página principal de la aplicación.
* `solicitudes.html`: Página que muestra la lista de solicitudes.
* `crear_solicitud.html`: Página para crear una nueva solicitud.
* `modificar_solicitud.html`: Página para modificar una solicitud existente.
* `static/`: Directorio que contiene archivos estáticos como CSS y JavaScript.
* `css/styles.css`: Archivo de estilos personalizados.

project_root/
│
├── app.py
├── config.py
├── create_tables.py
├── GrimoireRegistry/
│   ├── __init__.py
│   ├── models.py
│   ├── web_routes.py
│   ├── api_routes.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── solicitudes.html
│   ├── crear_solicitud.html
│   ├── modificar_solicitud.html
│
└── static/
    └── css/
        └── styles.css
## Sitio en internet:

https://flask-academy-grimoire.vercel.app/

## API doc Swagger: 

https://flask-academy-grimoire.vercel.app/apidocs/

## API :
   https://flask-academy-grimoire.vercel.app/api/{urls}

• POST /solicitud: Envía solicitud de ingreso.

• PUT /solicitud/{id}: Actualiza solicitud de ingreso.

• PATCH /solicitud/{id}/estatus: Actualiza estatus de solicitud.

• GET /solicitudes: Consulta todas las solicitudes.

• GET /asignaciones: Consulta asignaciones de Grimorios.

• DELETE /solicitud/{id}: Elimina solicitud de ingreso.
