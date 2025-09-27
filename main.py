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
    print("4. Sair")
    print("---------------------------------------")

def adicionar_transacao(transacoes):
    """Solicita os dados de uma nova transação ao usuário e a adiciona à lista."""
    print("\n--- Adicionar Nova Transação ---")
    descricao = input('Descreva a transação: ')

    while True:
        try:
            valor_str = input('Digite o valor: ')
            valor = float(valor_str)
            if valor <= 0:
                print('O valor deve ser positivo!')
            else:
                break
        except ValueError:
            print('Valor inválido! Por favor, digite um número (ex: 50 ou 12.30).')

    while True:
        tipo = input('Qual foi o tipo de transação? Digite "receita" ou "despesa": ').lower()
        if tipo in ['receita', 'despesa']:
            break
        else:
            print('Tipo de transação inválida. Vamos tentar novamente...')

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
    
    print(f"{'Descrição':<30} {'Valor':>15} {'Tipo':>10}")
    print("-" * 55)

    for t in transacoes:
        valor_formatado = f'R${t['valor']:.2f}'
        print(f"{t['descricao']:<30} {valor_formatado:>15} {t['tipo'].capitalize():>10}")

        print("-" * 55)   

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



# --- Lógica principal do programa ---
if __name__ == '__main__':
    todas_as_transacoes = carregar_transacoes()

    menu_acoes = {
        '1': adicionar_transacao, 
        '2': exibir_extrato,    
        '3': calcular_saldo,    
        '4': 'Sair',
    }

    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ')

        if opcao in menu_acoes:
            if opcao == '4':
                print('Saindo do programa. Até logo!')
                break
            else:
                acao_escolhida = menu_acoes[opcao]
                if callable(acao_escolhida):
                    acao_escolhida(todas_as_transacoes) # Passa a lista de transações para a função
                else:
                    print(f'Você escolheu: {acao_escolhida}. (Funcionalidade a ser implementada!)')
        else:
            print('Por favor, digite uma opção válida!')