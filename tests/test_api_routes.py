import unittest
from flask import json
from GrimoireRegistry import create_app, db
from GrimoireRegistry.models import Estudiante, Grimorio
from config import TestConfig

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Crear datos de prueba
        grimorio = Grimorio(tipo_trebol='Tres hojas', rareza='Poco habitual')
        estudiante = Estudiante(
            nombre='Juan',
            apellido='Pérez',
            identificacion='JP1234',
            edad=18,
            afinidad_magica='Fuego',
            grimorio=grimorio
        )
        db.session.add(grimorio)
        db.session.add(estudiante)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_solicitud(self):
        response = self.client.post('/solicitud', data=json.dumps({
            'nombre': 'Ana',
            'apellido': 'Lopez',
            'identificacion': 'AL1234',
            'edad': 20,
            'afinidad_magica': 'Agua'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Solicitud creada', str(response.data))

    def test_update_solicitud(self):
        estudiante = Estudiante.query.first()
        response = self.client.put(f'/solicitud/{estudiante.id}', data=json.dumps({
            'nombre': 'Pedro',
            'apellido': 'Gomez',
            'identificacion': 'PG1234',
            'edad': 22,
            'afinidad_magica': 'Viento',
            'grimorio_id': estudiante.grimorio_id
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Solicitud actualizada', str(response.data))

    def test_update_status(self):
        estudiante = Estudiante.query.filter_by(grimorio_id=6).first()
        if not estudiante:
            grimorio = Grimorio(tipo_trebol='Seis hojas', rareza='Raro')
            estudiante = Estudiante(
                nombre='Carlos',
                apellido='Martinez',
                identificacion='CM1234',
                edad=25,
                afinidad_magica='Tierra',
                grimorio=grimorio
            )
            db.session.add(grimorio)
            db.session.add(estudiante)
            db.session.commit()

        response = self.client.patch(f'/solicitud/{estudiante.id}/estatus')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Estatus actualizado', str(response.data))

    def test_get_all_solicitudes(self):
        response = self.client.get('/solicitudes')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Juan', str(response.data))

    def test_get_asignaciones(self):
        response = self.client.get('/asignaciones')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Tres hojas', str(response.data))

    def test_delete_solicitud(self):
        estudiante = Estudiante.query.first()
        response = self.client.delete(f'/solicitud/{estudiante.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Solicitud eliminada', str(response.data))

if __name__ == '__main__':
    unittest.main()
