from django.test import TestCase
from appAdres.views import validate_csv_row

class ValidateCSVRowTests(TestCase):
    def test_valid_row(self):
        """
        Prueba que una fila válida no genere errores.
        """
        row = ["12345", "test@example.com", "CC", "1000000", "Valor cualquiera"]
        errors = validate_csv_row(row, 1)
        self.assertEqual(errors, [])

    def test_invalid_column_count(self):
        """
        Prueba que una fila con un número incorrecto de columnas genere un error.
        """
        row = ["12345", "test@example.com", "CC", "1000000"]  # Faltan columnas
        errors = validate_csv_row(row, 1)
        self.assertIn("La fila 1: contiene 4 columnas, en vez de las 5 columnas exactas.", errors)

    def test_invalid_col1(self):
        """
        Prueba que una fila con un valor inválido en la columna 1 genere un error.
        """
        row = ["12", "test@example.com", "CC", "1000000", "Valor cualquiera"]  # Columna 1 inválida
        errors = validate_csv_row(row, 1)
        self.assertIn("Fila 1, Columna 1: Debe ser un número entero entre 3 y 10 caracteres.", errors)

    def test_invalid_col2(self):
        """
        Prueba que una fila con un correo electrónico inválido en la columna 2 genere un error.
        """
        row = ["12345", "invalid-email", "CC", "1000000", "Valor cualquiera"]  # Columna 2 inválida
        errors = validate_csv_row(row, 1)
        self.assertIn("Fila 1, Columna 2: Debe ser un correo electrónico válido.", errors)

    def test_invalid_col3(self):
        """
        Prueba que una fila con un valor inválido en la columna 3 genere un error.
        """
        row = ["12345", "test@example.com", "XX", "1000000", "Valor cualquiera"]  # Columna 3 inválida
        errors = validate_csv_row(row, 1)
        self.assertIn("Fila 1, Columna 3: Solo se permiten los valores 'CC' o 'TI'.", errors)

    def test_invalid_col4(self):
        """
        Prueba que una fila con un valor inválido en la columna 4 genere un error.
        """
        row = ["12345", "test@example.com", "CC", "2000000", "Valor cualquiera"]  # Columna 4 inválida
        errors = validate_csv_row(row, 1)
        self.assertIn("Fila 1, Columna 4: Debe ser un valor entre 500000 y 1500000.", errors)