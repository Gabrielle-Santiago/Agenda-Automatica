let produtoSelecionado = null;
let aromaSelecionado = null;

// Função para capturar o tipo de produto selecionado
function selecionarProduto(produto) {
    produtoSelecionado = produto;
    buscarProdutos();
}

// Função para capturar o aroma selecionado
function selecionarAroma(aroma) {
    aromaSelecionado = aroma;
    buscarProdutos();
}

// Função para buscar os produtos com base nas seleções do usuário
function buscarProdutos() {
    const url = document.getElementById('ajax-url').dataset.url + `?produto=${produtoSelecionado}&aroma=${aromaSelecionado}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            let resultadosDiv = document.getElementById('resultados');
            if (data.produtos.length > 0) {
                let lista = data.produtos.map(prod => 
                    `<button type="button" onclick="buscarDetalhesProduto(${prod[2]})">${prod[0]} - ${prod[1]}</button>`
                ).join('');
                resultadosDiv.innerHTML = lista;
            } else {
                resultadosDiv.innerHTML = "<p>Nenhum produto encontrado.</p>";
            }
        })
        .catch(error => {
            console.error('Erro ao buscar produtos:', error);
        });
}

// Função para buscar os detalhes de um produto específico
function buscarDetalhesProduto(produtoId) {
    const urlDetalhes = `/produto-detalhes/${produtoId}/`;

    fetch(urlDetalhes)
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao buscar detalhes do produto');
            }
            return response.json();
        })
        .then(data => {
            let detalhesDiv = document.getElementById('detalhes-produto');
            let ingredientes = data.ingredientes.map(ing => 
                `<li>${ing.nome}: ${ing.quantidade}</li>`
            ).join('');  // Cria uma lista com os ingredientes

            // Exibe os detalhes do produto, incluindo tipo, aroma e ingredientes
            detalhesDiv.innerHTML = `
                <h3>${data.option} - ${data.category}</h3>
                <h4>Ingredientes:</h4>
                <ul>${ingredientes}</ul>
            `;
        })
        .catch(error => {
            console.error('Erro ao buscar detalhes do produto:', error);
        });
}
