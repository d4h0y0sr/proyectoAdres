from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from appAdres.views import process_csv_file

class ProcessCSVFileTests(TestCase):
    def test_valid_csv(self):
        """
        Prueba que un archivo CSV válido no genere errores.
        """
        csv_content = (
            "12345,test@example.com,CC,1000000,Valor cualquiera\n"
            "67890,test2@example.com,TI,750000,Otro valor\n"
        )
        csv_file = SimpleUploadedFile("test.csv", csv_content.encode('utf-8'), content_type="text/csv")
        errors = process_csv_file(csv_file)
        self.assertEqual(errors, [])

    def test_invalid_csv(self):
        """
        Prueba que un archivo CSV inválido genere errores.
        """
        csv_content = "12345,test@example.com,CC,1000000\n"  # Faltan columnas
        csv_file = SimpleUploadedFile("test.csv", csv_content.encode('utf-8'), content_type="text/csv")
        errors = process_csv_file(csv_file)
        self.assertIn("La fila 1: contiene 4 columnas, en vez de las 5 columnas exactas.", errors)

    def test_non_csv_file(self):
        """
        Prueba que un archivo diferente a csv genere un error.
        """
        # Crear un archivo binario que simule una imagen JPEG
        file_content = b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00'  # Cabecera de un archivo JPEG
        image_file = SimpleUploadedFile(
            "test.jpg",  # Nombre del archivo
            file_content,  # Contenido binario
            content_type="image/jpeg"  # Tipo de contenido
        )        
        errors = process_csv_file(image_file)
        self.assertIn("Error al leer el archivo: El archivo no tiene un formato de texto válido.", errors)