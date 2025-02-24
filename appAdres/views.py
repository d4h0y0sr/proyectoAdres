import csv,re
from django.shortcuts import render
from .forms import CSVUploadForm


def validate_csv_row(row, row_num):
    """
    Valida una fila del CSV según las reglas especificadas.
    Retorna una lista de errores para la fila.

    Args:
        row (list): Lista de valores que representan una fila del CSV.
        row_num (int): Número de la fila actual (1-indexed).
    
    Returns:
        list: Lista de errores encontrados en la fila.
    """
    errors = []       
    # Verificar que la fila tenga exactamente 5 columnas
    if len(row) != 5:
        errors.append(f"La fila {row_num}: contiene {len(row)} columnas, en vez de las 5 columnas exactas.")
        return errors

    col1, col2, col3, col4, col5 = row
    # Validar la primera columna: debe ser un número entero entre 3 y 10 caracteres
    if not col1.isdigit() or len(col1) < 3 or len(col1) > 10:
        errors.append(f"Fila {row_num}, Columna 1: Debe ser un número entero entre 3 y 10 caracteres.")
    
    # Validar la segunda columna: debe ser un correo electrónico válido
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, col2):
        errors.append(f"Fila {row_num}, Columna 2: Debe ser un correo electrónico válido.")

    # if '@' not in col2 or '.' not in col2:
    #     errors.append(f"Fila {row_num}, Columna 2: Debe ser un correo electrónico válido.")

    # Validar la tercera columna: solo se permiten los valores 'CC' o 'TI'
    if col3 not in ['CC', 'TI']:
        errors.append(f"Fila {row_num}, Columna 3: Solo se permiten los valores 'CC' o 'TI'.")

    # Validar la cuarta columna: debe ser un valor entre 500000 y 1500000
    if not col4.isdigit() or int(col4) < 500000 or int(col4) > 1500000:
        errors.append(f"Fila {row_num}, Columna 4: Debe ser un valor entre 500000 y 1500000.")

    return errors

def process_csv_file(csv_file):
    """
    Procesa el archivo CSV y valida cada fila.
    
    Args:
        csv_file (UploadedFile): Archivo CSV subido por el usuario.
    
    Returns:
        list: Lista de errores encontrados en el archivo CSV.
    """
    errors = []
    # Leer y decodificar el archivo CSV
    try:
        decoded_file = csv_file.read().decode('utf-8').splitlines()                    
        reader = csv.reader(decoded_file)      
    except Exception as e:
        errors.append("Error al leer el archivo: El archivo no tiene un formato de texto válido.")
        return errors     
    # Validar cada fila del archivo CSV  
    for row_num, row in enumerate(reader, start=1):                
        row_errors = validate_csv_row(row, row_num)
        errors.extend(row_errors)

    return errors

def upload_csv(request):
    """
    Vista para manejar la subida y validación de archivos CSV.
    
    Args:
        request (HttpRequest): Objeto HttpRequest que contiene los datos de la solicitud.
    
    Returns:
        HttpResponse: Respuesta HTTP con el resultado de la validación del archivo CSV.
    """
    form_submitted = False

    if request.method == 'POST':
        form_submitted = True
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']               
            errors = process_csv_file(csv_file)     
  
            if errors:
                return render(request, 'appAdres/upload.html', {
                    'form': form,
                    'errors': errors,
                    'form_submitted': form_submitted,
                })
            else:
                return render(request, 'appAdres/upload.html', {
                    'form': form,
                    'success': 'El archivo es válido.',
                    'form_submitted': form_submitted,
                })
        else:
            return render(request, 'appAdres/upload.html', {
                'form': form,
                'errors': ["El contenido del archivo no corresponde a un CSV válido."],
                'form_submitted': form_submitted,
            })
    else:
        form = CSVUploadForm()    
    return render(request, 'appAdres/upload.html', {
        'form': form,
        'form_submitted': form_submitted,
    })