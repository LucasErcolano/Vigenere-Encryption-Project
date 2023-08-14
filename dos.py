import uno as uno


def descypher(key: str, msj: str) -> None:
    """Desencripta un mensaje cifrado con el cifrado de Vigenère.

    Args:
        key (str): La clave utilizada para cifrar el mensaje.
        msj (str): El mensaje cifrado.

    Returns:
        None
    """
    key = uno.same_len(key, msj)
    msj, key = uno.num_covert(key, msj)
    encripted = uno.encripter(key, msj, '-')
    print(uno.writer(encripted))


def main() -> None:
    """Función principal que ejecuta el desencriptador de cifrado de Vigenère.

    Returns:
        None
    """
    print("≡≡Desencriptador de Cifrado de Vigenère≡≡")
    msj = uno.path_picker()
    key = uno.keys()
    descypher(key, msj)


if __name__ == "__main__":
    main()
