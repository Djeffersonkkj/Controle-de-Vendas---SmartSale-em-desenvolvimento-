'''
O SmartBiz(nome provisório) tem como principal  objetivo
ajudar os comerciantes a gerenciarem melhor as suas ven-
das.

TAREFAS:
    sistema para poder excluir e substituir o espaço por outro produto
    não permitir o mesmo código de pesquisa 2 vezes
    Receber quais produtos estão disponíveis
    A quantidade desses produtos
    Qual foi o custo de produção
    Valor vendido
    Lucro
    Venda todal
    Gastos
'''

maximo = 1000
nmr_pesquisa = [0] * maximo
produto = [''] * maximo
estoque = [0] * maximo
valor_compra = [0] * maximo
v_compra_total = [0] * maximo
valor_venda = [0] * maximo

q_vendas = [0] * maximo
vendas_total = [0] * maximo
pdts_cadastrados = 0

while True:
    print('------------------SMARTBIZ------------------\n')
    print('1 |PRODUTOS')
    print('2 |VENDAS')
    print('0 |SAIR')
    print()
    op = int(input('SELECIONE UMA OPÇÃO: '))
    
    if op == 1:
        try:
            while True:
                print('------------------PRODUTOS------------------\n')
                print('1 |CADASTRAR')
                print('2 |LISTA')
                print('3 |EDITAR')
                print('0 |VOLTAR')
                print()
                op_2 = int(input('SELECIONE UMA OPÇÃO: '))
            
                if op_2 == 1:
                    if pdts_cadastrados < maximo:
                        print('--------------CADASTRAR PRODUTO--------------\n')
                        nmr_pesquisa[pdts_cadastrados] = int(input('CÓDIGO DE PESQUISA: '))
                        produto[pdts_cadastrados] = input('PRODUTO: ')
                        estoque[pdts_cadastrados] = int(input('EM ESTOQUE: '))
                        valor_compra[pdts_cadastrados] = float(input('VALOR DE COMPRA: '))
                        valor_venda[pdts_cadastrados] = float(input('VALOR DE VENDA: '))
                        v_compra_total[pdts_cadastrados] = valor_compra[pdts_cadastrados] * estoque[pdts_cadastrados]
                        print('produto cadastrado com sucesso!')
                        pdts_cadastrados += 1
                    else:
                        print('Limite máximo de cadastros atingido!')
                elif op_2 == 2:
                    if pdts_cadastrados > 0:
                        print('--------------------LISTA--------------------\n')
                        for i in range(pdts_cadastrados):
                            print(f'PRODUTO: {produto[i]} ({nmr_pesquisa[i]})')
                            print(f'ESTOQUE: {estoque[i]}')
                            print(f'VALOR DE COMPRA: {valor_compra[i]} | TOTAL: {v_compra_total[i]}')
                            print(f'VALOR DE VENDA: {valor_venda[i]} | VENDAS: {q_vendas[i]} - {vendas_total[i]}')
                            print('--------------------------------------------')
                    else:
                        print('Nenhum produto cadastrado!\n')
                elif op_2 == 3:
                    if pdts_cadastrados > 0:
                        print('------------------EDITAR------------------\n')
                        pesquisa = int(input('CÓDIGO DE PESQUISA: '))
                        achei = False
                        for i in range(pdts_cadastrados):
                            if pesquisa == nmr_pesquisa[i]:
                                achei = True
                                while True:
                                    print(f'1 |EDITAR - {produto[i]}')
                                    print(f'2 |EXCLUIR - {produto[i]}\n')
                                    print('0 |VOLTAR')
                                    op_3 = int(input('ELECIONE UMA OPÇÃO: '))
                                    if op_3 == 1:
                                        while True:
                                            print(f'--------------------{produto[i].upper()}--------------------\n')
                                            print(f'1 |PRODUTO - {produto[i]}')
                                            print(f'2 |EM ESTOQUE - {estoque[i]}')
                                            print(f'3 |VALOR DE COMPRA - {valor_compra[i]}')
                                            print(f'4 |VALOR DE VENDA - {valor_venda[i]}')
                                            print(f'5 |QUANTIDADE DE VENDAS - {q_vendas[i]}')
                                            print(f'6 |TOTAL DO VALOR DAS VENDAS - {vendas_total[i]}\n')
                                            print('0 | CONCLUIR')
                                            op_4 = int(input('ELECIONE UMA OPÇÃO: '))
                                            
                                            if op_4 == 1:
                                                print('Digite o novo valor ou clique enter para manter o valor atual.\n')
                                                new_produto = input(f'PRODUTO ({produto[i]}): ')
                                                if new_produto.strip():
                                                    try:
                                                        produto[i] = new_produto
                                                        print('Valor atualizado com sucesso!')
                                                    except:
                                                        print('Entrada inválida, valor não atualizado')
                                                else:
                                                    print('Valor mantido!') 
                                            elif op_4 == 2:
                                                print('Digite o novo valor ou clique enter para manter o valor atual.\n')
                                                new_estoque = input(f'EM ESTOQUE ({estoque[i]}): ')
                                                if new_estoque.strip():
                                                    try:
                                                        estoque[i] = int(new_estoque)
                                                        v_compra_total[i] = valor_compra[i] * estoque[i]
                                                        print('Valor atualizado com sucesso!')
                                                    except:
                                                        print('Entrada inválida, valor não atualizado')
                                                else:
                                                    print('Valor mantido!') 
                                            elif op_4 == 3:
                                                print('Digite o novo valor ou clique enter para manter o valor atual.\n')
                                                new_valor_compra = input(f'VALOR DE COMPRA ({valor_compra[i]}): ')
                                                if new_valor_compra.strip():
                                                    try:
                                                        valor_compra[i] = float(new_valor_compra)
                                                        v_compra_total[i] = valor_compra[i] * estoque[i]
                                                        print('Valor atualizado com sucesso!')
                                                    except:
                                                        print('Entrada inválida, valor não atualizado')
                                                else:
                                                    print('Valor mantido!') 
                                            elif op_4 == 4:
                                                print('Digite o novo valor ou clique enter para manter o valor atual.\n')
                                                new_valor_venda = input(f'VALOR DE VENDA ({valor_venda[i]}): ')
                                                if new_valor_venda.strip():
                                                    try:
                                                        valor_venda[i] = float(new_valor_venda)
                                                        print('Valor atualizado com sucesso!')
                                                    except:
                                                        print('Entrada inválida, valor não atualizado')
                                                else:
                                                    print('Valor mantido!') 
                                            elif op_4 == 5:
                                                print('Digite o novo valor ou clique enter para manter o valor atual.\n')
                                                new_q_vendas = input(f'QUANTIDADE DE VENDAS ({q_vendas[i]}): ')
                                                if new_q_vendas.strip():
                                                    try:
                                                        q_vendas[i] = int(new_q_vendas)
                                                        print('Valor atualizado com sucesso!')
                                                    except:
                                                        print('Entrada inválida, valor não atualizado')
                                                else:
                                                    print('Valor mantido!') 
                                            elif op_4 == 6:
                                                print('Digite o novo valor ou clique enter para manter o valor atual.\n')
                                                new_vendas_total = input(f'TOTAL DO VALOR DAS VENDAS ({vendas_total[i]}): ')
                                                if new_vendas_total.strip():
                                                    try:
                                                        vendas_total[i] = float(new_vendas_total)
                                                        print('Valor atualizado com sucesso!')
                                                    except:
                                                        print('Entrada inválida, valor não atualizado')
                                                else:
                                                    print('Valor mantido!') 
                                            elif op_4 == 0:
                                                break
                                            else:
                                                print('Opção invalida!')
                                    elif op_3 == 0:
                                        break
                                    else:
                                        print('Opção invalida!')
                    else:
                        print('Nenhum Nenhum produto cadastrado!\n')
                    
                elif op_2 == 0:
                    break
                else:
                    print('Opção invalida!')
        except:
            print('Opção invalida!')
                    
    elif op == 0:
        print('VOCÊ SAIU DO SISTEMA!')
        break
    
    
    
    