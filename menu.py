import os
import sys
from DB.DB import DBsqlite
from TPing.TPing import TPing
from VNC.VNC import VNC


def clean():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clean')


def show_info(dicloja):
    print('Codigo: {} Nome: {}'.format(
        dicloja['codloja'], dicloja['nome']))
    if dicloja['sonicwall'] != 'NULL':
        print('IP1: {} IP2: {} Roteador: {} Sonicwall: {}'.format(
            dicloja['ip1'],
            dicloja['ip2'],
            dicloja['roteador'],
            dicloja['sonicwall']
        ))

    else:
        print('IP1: {} IP2: {} Roteador: {}'.format(
            dicloja['ip1'],
            dicloja['ip2'],
            dicloja['roteador']
        ))
    print('CNPJ: {} Grife: {} Supervisor: {}'.format(
            dicloja['cnpj'],
            dicloja['grife'],
            dicloja['supervisor']
    ))
    print('Municipio: {} UF: {}'.format())


def options():
    print('\n\nEscolha uma opção')
    print('\n(1) Teste de ping Embratel')
    print('(2) Teste de ping VPN')
    print('(3) Teste de ping roteador')
    print('(4) SSH Embratel')
    print('(5) SSH VPN')
    print('(6) VNC Embratel')
    print('(7) VNC VPN')
    print('(0) Sair')

    return input('>>>: ')


def menu(dicloja):
    while True:
        clean()
        show_info(dicloja)
        options()
        input()
        break
