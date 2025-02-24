# Referencia de la API

## Descripción general

Este documento proporciona una referencia para los endpoints de la API disponibles en la aplicación proyectoAdres. La funcionalidad principal gira en torno a la carga y validación de archivos CSV.

## Endpoints

### Cargar CSV

- **URL**: `/upload_csv`
- **Método**: `POST`
- **Descripción**: Este endpoint maneja la carga de archivos CSV. Valida el contenido del archivo cargado de acuerdo con las reglas especificadas.

#### Solicitud

- **Tipo de contenido**: `multipart/form-data`
- **Parámetros**:
- `csv_file`: El archivo CSV que se cargará. Este archivo debe cumplir con la siguiente estructura:
- Cada fila debe contener exactamente 5 columnas.
- Columna 1: Un número entero entre 3 y 10 dígitos.
- Columna 2: Una dirección de correo electrónico válida.
- Columna 3: debe ser 'CC' o 'TI'.
- Columna 4: un número entero entre 500000 y 1500000.
- Columna 5: cualquier valor (opcional).

#### Respuesta

- **Éxito (200)**:
- Contenido: un mensaje de éxito que indica que el archivo es válido.

- **Error (400)**:
- Contenido: una lista de mensajes de error que detallan los problemas de validación encontrados en el archivo CSV cargado.

### Ejemplo

#### Ejemplo de solicitud

```http
POST /upload_csv HTTP/1.1
Host: example.com
Content-Type: multipart/form-data

--boundary
Content-Disposition: form-data; name="csv_file"; nombre de archivo="prueba.csv"
Tipo de contenido: texto/csv

12345,test@example.com,CC,1000000,Valor cualquiera
67890,test2@example.com,TI,750000,Otro valor
--límite--
```

#### Ejemplo de respuesta

```json
{
 "success": "El archivo es válido."
}
```

### Ejemplo de respuesta de error

```json
{
 "errores": [
 "La fila 1: contiene 4 columnas, en vez de las 5 columnas exactas.",
 "Fila 2, Columna 2: Debe ser un correo electrónico válido."
 ]
}
```

## Conclusión

Esta API permite a los usuarios cargar archivos CSV para su validación, asegurando que los datos cumplan con el formato y las reglas especificados. Se implementa un manejo adecuado de errores para guiar a los usuarios en la corrección de cualquier problema con sus cargas.