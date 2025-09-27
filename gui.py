import PySimpleGUI as sg
# Importa as funções que já criamos no nosso outro arquivo
from backend import carregar_transacoes, salvar_transacoes, adicionar_transacao, excluir_transacao, editar_transacao

def formatar_para_tabela(transacoes):
    """Converte a lista de dicionários para o formato que a tabela do PySimpleGUI aceita."""
    dados_tabela = []
    for i, transacao in enumerate(transacoes, start=1):
        # O formato é: [Número, Descrição, Valor, Tipo]
        dados_tabela.append([
            i,
            transacao['descricao'],
            f"R$ {transacao['valor']:.2f}",
            transacao['tipo'].capitalize()
        ])
    return dados_tabela

# --- Layout da Janela ---

# 1. Cabeçalho da tabela
cabecalho = ['#', 'Descrição', 'Valor', 'Tipo']

# 2. Carrega as transações iniciais
lista_transacoes = carregar_transacoes()
dados_iniciais = formatar_para_tabela(lista_transacoes)

# 3. Define o layout
layout = [
    [sg.Text('Gerenciador de Finanças Pessoais', font=('Helvetica', 18))],
    [sg.Table(values=dados_iniciais, headings=cabecalho,
            auto_size_columns=False,
            col_widths=[3, 30, 15, 10],
            justification='left',
            num_rows=15,
            key='--TABELA--', # Chave para identificar a tabela
            display_row_numbers=False,
            enable_events=True, # Importante para saber qual linha foi clicada
            select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
    [sg.Button('Adicionar'), sg.Button('Editar'), sg.Button('Excluir'), sg.Push(), sg.Button('Sair')]
]

# --- Criação da Janela ---
window = sg.Window('Meu Gerenciador Financeiro', layout)

# --- Loop de Eventos ---
while True:
    event, values = window.read() # Escuta por eventos na janela

    # Se o usuário fechar a janela ou clicar em 'Sair'
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    # Lógica para os outros botões virá aqui nas próximas etapas
    print(f"Evento: {event}")
    print(f"Valores: {values}")


# --- Finalização ---
window.close()