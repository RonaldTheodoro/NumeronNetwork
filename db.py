import sqlite3
import os


class DB(object):

    """
        Verifica, conecta e controla o banco de dados sqlite3
    """

    def __init__(self, nameDB):
        nameDB = os.getcwd() + '/db/' + nameDB
        try:
            self.conn = sqlite3.connect(nameDB)
            self.cursor = self.conn.cursor()
        except sqlite3.Error:
            print('Banco de dados corrompido ou não encontrado')
            return False

    # Recebe uma string e executa o comando no DB
    def ExecuteDB(self, c):
        self.cursor.execute(c)

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
        if self.DB == False:
            input('Banco de dados não encontrado')

    # Recebe um codigo de loja efetua a consulta no DB
    def SearchCodLojaDB(self, codloja):
        c = 'SELECT * FROM lojas WHERE codloja = "{}"'
        self.DB.ExecuteDB(c.format(codloja))

    # Recebe o nome de um supervisor e busca suas lojas
    def SearchSupDB(self, sup):
        c = 'SELECT codloja FROM lojas WHERE supervisor LIKE "%{}%"'
        self.DB.ExecuteDB(c.format(sup.upper()))

    # Retorna uma lista de lojas
    def ShowLastQuery(self, typequery):
        # Retorna uma tupla com os dados de uma loja
        if typequery == 'one':
            return self.DB.FetchOneDB()

        # Retorna uma lista de tuplas com os dados de varias lojas
        elif typequery == 'all':
            return self.DB.FetchAllDB()
