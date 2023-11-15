import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-H8CUGMV\SQLEXPRESS;"
    "Database=APRENDENDO;"
)
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()
