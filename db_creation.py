# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 21:21:20 2022

@author: EdenPereiradaSilva
"""

import sqlite3 as conector

#conecxao com banco de dados
conexao = conector.connect('books.db')

#criando cursor para executar comandos
cursor = conexao.cursor()
comando = """
                 CREATE TABLE BOOK(
                 BO_SQ_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                 BO_NM_TITLE TEXT NOT NULL,
                 BO_DS_CATEGORY TEXT NOT NULL,
                 BO_NR_STARS INTEGER,
                 BO_NR_PRICE REAL,
                 BO_IN_STOCK TEXT DEFAULT 'not in stock' not null
                 )   ;

"""
cursor.execute(comando)

conexao.commit()
cursor.close()

conexao.close()