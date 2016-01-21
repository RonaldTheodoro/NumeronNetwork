import sqlite3
import os


class DBsqlite(object):

    """
    Verifica, conecta e controla o banco de dados sqlite3
    """

    def __init__(self, nameDB):
        self.DBname = os.getcwd() + '\\' + nameDB
        try:
            self.conn = sqlite3.connect(self.DBname)
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
        print('Salvando as alterações em {}'.format(self.DBname))
        self.conn.commit()

    # Encera a conexão com o DB
    def CloseDB(self):
        print('Encerando conexão com {}'.format(self.DBname))
        self.conn.close()
