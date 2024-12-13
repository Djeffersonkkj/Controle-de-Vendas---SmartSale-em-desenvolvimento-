'''
aprendendo e mudando o sistema para dicionário

produtos não terem o mesmo id
'''
import os
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

produtos = {}
limpar()
while True:
    print('------------------SMARTBIZ------------------\n')
    print('1 |PRODUTOS')
    print('2 |VENDAS\n')
    print('0 |SAIR')
    op = int(input('SELECIONE UMA OPÇÃO: '))
    
#MENU DE PRODUTOS
    if op == 1:
        limpar()
        while True:
            print('------------------PRODUTOS------------------\n')
            print('1 |CADASTRAR')
            print('2 |PESQUISAR')
            print('3 |LISTA')
            print('4 |EDITAR\n')
            print('0 |VOLTAR')
            op_2 = int(input('SELECIONE UMA OPÇÃO: '))
            
            if op_2 == 1: #CADASTRAR
                limpar()
                for i in range(1):
                    print('--------------CADASTRAR PRODUTO--------------\n')
                    produto_id = int(input('(o id será importante para buscar o produto)\nID DO PRODUTO: '))
                        
                    if produtos.get(produto_id) is None:
                        nome = input('NOME: ')
                        estoque = int(input('EM ESTOQUE: '))
                        valor_compra = float(input('VALOR DE COMPRA: R$'))
                        valor_venda = float(input('VALOR A SER VENDIDO: R$'))
                        produto = {'produto_id': produto_id, 'nome': nome, 'estoque': estoque,
                                    'valor_compra': valor_compra, 'valor_venda': valor_venda,
                                    'v_compra_total': valor_compra * estoque, 'q_vendas': 0,
                                    't_vendas': 0
                                    }
                        produtos[produto_id] = produto
                        limpar()
                    else:
                        limpar()
                        print('ID JÁ CADASTRADO NO SISTEMA!')
                            
            elif op_2 == 2: #PESQUISAR
                limpar()
                if not produto:
                    print('NENHUM PRODUTO CADASTRADO!')
                else:
                    print('---------------PESQUISAR---------------\n')
                    pesquisa = int(input('DIGITE O ID DO PRODUTO: '))
                    if produtos.get(pesquisa) is None:
                        limpar()
                        print('ID ERRADO OU INEXISTENTE!\n')
                    else:
                        limpar()
                        print(f'-------------------{produtos[pesquisa].get("nome", "nome inexistente").upper()}-------------------\n')
                        print(f'ESTOQUE: {produtos[pesquisa]["estoque"]}')
                        print(f'VALOR DE COMPRA: {produtos[pesquisa]["valor_compra"]}')
                        print(f'VALOR DE VENDA: {produtos[pesquisa]["valor_venda"]} | VENDAS: {produtos[pesquisa]["q_vendas"]} - {produtos[pesquisa]["t_vendas"]}')
                        
            elif op_2 == 3: #LISTA
                if not produto:
                    limpar()
                    print('NENHUM PRODUTO CADASTRADO!')
                else:
                    limpar()
                    print('--------------------LISTA--------------------\n')
                    for chave, dados in produtos.items():
                        print(f"NOME: {dados['nome']} ({dados['produto_id']}) | ESTOQUE: {dados['estoque']}x | VALOR DE VENDA: R${dados['valor_venda']:.2f} | \
VENDAS: {dados['q_vendas']}   TOTAL: {dados['t_vendas']}")
                        print('---------------------------------------------------------------------')
                            
            elif op_2 == 4: #EDITAR
                if not produto:
                    limpar()
                    print('NENHUM PRODUTO CADASTRADO!')
                else:
                    limpar()
                    print('------------------EDITAR------------------\n')
                    pesquisa = int(input('DIGITE O ID DO PRODUTO: '))
                        
                    if produtos.get(pesquisa) is None:
                        limpar()
                        print('ID ERRADO OU INEXISTENTE!\n')
                    else:
                        while True:
                            limpar()
                            print(f'------------------EDITAR |{produtos[pesquisa].get("nome", "nome inexistente").upper()}------------------\n')
                            print(f'1 |EDITAR - {produtos[pesquisa].get("nome", "nome inexistente")}')
                            print(f'2 |EXCLUIR - {produtos[pesquisa].get("nome", "nome inexistente")}\n')
                            print('0 |VOLTAR')
                            op_3 = int(input('SELECIONE UMA OPÇÃO: '))
                                
                            if op_3 == 1:
                                limpar()
                                print(f'------------------EDITAR |{produtos[pesquisa].get("nome", "nome inexistente").upper()}------------------\n')
                                print(f'--------------------{produtos[pesquisa].get("nome", "nome inexistente").upper()}--------------------\n')
                                print(f'1 |NOME - {produtos[pesquisa].get("nome", "nome inexistente")}')
                                print(f'2 |EM ESTOQUE - {produtos[pesquisa].get("estoque", "estoque inexistente")}')
                                print(f'3 |VALOR DE COMPRA - {produtos[pesquisa].get("valor_compra", "valor de compra inexistente")}')
                                print(f'4 |VALOR DE VENDA - {produtos[pesquisa].get("valor_venda", "valor de venda inexistente")}')
                                print(f'5 |QUANTIDADE DE VENDAS - {produtos[pesquisa].get("q_vendas", "vendas inexistentes")}')
                                print(f'6 |TOTAL DO VALOR DE VENDAS - {produtos[pesquisa].get("t_vendas", "vendas inexistentes")}\n')
                                print('0 |VOLTAR')
                                op_4 = int(input('ELECIONE UMA OPÇÃO: '))

                                if op_4 == 1:
                                    novo_valor = input('NOME: ')
                                    produtos[pesquisa]["nome"] = novo_valor
                                    limpar()
                                elif op_4 == 2:
                                    novo_valor = input('ESTOQUE: ')
                                    produtos[pesquisa]["estoque"] = novo_valor
                                    limpar()
                                elif op_4 == 3:
                                    novo_valor = input('VALOR DE COMPRA: ')
                                    produtos[pesquisa]["valor_compra"] = novo_valor
                                    limpar()
                                elif op_4 == 4:
                                    novo_valor = input('VALOR DE VENDA: ')
                                    produtos[pesquisa]["valor_venda"] = novo_valor
                                    limpar()
                                elif op_4 == 5:
                                    novo_valor = input('QUANTIDADE DE VENDAS: ')
                                    produtos[pesquisa]["q_vendas"] = novo_valor
                                    limpar()
                                elif op_4 == 6:
                                    novo_valor = input('TOTAL DO VALOR DE VENDAS: ')
                                    produtos[pesquisa]["t_vendas"] = novo_valor
                                    limpar()
                                elif op_4 == 0:
                                    limpar()
                                    break
                                else:
                                    limpar()
                                    print('OPÇÃO INVÁLIDA!')
                            elif op_3 == 2:
                                limpar()
                                excluir = input(f'DIGITE "SIM" PARA EXCLUIR {produtos[pesquisa]["nome"].upper()}: ')
                                if excluir in ['SIM', 'Sim', 'sim', 's', 'S']:
                                    limpar()
                                    print(f'{produtos[pesquisa]["nome"].upper()} EXCLUÍDO COM SUCESSO!')
                                    del produtos[pesquisa]
                                    break
                                else:
                                    limpar()
                                    print(f'{produtos[pesquisa]["nome"].upper()} NÃO FOI EXCLUÍDO!')
                            elif op_3 == 0:
                                limpar()
                                break
                            else:
                                limpar()
                                print('OPÇÃO INVÁLIDA!')
            elif op_2 == 0:
                limpar()
                break
            else:
                limpar()
                print('OPÇÃO INVÁLIDA!')
    
    
#MENU DE VENDAS
    elif op == 2:
        while True:
            limpar()
            print('------------------VENDAS------------------\n')
            print('1 |VENDER')
            print('2 |HISTÓRICO')
            print('3 |RELATÓRIO')
            print('0 |VOLTAR\n')
            
            op_2 = int(input('SELECIONE UMA OPÇÃO: '))
            if op_2 == 1:
                if not produto:
                    limpar()
                    print('NENHUM PRODUTO CADASTRADO!')
                else:
                    limpar()
                    print('------------------VENDER------------------\n')
                    pesquisa = int(input('DIGITE O ID DO PRODUTO: '))
                        
                    if produtos.get(pesquisa) is None:
                        limpar()
                        print('ID ERRADO OU INEXISTENTE!\n')
                    else:
                        while True:
                            limpar()
        
            elif op_2 == 0:
                    limpar()
                    break
        
    elif op == 0:
        limpar()
        print("VOCÊ SAIU DO SISTEMA!")
        break
    else:
        limpar()
        print('OPÇÃO INVÁLIDA!')