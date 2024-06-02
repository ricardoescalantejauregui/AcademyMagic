import unittest
from GrimoireRegistry import create_app, db
from GrimoireRegistry.models import Estudiante, Grimorio
from config import TestConfig

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test variables."""
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Crear datos de prueba
        self.grimorio = Grimorio(tipo_trebol='Tres hojas', rareza='Poco habitual')
        self.estudiante = Estudiante(
            nombre='Juan',
            apellido='Pérez',
            identificacion='JP1234',
            edad=16,
            afinidad_magica='Fuego',
            grimorio=self.grimorio
        )

        db.session.add(self.grimorio)
        db.session.add(self.estudiante)
        db.session.commit()

    def tearDown(self):
        """Tear down test variables."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_estudiante_creation(self):
        """Test if the estudiante model is created correctly."""
        estudiante = Estudiante.query.first()
        self.assertEqual(estudiante.nombre, 'Juan')
        self.assertEqual(estudiante.apellido, 'Pérez')
        self.assertEqual(estudiante.identificacion, 'JP1234')
        self.assertEqual(estudiante.edad, 16)
        self.assertEqual(estudiante.afinidad_magica, 'Fuego')
        self.assertEqual(estudiante.grimorio.tipo_trebol, 'Tres hojas')

    def test_grimorio_creation(self):
        """Test if the grimorio model is created correctly."""
        grimorio = Grimorio.query.first()
        self.assertEqual(grimorio.tipo_trebol, 'Tres hojas')
        self.assertEqual(grimorio.rareza, 'Poco habitual')

if __name__ == '__main__':
    unittest.main()
