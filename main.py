import os
import sys
from db import QueryDB


def clear():
    if sys.platform == 'linux':
        os.system('clear')
    else:
        os.system('cls')


def version():
    ver = '1.5 nome a definir'
    print('Numeron Network {}\n'.format(ver))


def get_codloja():
    codloja = input(
        'Digite o codloja da loja ou 00 para sair(? configuração): ').upper()
    if codloja == '00':
        sys.exit(0)
    elif codloja == '?':
        input('configuração')
    return codloja


if __name__ == '__main__':
    while True:
        clear()
        version()
        get_codloja()

