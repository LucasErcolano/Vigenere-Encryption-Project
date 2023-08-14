from matplotlib.pyplot import subplots, ylim, legend, tight_layout, show, figure, bar, subplot, title, subplots_adjust, rcParams
from elf import elf, abc, legenda, elf0
from seaborn import set_style as sns
from uno import path_picker
from dos import descypher


def clean_txt(txt: str) -> str:
    """Elimina los caracteres no alfabéticos de una cadena.

    Args:
        txt (str): La cadena de entrada.

    Returns:
        str: La cadena limpia.
    """
    txt = ''.join(c for c in txt if c.isalpha())
    return txt


def txt_split(txt: str) -> list:
    """Divide una cadena en grupos de caracteres.

    Args:
        txt (str): La cadena de entrada.

    Returns:
        list: Una lista de listas que contiene los grupos de caracteres.
    """
    listg = [[txt[start::k] for start in range(k)] for k in range(1, 31)]
    return listg


def ioc(listg: list, txt: str, abc: list) -> list:
    """Calcula el índice de coincidencia para cada grupo de caracteres.

    Args:
        listg (list): Una lista de listas que contiene los grupos de caracteres.
        txt (str): La cadena original.
        abc (list): Una lista con los caracteres del diccionario ingles.

    Returns:
        list: Una lista con el índice de coincidencia para cada grupo.
    """
    prompts = []
    for clave in listg:
        grupos = 0
        for group in clave:
            n = len(group)
            if n > 1:
                prom = sum(group.count(c) * (group.count(c) - 1) for c in abc)
                prom /= (n * (n - 1))
                grupos += prom
        grupos /= len(clave)
        prompts.append(grupos)
    return prompts


def graphicator(prompts: list, legenda: list) -> None:
    """Genera un gráfico de barras con los índices de coincidencia.

    Args:
        prompts (list): Una lista con el índice de coincidencia para cada grupo.
        legenda (list): Una lista con las etiquetas para el eje x del gráfico.

    Returns:
        None
    """
    sns('darkgrid')
    figure, ax = subplots()
    ax.bar(legenda, prompts)
    ax.axhline(y=0.0686, color='#181818', linestyle='--', label='6.86%')
    ax.axhline(y=0.0385, color='#343434', linestyle='--', label='3.85%')
    ax.set_title('Análisis de similaridad')
    ax.set_xlabel('Longitud de la clave')
    ax.set_ylabel('Índice de coincidencia')
    ylim(0, 0.07)
    legend()
    tight_layout()
    show()


def words_frequency(dic: dict) -> None:
    """Genera un gráfico de barras de la frecuencia de las palabras en ingles.

    Args:
        dic (dict): Diccionario con las palabras como claves y su frecuencia como valores.

    Returns:
        None
    """
    letras = list(dic.keys())
    frecuencia = list(dic.values())
    figure(figsize=(15, 10))
    subplot(3, 2, 1)
    bar(letras, frecuencia)
    title("Ingles", fontsize=8)


def count(group: list, abc: list) -> list:
    """Calcula la frecuencia de las letras en cada grupo.

    Args:
        group (list): Una lista que contiene los grupos de caracteres.
        abc (list): Una lista con los caracteres alfabéticos.

    Returns:
        list: Una lista de diccionarios que contienen la frecuencia de las letras para cada grupo.
    """

    letter_frequencies = []
    for j in group:
        apperence = {i: j.count(i) / len(j) for i in abc}
        letter_frequencies.append(apperence)
    return letter_frequencies


def app(lis: list, elf0: dict) -> None:
    """Genera gráficos de barras para visualizar el recuento de letras en una lista de diccionarios.

    Args:
        lis (list): Una lista de diccionarios que contienen el recuento de letras.
        elf0 (dict): Un diccionario vacío para almacenar temporalmente el recuento de letras.

    Returns:
        None
    """
    rcParams['figure.constrained_layout.use'] = True
    bar_labels = ["IoC"]
    counter = 2
    for i in lis:
        for j, k in i.items():
            elf0[j] = k
        subplot(3, 2, counter)
        title(f"Letra {counter - 1} de la clave", fontsize=8)
        counter += 1
        x = elf0.keys()
        y = elf0.values()
        bars = bar(x, y)
        for bard, label in zip(bars, bar_labels):
            bard.set_label(label)
        legend()
    subplots_adjust(wspace=0.3, hspace=0.3)
    show()


def find_encryption_key(lis: list) -> str:
    """Encuentra la clave utilizada para encriptar el texto original.

    Args:
        lis (list): Una lista de diccionarios que contienen el recuento de letras para cada grupo.

    Returns:
        str: La clave utilizada para encriptar el texto original.
    """
    superlista = []
    for i in lis:
        aux = []
        for values in i.values():
            aux.append(values)
        superlista.append(aux)
    key = ""
    for i in superlista:
        key += chr((((i.index(max(i)))-4) % 26)+97)
    return key


def main():
    """Ejecuta el programa principal.

    Esta función ejecuta el programa principal utilizando las funciones path_picker,
    clean_txt, txt_split, ioc, graphicator, words_frequency,
    count, app y find_encryption_key.
    """
    txt1 = path_picker()
    txt = clean_txt(txt1)
    listg = txt_split(txt)
    prompts = ioc(listg, txt, abc)
    graphicator(prompts, legenda)
    words_frequency(elf)
    lis = count(listg[4], abc)
    test = app(lis, elf0)
    key = find_encryption_key(lis)
    print("Clave utilizada para encriptar:", key)
    print("Ingrese 1 para desencriptar el archivo")
    print("\033[1mDe lo contrario\033[0m, el programa terminara: ")
    user = input(("> "))
    if user == "1":
        print("≡≡Desencriptador de Cifrado de Vigenère≡≡")
        descypher(key, txt1)
    else:
        print("\033[46mEl programa termino correctamente\033[0m")


if __name__ == "__main__":
    main()
