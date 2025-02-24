## Descripción general

El proyecto `proyectoAdres` está diseñado para facilitar la carga y validación de archivos CSV. Este documento proporciona orientación sobre cómo usar la aplicación de manera efectiva.

## Primeros pasos

1. **Acceda a la aplicación**: navegue a la página de carga de CSV en su navegador web. La URL generalmente sigue el formato: `http://<your-server>/upload`. Sin embargo, puede ir a la raiz del servidor e.g http://Localhost:8080/ y será redirigido automaticamente a la página de carga.

2. **Carga de un archivo CSV**:
- Haga clic en el botón "Selecciona un archivo CSV" para elegir un archivo CSV de su máquina local.
- Asegúrese de que el archivo CSV cumpla con el siguiente formato:
- Cada fila debe contener exactamente 5 columnas.
- La primera columna debe ser un número entero de entre 3 y 10 caracteres de longitud.
- La segunda columna debe ser una dirección de correo electrónico válida.
- La tercera columna debe contener 'CC' o 'TI'.
- La cuarta columna debe ser un número entero entre 500.000 y 1.500.000.
- La quinta columna puede contener cualquier valor.

3. **Envío del archivo**: Después de seleccionar el archivo, haga clic en el botón "Enviar" para cargar el archivo CSV.

## Manejo de errores

Si el archivo CSV cargado contiene errores:
- La aplicación mostrará una lista de errores que indica los problemas específicos encontrados en el archivo.
- Cada mensaje de error especificará la fila y la columna donde ocurrió el problema, lo que permite una fácil identificación y corrección.

## Notificación de éxito

Tras la validación exitosa del archivo CSV:
- Se mostrará un mensaje de éxito, confirmando que el archivo es válido.

## Ejemplo de uso

### Ejemplo de CSV válido
```
12345,test@example.com,CC,1000000,Some value
67890,test2@example.com,TI,750000,Another value
```

### Ejemplo de CSV no válido
```
12345,test@example.com,CC,1000000
67890,test2@example.com,XYZ,750000,Another value
```
En el ejemplo no válido, a la primera fila le falta una columna y la tercera columna de la segunda fila contiene un valor no válido.

## Conclusión

Esta guía proporciona los pasos necesarios para utilizar eficazmente la aplicación `proyectoAdres` para cargar archivos CSV. Para obtener más ayuda, consulte los demás archivos de documentación o comuníquese con los encargados del mantenimiento del proyecto.