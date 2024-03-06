from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from config import configuração_ativa

app = Flask(__name__)
app.config.from_object(configuração_ativa)
app.config['SQLALCHEMY_DATABASE_URI'] #= 'mysql://seu_usuario_mysql:sua_senha_mysql@localhost/seu_banco_de_dados_mysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    preco = db.Column(db.Float, nullable=False)    

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        id_produto = request.form.get('idProduto')
        nome = request.form.get('nomeProduto')
        descricao = request.form.get('descricaoProduto')
        preco = request.form.get('precoProduto')

        if id_produto:  # Verifica se é uma edição de produto
            editar_produto = Produto.query.get(id_produto)
            if editar_produto:
                editar_produto.nome = nome
                editar_produto.descricao = descricao
                editar_produto.preco = preco
                db.session.commit()
        else:

            if nome and descricao and preco:
                novo_produto = Produto(nome=nome, descricao=descricao, preco=preco)
                db.session.add(novo_produto)
                db.session.commit()

    produtos = Produto.query.all()
    return  render_template("home.html", produtos=produtos)

@app.route("/delete_product/<int:product_id>", methods=['GET'])
def delete_product(product_id):
    produto_a_excluir = Produto.query.get(product_id)
    if produto_a_excluir:
        db.session.delete(produto_a_excluir)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)