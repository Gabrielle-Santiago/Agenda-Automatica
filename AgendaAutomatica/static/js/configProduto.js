// As configurações daqui são referentes ao cadastro dos produtos

let produtoSelecionado = null;
let aromaSelecionado = null;

function selecionarProduto(produto) {
    produtoSelecionado = produto;
    buscarProdutos();
}

function selecionarAroma(aroma) {
    aromaSelecionado = aroma;
    buscarProdutos();
}

// Faz a busca no BD para ver se existe o tipo de produto com o aromas
function buscarProdutos() {
    const ajaxUrlElement = document.getElementById('ajax-url');
    const urlBase = ajaxUrlElement.getAttribute('data-url');
    const url = `${urlBase}?produto=${produtoSelecionado}&aroma=${aromaSelecionado}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            let resultadosDiv = document.getElementById('resultados');
            if (data.produtos.length > 0) {
                let lista = data.produtos.map(prod => `<p>${prod[0]} - ${prod[1]}</p>`).join('');
                resultadosDiv.innerHTML = lista;
            } else {
                resultadosDiv.innerHTML = "<p>Nenhum produto encontrado.</p>";
            }
        })
        .catch(error => {
            console.error('Erro ao buscar os produtos:', error);
        });
}

function buscarDetalhesProduto(produtoId) {
    const urlDetalhes = `/produto-detalhes/${produtoId}/`;
    fetch(urlDetalhes)
        .then(response => response.json())
        .then(data => {
            let detalhesDiv = document.getElementById('detalhes-produto');
            let ingredientes = data.ingredientes.map(ing => `<li>${ing.nome}: ${ing.quantidade}</li>`).join('');

            detalhesDiv.innerHTML = `
                <h3>${data.option} - ${data.category}</h3>
                <p>${data.descricao}</p>
                <h4>Ingredientes:</h4>
                <ul>${ingredientes}</ul>
            `;
        })
}
