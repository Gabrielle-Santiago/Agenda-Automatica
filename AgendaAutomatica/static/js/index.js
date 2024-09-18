// Configaração do horário

// Quando clica em adicionar produto cria mais abas

let productCount = 1; // Mantém o controle de quantos produtos foram adicionados

function addProduct() {
    productCount++; // Aumenta o contador para o próximo produto

    const container = document.getElementById('adicionarProdutoContainer');

    // Criar um novo elemento
    const newRow = document.createElement('div');
    newRow.classList.add('row', 'mt-3'); // Nova linha para os novos inputs

    // Criar o novo campo "Nome do Ingrediente"
    const newIngredientDiv = document.createElement('div');
    newIngredientDiv.classList.add('col-md-6');
    const newLabel1 = document.createElement('label');
    newLabel1.setAttribute('for', `nomeIngrediente-${productCount}`);

    const newInput1 = document.createElement('input');
    newInput1.setAttribute('type', 'text');
    newInput1.setAttribute('id', `nomeIngrediente-${productCount}`);
    newInput1.setAttribute('name', `nomeIngrediente-${productCount}`);
    newInput1.setAttribute('class', 'form-control');
    newInput1.setAttribute('placeholder', 'Adicione ingrediente');

    newIngredientDiv.appendChild(newLabel1);
    newIngredientDiv.appendChild(newInput1);

    // Criar o novo campo "Quantidade"
    const newQuantityDiv = document.createElement('div');
    newQuantityDiv.classList.add('col-md-6');
    const newLabel2 = document.createElement('label');
    newLabel2.setAttribute('for', `quantidadeProduto-${productCount}`);

    const newInput2 = document.createElement('input');
    newInput2.setAttribute('type', 'number');
    newInput2.setAttribute('id', `quantidadeProduto-${productCount}`);
    newInput2.setAttribute('name', `quantidadeProduto-${productCount}`);
    newInput2.setAttribute('class', 'form-control');
    newInput2.setAttribute('placeholder', 'Quantidade usada');

    newQuantityDiv.appendChild(newLabel2);
    newQuantityDiv.appendChild(newInput2);

    // Adicionar ambos os campos na nova linha
    newRow.appendChild(newIngredientDiv);
    newRow.appendChild(newQuantityDiv);

    // Adicionar o novo <div> ao contêiner
    container.appendChild(newRow);
}

document.getElementById('adicionarProduto').addEventListener('click', addProduct);

// Diminui o tamanho do botão quando seleciona

// Esconde e mostra os botões e a div