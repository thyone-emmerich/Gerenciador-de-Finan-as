from flask import Flask, render_template, request, redirect, url_for
from backend import carregar_transacoes, salvar_transacoes

app = Flask(__name__)

@app.route('/')
def index():
    lista_de_transacoes = carregar_transacoes()
    return render_template('index.html', transacoes=lista_de_transacoes)



@app.route('/adicionar', methods=['POST'])
def adicionar():
    descricao = request.form['descricao']
    valor = float(request.form['valor'])
    tipo = request.form['tipo']

    nova_transacao = {'descricao': descricao, 'valor': valor, 'tipo': tipo}

    transacoes_atuais = carregar_transacoes()
    transacoes_atuais.append(nova_transacao)
    salvar_transacoes(transacoes_atuais)

    return redirect(url_for('index'))



@app.route('/excluir/<int:indice>', methods=['POST'])
def excluir(indice):
    transacoes_atuais = carregar_transacoes()
    
    if 0 <= indice < len(transacoes_atuais):
        transacoes_atuais.pop(indice)
        salvar_transacoes(transacoes_atuais)
    else:
        print(f"Tentativa de excluir índice inválido: {indice}")

    return redirect(url_for('index'))


@app.route('/editar/<int:indice>', methods=['GET'])
def editar(indice):
    transacoes_atuais = carregar_transacoes()
    
    if 0 <= indice < len(transacoes_atuais):
        transacao_para_editar = transacoes_atuais[indice]
        return render_template('editar.html', transacao=transacao_para_editar, indice=indice)
    else:
        print(f"Tentativa de editar índice inválido: {indice}")
        return redirect(url_for('index')) 
    

    
@app.route('/atualizar/<int:indice>', methods=['POST'])
def atualizar(indice):
    transacoes_atuais = carregar_transacoes()

    if 0 <= indice < len(transacoes_atuais):
        descricao_nova = request.form['descricao']
        valor_novo = float(request.form['valor'])
        tipo_novo = request.form['tipo']

        transacoes_atuais[indice]['descricao'] = descricao_nova
        transacoes_atuais[indice]['valor'] = valor_novo
        transacoes_atuais[indice]['tipo'] = tipo_novo
        
        salvar_transacoes(transacoes_atuais)
    else:
        print(f"Tentativa de atualizar índice inválido: {indice}")
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
