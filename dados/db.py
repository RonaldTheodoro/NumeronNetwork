import sqlite3
import os


class DB(object):

    """
        Verifica, conecta e controla o banco de dados sqlite3
    """

    def __init__(self, nameDB):
        if os.path.exists('lojas.db'):
            self.conn = sqlite3.connect(nameDB)
            self.cursor = self.conn.cursor()
        else:
            print('Banco de dados corrompido ou não encontrado')
            return False

    # Recebe uma string e executa o comando no DB
    def ExecuteDB(self, command):
        self.cursor.execute(command)

    # Retorna o resultado de uma consulta
    def FetchOneDB(self):
        return self.cursor.fetchone()

    # Retorna varios resultados de uma consulta
    def FetchAllDB(self):
        return self.cursor.fetchall()

    # Salva uma alteração no DB
    def CommitDB(self):
        self.conn.commit()

    # Encera a conexão com o DB
    def CloseDB(self):
        self.conn.close()


class QueryDB(object):

    """
        executa as consultas no DB
    """

    def __init__(self):
        self.DB = DB('lojas.db')

    # Recebe um codigo de loja efetua a consulta no DB
    def SearchCodLojaDB(self, codloja):
        command = 'SELECT * FROM lojas WHERE codloja = "{}"'.format(codloja)
        DB.ExecuteDB(command)

    # Recebe o tipo da busca e retorna o resultado
    def ShowLastQuery(self, typequery):
        if typequery == 'one':
            print(DB.FetchOneDB())
        elif typequery == 'all':
            print(DB.FetchAllDB())
