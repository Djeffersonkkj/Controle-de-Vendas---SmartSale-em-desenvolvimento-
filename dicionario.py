'''
aprendendo e mudando o sistema para dicionário
'''

produtos = {}


while True:
    print('------------------SMARTBIZ------------------\n')
    print('1 |PRODUTOS')
    print('2 |VENDAS')
    print('0 |SAIR')
    print()
    op = int(input('SELECIONE UMA OPÇÃO: '))
    
    if op == 1:
            while True:
                print('------------------PRODUTOS------------------\n')
                print('1 |CADASTRAR')
                print('2 |LISTA')
                print('3 |EDITAR')
                print('0 |VOLTAR')
                print()
                op_2 = int(input('SELECIONE UMA OPÇÃO: '))
            
                if op_2 == 1:
                    for i in range(1):
                        print('--------------CADASTRAR PRODUTO--------------\n')
                        produto = input('NOME: ')
                        nome = produto
                        estoque = int(input('EM ESTOQUE: '))
                        valor_compra = float(input('VALOR DE COMPRA: R$'))
                        valor_venda = float(input('VALOR A SER VENDIDO: R$'))
                        produto = {'nome': nome, 'estoque': estoque,
                                   'valor_compra': valor_compra, 'valor_venda': valor_venda,
                                   'v_compra_total': valor_compra * estoque
                                   }
                        produtos[nome] = produto
                elif op_2 == 0:
                    break
                        
    elif op == 0:
        pesquisa = input()
        print(produtos[pesquisa])
        break