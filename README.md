# GrimoireRegistry

GrimoireRegistry es una aplicación Flask para gestionar solicitudes de estudiantes y la asignación de grimorios en una academia de magia.

## Requisitos

- Python 3.8 o superior
- Virtualenv

## Configuración del Entorno

1. Clona el repositorio:

    ```sh
    git clone https://github.com/tu-usuario/GrimoireRegistry.git
    cd GrimoireRegistry
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

1. Ejecuta el servidor:

    ```sh
    python run.py
    ```

2. Abre tu navegador y navega a `http://127.0.0.1:5000` para ver la aplicación en funcionamiento.

## Estructura del Proyecto

