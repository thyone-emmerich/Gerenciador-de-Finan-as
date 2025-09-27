import json

NOME_ARQUIVO = 'transacoes.json'

def carregar_transacoes():
    """Esta função lê as transações do arquivo JSON e as retorna como uma lista."""
    try:
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Arquivo '{NOME_ARQUIVO}' não encontrado. Iniciando com transações vazias.")
        return []
    except json.JSONDecodeError:
        print(f"Atenção: O arquivo '{NOME_ARQUIVO}' está vazio ou corrompido. Iniciando com transações vazias.")
        return []




def salvar_transacoes(transacoes):
    """Esta função salva uma lista de transações no arquivo JSON."""
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(transacoes, f, indent=4, ensure_ascii=False)




def exibir_menu():
    """Exibe as opções do menu principal para o usuário."""
    print("\n--- Gerenciador de Finanças Pessoais ---")
    print("1. Adicionar Transação")
    print("2. Exibir Extrato")
    print("3. Calcular Saldo")
    print("4. Excluir Transação")
    print("5. Editar Transação")
    print("6. Sair")
    print("---------------------------------------")




def coletar_valor_valido():
    while True:
        try:
            valor_str = input('Digite um valor: ')
            valor = float(valor_str)

            if valor <= 0:
                print('Digite um valor positivo.')
            else:
                return valor

        except ValueError:
            print('Valor Inválido. Digite um número.')




def coletar_tipo_valido():
    while True:
        tipo = input('Digite o tipo de transação: "receita" ou "despesa" ').lower()

        if tipo in ['receita', 'desepesa']:
            return tipo
        else:
            print('Digite um tipo válido.')




def adicionar_transacao(transacoes):
    """Solicita os dados de uma nova transação ao usuário e a adiciona à lista."""
    print("\n--- Adicionar Nova Transação ---")
    
    descricao = input('Descreva a transação: ')
    valor = coletar_valor_valido()
    tipo = coletar_tipo_valido()

    nova_transacao = {
        'descricao': descricao,
        'valor': valor,
        'tipo': tipo,
    }
    
    transacoes.append(nova_transacao)
    salvar_transacoes(transacoes)
    print("\nTransação adicionada com sucesso!")




def exibir_extrato(transacoes):
    print("\n--- Extrato de Transações ---")

    if not transacoes:
        print("Nenhuma transação registrada ainda.")
        return
    
    print(f"{'#':<3} {'Descrição':<30} {'Valor':>15} {'Tipo':>10}")
    print("-" * 60)

    for numero, t in enumerate(transacoes, start=1):
        valor_formatado = f"R$ {t['valor']:.2f}" 
        print(f"{numero:<3} {t['descricao']:<30} {valor_formatado:>15} {t['tipo'].capitalize():>10}")
    
    print("-" * 60)  




def calcular_saldo(transacoes):
    print("\n--- Saldo Atual ---")

    if not transacoes:
        print('Não há nenhuma transação registrada.')
        return

    saldo_atualizado = 0.0

    for t in transacoes:
        if t['tipo'] == 'receita':
            saldo_atualizado += t['valor']
        elif t['tipo'] == 'despesa':
            saldo_atualizado -= t['valor']

    saldo_formatado = f'R${saldo_atualizado:.2f}'
    print(f'Seu saldo atual é de: {saldo_formatado}')




def excluir_transacao(transacoes):
    print("\n--- Excluir Transação ---")
    
    if not transacoes:
        print('Não há transações para exibir.')
        return
    
    exibir_extrato(transacoes)
    
    while True:
        try:
            num_para_excluir_str = input('Digite o número da transação a ser excluída: ')
            num_para_excluir = int(num_para_excluir_str)

            if num_para_excluir == 0:
                print('Operação de exlusão cancelada!')

            if 1 <= num_para_excluir <= len(transacoes):
                indice_para_excluir = num_para_excluir - 1

                transacao_removida = transacoes.pop(indice_para_excluir)

                salvar_transacoes(transacoes)

                print(f"\nTransação '{transacao_removida['descricao']}' foi excluída com sucesso!")
                break
            else:
                print("Número inválido. Por favor, digite um número da lista.")

        except ValueError:
            print("Entrada inválida. Por favor, digite apenas um número.")



def editar_transacao(transacoes):
    print("\n--- Editar Transação ---")
    
    if not transacoes:
        print("Nenhuma transação para editar.")
        return

    exibir_extrato(transacoes)

    try:
        num_para_editar = int(input("Digite o número da transação que deseja editar (ou 0 para cancelar): "))

        if num_para_editar == 0:
            print("Operação de edição cancelada.")
            return
        
        if 1 <= num_para_editar <= len(transacoes):
            indice = num_para_editar - 1
            transacao_selecionada = transacoes[indice]

            print("\nVocê selecionou a transação:")
            print(f"  Descrição: {transacao_selecionada['descricao']}")
            print(f"  Valor: R$ {transacao_selecionada['valor']:.2f}")
            print(f"  Tipo: {transacao_selecionada['tipo']}")

            while True:
                print("\nO que você deseja editar?")
                print("1. Descrição")
                print("2. Valor")
                print("3. Tipo")
                print("4. Cancelar")
                
                escolha = input("Escolha uma opção: ")

                if escolha == '1':
                    nova_descricao = input("Digite a nova descrição: ")
                    transacao_selecionada['descricao'] = nova_descricao
                    break
                elif escolha == '2':
                    novo_valor = coletar_valor_valido() # Reutilizando nossa função ajudante!
                    transacao_selecionada['valor'] = novo_valor
                    break
                elif escolha == '3':
                    novo_tipo = coletar_tipo_valido() # Reutilizando nossa função ajudante!
                    transacao_selecionada['tipo'] = novo_tipo
                    break
                elif escolha == '4':
                    print("Edição cancelada.")
                    return
                else:
                    print("Opção inválida. Tente novamente.")
            
            salvar_transacoes(transacoes)
            print("\nTransação atualizada com sucesso!")

        else:
            print("Número de transação inválido.")

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas um número.")

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas um número.")



# --- Lógica principal do programa ---
# --- Lógica principal do programa ---
if __name__ == '__main__':
    todas_as_transacoes = carregar_transacoes()

    menu_acoes = {
        '1': adicionar_transacao,
        '2': exibir_extrato,
        '3': calcular_saldo,
        '4': excluir_transacao,
        '5': editar_transacao, # Nova função adicionada
        '6': 'Sair',
    }

    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ')

        if opcao in menu_acoes:
            if opcao == '6': # Condição de saída agora é '6'
                print('Saindo do programa. Até logo!')
                break
            else:
                acao_escolhida = menu_acoes[opcao]
                if callable(acao_escolhida):
                    acao_escolhida(todas_as_transacoes)
                else:
                    print(f'Você escolheu: {acao_escolhida}. (Funcionalidade a ser implementada!)')
        else:
            print('Por favor, digite uma opção válida!')