import argparse
import sys

import rail_fence
import adfgvx
import alberti


def block(action: str, content: str, key: str):
    ciphers = [rail_fence, adfgvx, alberti]

    r = range(len(ciphers)) if action == 'cipher' else range(
        len(ciphers) - 1, 0 - 1, -1)

    result = content

    for c in r:
        key_func = getattr(ciphers[c], 'key_processor')
        k = key_func(key)

        func = getattr(ciphers[c], action)
        result = func(result, k)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="rail-fence",
        description="Simple demo of the rail-rence cipher")

    parser.add_argument('action', choices=[
                        'cipher', 'decipher'], help='action to do')
    parser.add_argument('-i', '--input', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin, help="input file (default stdin)")
    parser.add_argument('-o', '--output', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout, help="output file (default stdout)")
    parser.add_argument('-k', '--key', help="key value",
                        type=str, required=True)

    args = parser.parse_args()

    r = args.input.read().upper()

    for i in range(5):
        r = block(args.action, r, args.key)

    print(r, file=args.output, end='')
