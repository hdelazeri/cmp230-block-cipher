def key_processor(key: str):
    return (ord(key[0]) % ((len(key) // 5)) + 3)


def cipher(text: str, key: int) -> str:
    if key <= 0:
        raise ValueError("key should be a positive integer")

    chars = text[:]
    rails = [''] * key

    current_rail = 0
    direction = 1

    for i in range(len(chars)):
        if not chars[i].isalnum():
            continue

        rails[current_rail] += chars[i]

        if current_rail == key - 1 and direction == 1:
            direction = -1

        if current_rail == 0 and direction == -1:
            direction = 1

        current_rail += direction

    joined = ''.join(rails)
    result = [''] * len(chars)

    for i in range(len(chars)):
        if chars[i].isalnum():
            result[i] = joined[0]
            joined = joined[1:]
        else:
            result[i] = chars[i]

    return ''.join(result)


def decipher(text: str, key: int) -> str:
    if key <= 0:
        raise ValueError("key should be a positive integer")

    chars = text[:]
    rails = [[' ' for _ in range(len(chars))] for _ in range(key)]

    considered_chars = list(filter(lambda x: x.isalnum(), chars))

    rail = 0
    direction = 1

    for i in range(len(considered_chars)):
        rails[rail][i] = '*'

        if rail == key - 1 and direction == 1:
            direction = -1

        if rail == 0 and direction == -1:
            direction = 1

        rail += direction

    rail = 0
    idx = 0

    for i in range(key):
        for j in range(len(considered_chars)):
            if rails[i][j] == "*":
                rails[i][j] = considered_chars[idx]
                idx += 1

    result = ''
    idx = 0

    for i in range(len(chars)):
        if chars[i].isalnum():
            result += rails[rail][idx]

            if rail == key - 1 and direction == 1:
                direction = -1

            if rail == 0 and direction == -1:
                direction = 1

            rail += direction
            idx += 1
        else:
            result += chars[i]

    return result
