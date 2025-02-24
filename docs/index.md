# Documentación del Proyecto Adres

## Descripción general

Proyecto Adres es una aplicación web diseñada para facilitar la carga y validación de archivos CSV. La aplicación ofrece a los usuarios una interfaz intuitiva para cargar sus archivos CSV, lo que garantiza que los datos cumplan con las reglas de validación especificadas. Está construida con Django, un framework web Python de alto nivel, y aprovecha Bootstrap para un diseño responsive.

## Características

- **Carga de CSV**: los usuarios pueden cargar archivos CSV a través de un formulario fácil de usar.
- **Validación**: la aplicación valida los archivos CSV cargados con reglas predefinidas, lo que garantiza la integridad de los datos.
- **Manejo de errores**: los usuarios reciben comentarios claros sobre cualquier error de validación encontrado durante el proceso de carga.
- **Notificaciones de éxito**: luego de una validación exitosa, se notifica a los usuarios que su archivo es válido.

## Estructura del proyecto

El proyecto consta de los siguientes componentes clave:

- **appAdres**: contiene la lógica principal de la aplicación, incluidas las vistas y las plantillas.
- **templates/appAdres/upload.html**: plantilla HTML para la página de carga de CSV.
- **views.py**: contiene la lógica para manejar las cargas y validaciones de archivos CSV.
- **tests/test_views.py**: pruebas unitarias para las vistas de la aplicación.

- **docs**: archivos de documentación del proyecto.
- **index.md**: punto de entrada principal para la documentación.
- **installation.md**: instrucciones para instalar el proyecto.
- **usage.md**: información sobre cómo usar el proyecto.
- **api_reference.md**: documentación de los puntos finales de la API.


- **README.md**: breve descripción del proyecto y cómo comenzar.
- **requirements.txt**: enumera las dependencias de Python necesarias para el proyecto.

## Primeros pasos

Para comenzar a utilizar Proyecto Adres, consulte las instrucciones de instalación en `docs/installation.md`. Para ver ejemplos y escenarios de uso, consulte `docs/usage.md`. 