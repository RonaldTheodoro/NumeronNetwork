from db import QueryDB


DB = QueryDB()

DB.SearchCodLojaDB('88')
print(DB.ShowLastQuery('one'))

DB.SearchSupDB('JOAO')
print(DB.ShowLastQuery('all'))
