def key_processor(key: str):
    return key


def cipher(text, key):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    key = key.upper()
    texto_cifrado = []

    chave_expandida = (key * (len(text) // len(key) + 1))[:len(text)]

    for i in range(len(text)):
        if text[i] in alfabeto:
            pos_texto = alfabeto.find(text[i])
            pos_chave = alfabeto.find(chave_expandida[i])
            pos_cifrada = (pos_chave - pos_texto) % len(alfabeto)
            texto_cifrado.append(alfabeto[pos_cifrada])
        else:
            texto_cifrado.append(text[i])

    return ''.join(texto_cifrado)


def decipher(text, key):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    key = key.upper()
    texto_decifrado = []

    chave_expandida = (key * (len(text) // len(key) + 1))[:len(text)]

    for i in range(len(text)):
        if text[i] in alfabeto:
            pos_cifrada = alfabeto.index(text[i])
            pos_chave = alfabeto.index(chave_expandida[i])
            pos_decifrada = (pos_chave - pos_cifrada) % len(alfabeto)
            texto_decifrado.append(alfabeto[pos_decifrada])
        else:
            texto_decifrado.append(text[i])

    return ''.join(texto_decifrado)
