# Sistema de Cadastro de Produtos Atualizado

## Descrição
Essa aplicação fornece uma interface amigável e intuitiva para o cadastramento, atualização e exclusão de produtos. Os produtos podem ser de qualquer tipo e possuem nome, descrição e valor. Para adicionar um novo produto, preencha os campos de informações e clique em "Cadastrar Produto". Com isso, o novo produto aparecerá na lista de produtos logo abaixo do formulário. Para editar um produto, clique em "Atualizar" localizado na última coluna da lista de produtos, ao lado de cada produto listado. Assim, as informações do produto selecionado serão transferidas para o formulário, podendo ser editadas como desejar. Para confirmar as alterações, basta clicar no botão de "Atualizar Produto". Para excluir um produto, basta clicar no botão "Excluir" localizado junto ao botão de "Atualizar". Com isso, um pop-up de confirmação surgirá e o produto poderá ser excluído da lista de produtos cadastrados.

## Configuração

### Pré-requisitos
- Python (versão 3.11.8)
- MySQL
- Git

### Configuração do Ambiente Virtual
1. Clone o repositório:
    ```bash
    git clone https://github.com/feandrade02/cadastro-de-produtos-att.git
    cd seu-repositorio
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # para sistemas Unix
    # ou
    .\venv\Scripts\activate  # para Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Configuração do Banco de Dados
1. Crie um banco de dados MySQL chamado `seu_banco_de_dados_mysql`.

2. Configure as credenciais do banco de dados no arquivo `config.py`:
    ```python
    SQLALCHEMY_DATABASE_URI = 'mysql://seu_usuario_mysql:sua_senha_mysql@localhost/seu_banco_de_dados_mysql'
    ```
Obs.: O arquivo `config.py` tem o seguinte formato:
    
    ```python
    # config.py
    class Config:
        DEBUG = False
        TESTING = False
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    class DevelopmentConfig(Config):
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = 'mysql://seu_usuario_mysql:sua_senha_mysql@localhost/seu_banco_de_dados_mysql'

    class ProductionConfig(Config):
        SQLALCHEMY_DATABASE_URI = 'mysql://usuario_prod:senha_prod@localhost/banco_prod'

    # Outras configurações específicas podem ser adicionadas aqui

    # Selecione a configuração apropriada com base no ambiente de execução (desenvolvimento, produção, etc.)
    configuração_ativa = DevelopmentConfig
    ```


3. Execute as migrações para criar as tabelas:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

## Execução
1. Inicie a aplicação:
    ```bash
    flask run
    ```

2. Abra o navegador e acesse [http://localhost:5000](http://localhost:5000).
