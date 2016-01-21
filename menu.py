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
    print('Municipio: {} UF: {}'.format(dicloja['cidade'], dicloja['uf']))


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
    ping = TPing()
    while True:
        clean()
        show_info(dicloja)
        op = options()

        if op == '0':
            break
        elif op == '1':
            ping.TestPing(dicloja['ip1'])
        elif op == '2':
            ping.TestPing(dicloja['ip2'])
        elif op == '3':
            ping.TestPing(dicloja['roteador'])
            if dicloja['sonicwall'] != 'NULL':
                ping.TestPing(dicloja['sonicwall'])
        elif op == '4':
            pass
        elif op == '5':
            pass
        elif op == '6':
            pass
        elif op == '7':
            pass
        else:
            input('Opção invalida')
