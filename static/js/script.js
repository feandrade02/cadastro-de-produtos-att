function preencherFormulario(id, nome, descricao, preco) {
    document.getElementById('idProduto').value = id;
    document.getElementById('nomeProduto').value = nome;
    document.getElementById('descricaoProduto').value = descricao;
    document.getElementById('precoProduto').value = preco;
    document.getElementById('submitButton').innerText = 'Atualizar Produto';
}

function excluirProduto(id) {
    if (confirm("Deseja excluir este produto?")) {
        // Redireciona para a rota de exclusão
        window.location.href = `/delete_product/${id}`;
    }
}