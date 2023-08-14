Dependencias
Estos scripts requieren las siguientes bibliotecas:
requests
qrcode
PIL
seaborn
matplotlib

Se encontró que la función generate_qr en el archivo uno.py puede generar un error catastrófico si es la primera vez que se abre una imagen como salida de Visual Studio Code en el visor de imágenes de Windows. Este error solo ocurre en ese sistema operativo y se debe a cómo se almacenan los datos temporales al solicitarle al usuario con qué desea abrir la imagen. Este error nunca vuelve a ocurrir a partir de la segunda ejecución en adelante.
