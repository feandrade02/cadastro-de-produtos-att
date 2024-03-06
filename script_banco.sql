CREATE DATABASE banco_produtos;

USE banco_produtos;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    preco FLOAT NOT NULL
);

DESCRIBE produtos;

SELECT * FROM banco_produtos.produto;