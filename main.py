from menu import menu
from menu import clean
from DB.DB import DBsqlite


def create_dict(infloja):
    dictloja = {}

    dictloja['codloja'] = infloja[1]
    dictloja['nome'] = infloja[2]
    dictloja['uf'] = infloja[3]
    dictloja['cidade'] = infloja[4]
    dictloja['cnpj'] = infloja[5]
    dictloja['grife'] = infloja[6]
    dictloja['supervisor'] = infloja[7]
    dictloja['ip1'] = infloja[8]
    dictloja['ip2'] = infloja[9]
    dictloja['roteador'] = infloja[10]
    dictloja['sonicwall'] = infloja[11]

    return dictloja


def search_store(codloja):
    db = DBsqlite('Database\\lojas.db')
    db.ExecuteDB('SELECT * FROM lojas WHERE codloja = {}'.format(codloja))
    infloja = db.FetchOneDB()
    if infloja is None:
        return None
    else:
        return create_dict(infloja)
    db.CloseDB()


def test_ping(ip):
    Ping = TPing()
    Ping.TestPing(ip)


def vnc_access(ip):
    vnc = VNC()
    vnc.VNCAccess(ip, '01')


if __name__ == '__main__':
    _version_ = '1.5 Gimmick Puppet Giant Grinder'

    while True:
        clean()
        print('Numeron Network Version: {}'.format(_version_))

        codloja = input('\nDigite o codigo da loja(00 para sair): ')

        if codloja == '00':
            break
        elif codloja == '?':
            input('Configuração')
        else:
            dictloja = search_store(codloja)

            menu(dictloja)
