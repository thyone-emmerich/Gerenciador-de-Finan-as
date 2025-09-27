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

if __name__ == '__main__':
    app.run(debug=True)