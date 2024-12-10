# Matriz da cifra ADFGVX (6x6), usando letras e dígitos
MATRIZ_ADFGVX = [
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['G', 'H', 'I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P', 'Q', 'R'],
    ['S', 'T', 'U', 'V', 'W', 'X'],
    ['Y', 'Z', '0', '1', '2', '3'],
    ['4', '5', '6', '7', '8', '9']
]

LETTERS = ['A', 'D', 'F', 'G', 'V', 'X']


def key_processor(key: str):
    return key


def encontrar_posicao(char):
    for i, linha in enumerate(MATRIZ_ADFGVX):
        if char in linha:
            return i, linha.index(char)
    raise ValueError(f"Caractere '{char}' não encontrado na matriz.")


def substituir(texto):
    resultado = ""
    for char in texto.upper():
        if char.isspace():
            resultado += " "
        elif char.isalnum():
            linha, coluna = encontrar_posicao(char)
            resultado += LETTERS[linha] + LETTERS[coluna]
    return resultado


def transpor(texto, chave):
    colunas = sorted((chave[i], i) for i in range(len(chave)))
    texto_matriz = [texto[i:i + len(chave)]
                    for i in range(0, len(texto), len(chave))]

    ultimo_tamanho = len(texto_matriz[-1])
    padding = len(chave) - ultimo_tamanho
    if padding > 0:
        texto_matriz[-1] += 'X' * padding

    transposto = ""
    for _, indice in colunas:
        for linha in texto_matriz:
            if indice < len(linha):
                transposto += linha[indice]

    transposto += str(padding)
    return transposto


def cipher(entrada, chave):
    substituido = substituir(entrada)
    texto_cifrado = transpor(substituido, chave)

    return texto_cifrado


def inverter_chave(chave):
    return sorted(range(len(chave)), key=lambda k: chave[k])


def destranspor(texto, chave):
    colunas = len(chave)
    linhas = len(texto) // colunas
    sobra = len(texto) % colunas
    indices = inverter_chave(chave)
    matriz = [''] * colunas

    posicao = 0
    for i, indice in enumerate(indices):
        num_linhas = linhas + 1 if i < sobra else linhas
        matriz[indice] = texto[posicao:posicao + num_linhas]
        posicao += num_linhas

    return ''.join(''.join(linha) for linha in zip(*matriz))


def reverter_substituicao(texto):
    resultado = ""
    i = 0
    while i < len(texto) - 1:
        if texto[i].isspace():
            resultado += " "
            i += 1
        else:
            linha = LETTERS.index(texto[i])
            coluna = LETTERS.index(texto[i + 1])
            resultado += MATRIZ_ADFGVX[linha][coluna]
            i += 2
    return resultado


def decipher(entrada, chave):
    if not entrada[-1].isdigit():
        raise ValueError("O texto cifrado não contém um padding válido.")

    padding = int(entrada[-1])
    entrada = entrada[:-1]

    if len(entrada) % 2 != 0:
        raise ValueError(
            "O texto cifrado não tem um número par de caracteres após remoção do padding.")

    transposto = destranspor(entrada, chave)

    if padding > 0:
        transposto = transposto[:-padding]

    texto_decifrado = reverter_substituicao(transposto)

    return texto_decifrado
