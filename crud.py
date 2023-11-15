from biblioteca import *

while True:
    resp = "S"
    print("----------Menu Principal----------"
          "\n1. Adicionar informações na tabela\n"
          "2. Visualizar informações da tabela\n"
          "3. Atualizar informações da tabela\n"
          "4. Deletar informações da tabela\n"
          "5. Sair do sistema")
    resposta = input("Informe sua opção: ")
    if resposta == "1":
        while resp == "S":
            consultar_tabela = """SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE';"""
            cursor.execute(consultar_tabela)
            print("-------------------")
            print("Tabelas disponíveis")
            for x in cursor.fetchall():
                print(f"1 - {x[0]}")
            tabela = input("Escolha a tabela: ")
            if tabela == "1":
                print(f"-----tabela VENDAS selecionada-----")
                cliente = input("Informe o nome do cliente: ")
                produto = input("Informe o produto: ")
                data_venda = input("Informe a data atual: ")
                preco = float(input("Informe o valor do produto: "))
                quantidade = int(input("Informe a quantidade: "))
                comando = f"""insert into VENDAS (cliente, produto, data_venda, preco, quantidade)
                VALUES
                    ('{cliente}', '{produto}', '{data_venda}', {preco}, {quantidade})"""
                cursor.execute(comando)
                cursor.commit()
                print("Valores adicionados na tabela vendas!")
                print("-------------------------------------")
                resp = input("Deseja adicionar dados novamente? [S/N]: ")
                while (resp != "S") and (resp != "N" and resp != "n"):
                    resp = input("Opção inválida, escolha novamente [S/N]: ")
        print("Retornando ao menu...")
    elif resposta == "2":
        while resp == "S":
            tabela = input("Informe a tabela: ")
            print(f"-----tabela {tabela} selecionada.-----")
            comando = f'SELECT * FROM {tabela};'
            cursor.execute(comando)
            for x in cursor.fetchall():
                print(f"ID: {x[0]}")
                print(f"Cliente: {x[1]}")
                print(f"Produto: {x[2]}")
                print(f"Data da venda: {x[3]}")
                print(f"Preço: R${x[4]}")
                print(f"Quantidade: {x[5]}")
                print("----------------------")
            resp = input("Deseja visualizar dados novamemte? [S/N]: ")
            while (resp != "S") and (resp != "N" and resp != "n"):
                resp = input("Opção inválida, escolha novamente [S/N]: ")
        print("Retornando ao menu...")
    elif resposta == "3":
        while resp == "S":
            tabela = input("Informe a tabela: ")
            print(f"-----tabela {tabela} selecionada-----")
            coluna1 = input("Informe o nome da coluna para alteração: ")
            valor_coluna = input("Insira o novo valor: ")
            coluna2 = input("Informe a coluna que será alterada: ")
            condicao = input("Onde o valor é equivalente a: ")
            comando = f"""UPDATE {tabela} SET {coluna1} = '{valor_coluna}' WHERE {coluna2} = '{condicao}'"""
            cursor.execute(comando)
            conexao.commit()
            resp = input("Deseja visualizar dados novamemte? [S/N]: ")
            while (resp != "S") and (resp != "N" and resp != "n"):
                resp = input("Opção inválida, escolha novamente [S/N]: ")
        print("Retornando ao menu...")
    elif resposta == "4":
        tabela = input("Informe a tabela: ")
        print(f"-----tabela {tabela} selecionada-----")
        coluna1 = input("Informe o nome da coluna: ")
        condicao = input("Onde o valor é equivalente a: ")
        comando = f"""DELETE FROM {tabela} WHERE {coluna1} = '{condicao}'"""
        cursor.execute(comando)
        conexao.commit()
        resp = input("Deseja visualizar dados novamemte? [S/N]: ")
        while (resp != "S") and (resp != "N" and resp != "n"):
            resp = input("Opção inválida, escolha novamente [S/N]: ")
        print("Retornando ao menu...")
    elif resposta == "5":
        print("Saindo do sistema...")
        cursor.close()
        conexao.close()
        break
    else:
        print("Opção inválida, tente novamente!")
