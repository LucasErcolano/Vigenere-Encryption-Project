import requests
import qrcode
from PIL import Image


def keys() -> str:
    """Solicita al usuario que ingrese una clave y verifica si es válida.

    La clave debe contener solo letras del alfabeto inglés y no puede estar vacía.
    Si la clave no cumple con estos requisitos, se le pedirá al usuario que ingrese una nueva clave hasta que sea válida.

    Returns:
        str: La clave válida ingresada por el usuario.
    """
    print("Ingrese la clave: ")
    key = input("> ")
    check = True
    while check:
        if key == "":
            print("La clave no puede ser vacia")
            key = input("\033[31m>\033[0m ")
        elif not (key.isalpha()):
            print("La clave solo puede contener letras del alfabeto inglés")
            key = input("\033[31m>\033[0m ")
        else:
            check = False
    return key.lower()


def path_picker() -> str:
    """Solicita al usuario que ingrese la ruta de un archivo y lo abre.

    Si no se puede abrir el archivo, se le pedirá al usuario que vuelva a ingresar
    la ruta hasta que se pueda abrir el archivo. Devuelve el contenido del archivo en minúsculas.

    Returns:
        str: El contenido del archivo en minúsculas.
    """
    print("Ingrese la \033[4mruta\033[0m del archivo: ")
    path = input("> ")
    check = True
    while check:
        try:
            with open(path) as msj:
                check = False
                files = msj.readlines()
        except:
            print("No se pudo \033[1mabrir\033[0m el archivo")
            path = input("\033[31m>\033[0m ")
    final = ""
    for line in files:
        final += line.lower()
    return final


def same_len(key: str, msj: str) -> str:
    """Ajusta la longitud de la clave para que coincida con la longitud del mensaje.

    Args:
        key (str): La clave a ajustar.
        msj (str): El mensaje para el cual se ajustará la clave.

    Returns:
        str: La clave ajustada para que coincida con la longitud del mensaje.
    """
    k_clone = ''
    k_index = 0
    for char in msj:
        if char.isalpha():
            k_clone += key[k_index]
            k_index = (k_index + 1) % len(key)
        else:
            k_clone += char
    return k_clone


def num_covert(key: str, msj: str) -> set:
    """Convierte las letras de una clave y un mensaje en números.

     Args:
         key (str): La clave a convertir.
         msj (str): El mensaje a convertir.

     Returns:
         Dos listas.
         La primera lista contiene los números correspondientes,
         a las letras de la clave y la segunda lista
         contiene los números correspondientes a las letras del mensaje.
         Si un carácter en el mensaje no es una letra,
         se agrega el carácter original a la lista.
     """
    m = []
    k = []
    for i, j in zip(key, msj):
        k.append((ord(i)-97))
        if j.isalpha():
            m.append((ord(j)-97))
        else:
            m.append(j)
    return m, k


def encripter(key: list, msj: list, op: str) -> str:
    """Encripta o desencripta un mensaje utilizando una clave y una operación.
    Args:
        key (list): La clave utilizada para encriptar o desencriptar el mensaje.
        msj (list): El mensaje a encriptar o desencriptar.
        op (str): La operación a realizar, "+" para encriptar y
        "-" para desencriptar.
    Returns:
        str: El mensaje solicitado.
    """
    res = ""
    for k, m in zip(key, msj):
        if type(m) == int:
            if op == "+":
                res += chr(((m+k) % 26)+97)
            else:
                res += chr(((m-k) % 26)+97)
        else:
            res += m
    return res


def generate_qr(file_path: str) -> None:
    """Genera un código QR para un archivo.

    Args:
        file_path (str): La ruta del archivo para el cual se generará el código QR.

    Returns:
        None
    """
    with open(file_path, 'rb') as f:
        r = requests.post('https://file.io', files={'file': f})
        link = r.json()['link']
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.show()


def writer(encripted) -> None:

    print("Ingrese la \033[4mruta de destino\033[0m: ")
    out = input("> ")
    while out == "":
        print("La ruta ingresada es invalida")
        out = input("\033[31m>\033[0m ")
    check = True
    while check:
        try:
            with open(out, "w") as let:
                let.write(encripted)
                check = False
        except IsADirectoryError:
            print("La ruta ingresada es un directorio")
            out = input("\033[31m>\033[0m ")
        except:
            print("La ruta ingresada es invalida")
            out = input("\033[31m>\033[0m ")
    print("Ingrese 1 para generar un qr del archivo")
    print("\033[1mDe lo contrario,\033[0m el programa terminara: ")
    user = input(("> "))
    if user == "1":
        generate_qr(out)
    return "\033[46mEl programa termino correctamente\033[0m"


def main():
    print("≡≡Encriptador de Cifrado de Vigenère≡≡")
    msj = path_picker()
    key = keys()
    key = same_len(key, msj)
    msj, key = num_covert(key, msj)
    encripted = encripter(key, msj, "+")
    print(writer(encripted))


if __name__ == "__main__":
    main()
