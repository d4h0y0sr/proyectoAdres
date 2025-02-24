# Proyecto Adres

Proyecto Adres es una aplicación web diseñada para validar y procesar archivos CSV. Permite a los usuarios subir archivos CSV, los cuales son validados según reglas específicas, y proporciona retroalimentación sobre la validez de los datos.

## Contenido del Proyecto

- **appAdres/templates/appAdres/upload.html**: Contiene la plantilla HTML para la página de carga de CSV. Incluye un formulario para la carga de archivos, mensajes de error y notificaciones de éxito.
  
- **appAdres/views.py**: Contiene la lógica para manejar las cargas de archivos CSV. Incluye las siguientes funciones:
  - `validate_csv_row(row, row_num)`: Valida una fila del archivo CSV según reglas especificadas y devuelve una lista de errores.
  - `process_csv_file(csv_file)`: Procesa el archivo CSV subido, valida cada fila y devuelve una lista de errores encontrados.
  - `upload_csv(request)`: Maneja la carga y validación de archivos CSV. Procesa solicitudes POST, valida el archivo subido y renderiza la respuesta adecuada según el éxito o los errores.

- **appAdres/tests/test_views.py**: Contiene pruebas unitarias para las vistas de la aplicación. Incluye los siguientes casos de prueba:
  - `test_get_request`: Prueba que la vista maneje correctamente las solicitudes GET.
  - `test_post_invalid_csv`: Prueba que la vista maneje correctamente la carga de un archivo CSV inválido.
  - `test_post_valid_csv`: Prueba que la vista maneje correctamente la carga de un archivo CSV válido.

- **docs/index.md**: Sirve como punto de entrada principal para la documentación. Proporciona una visión general del proyecto.

- **docs/installation.md**: Contiene instrucciones para instalar el proyecto y sus dependencias.

- **docs/usage.md**: Proporciona información sobre cómo usar el proyecto, incluyendo ejemplos y escenarios de uso.

- **docs/api_reference.md**: Documenta los endpoints de la API y su uso.

- **requirements.txt**: Lista las dependencias de Python requeridas para el proyecto.

## Cómo Empezar

1. Clona o descarga este repositorio:

2. Navega al directorio del proyecto:
   ```
   cd inserte-ubicación-del-proyecto\proyectoAdres
   ```
3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

5. Accede a la aplicación en tu navegador en `http://127.0.0.1:8000`
