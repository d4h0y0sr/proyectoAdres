from django.test import TestCase, RequestFactory
from django.urls import reverse
from appAdres.views import upload_csv
from django.core.files.uploadedfile import SimpleUploadedFile

class UploadCSVViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('upload_csv')

    def test_get_request(self):
        """
        Prueba que la vista maneje correctamente una solicitud GET.
        """
        request = self.factory.get(self.url)
        response = upload_csv(request)
       
        self.assertEqual(response.status_code, 200)        

    def test_post_invalid_csv(self):
        """
        Prueba que la vista maneje correctamente un archivo CSV inválido.
        """
        csv_content = "12345,test@example.com,CC,asdasfdasdf\n"
        csv_file = SimpleUploadedFile("test.csv", csv_content.encode('utf-8'), content_type="text/csv")
        request = self.factory.post(self.url, {'csv_file': csv_file})
        request.FILES['csv_file'] = csv_file
        csv_file.seek(0)        
        response = upload_csv(request)                      
        self.assertIn('La fila 1: contiene 4 columnas, en vez de las 5 columnas exactas.', response.content.decode())

    def test_post_invalid_email(self):
        """
        Prueba que la vista maneje correctamente un archivo CSV inválido.
        """
        csv_content = "12345,com.@.latam$,CC,500000,asdf\n"
        csv_file = SimpleUploadedFile("test.csv", csv_content.encode('utf-8'), content_type="text/csv")
        request = self.factory.post(self.url, {'csv_file': csv_file})
        request.FILES['csv_file'] = csv_file
        csv_file.seek(0)        
        response = upload_csv(request)                      
        self.assertIn('Fila 1, Columna 2: Debe ser un correo electrónico válido.', response.content.decode())
        
        
    def test_post_valid_csv(self):
        """
        Prueba que la vista maneje correctamente un archivo CSV válido.
        """
        csv_content = (
            "12345,test@example.com,CC,1000000,Valor cualquiera\n"
            "67890,test2@example.com,TI,750000,Otro valor\n"
        )
        csv_file = SimpleUploadedFile("test.csv", csv_content.encode('utf-8'), content_type="text/csv")        
        request = self.factory.post(self.url, {'csv_file': csv_file})
        request.FILES['csv_file'] = csv_file
        csv_file.seek(0)
        response = upload_csv(request)       
        self.assertEqual(response.status_code, 200)
        self.assertIn('El archivo es válido.', response.content.decode())

