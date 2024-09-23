let productCount = parseInt('{{ ingrediente_formset.total_form_count }}'); // Pegando o valor do formset

function addProduct() {
    productCount++;

    const container = document.getElementById('ingredienteContainer');

    // Criar um novo elemento para o ingrediente
    const newRow = document.createElement('div');
    newRow.classList.add('row', 'mt-3');

    // Criar o novo campo "Nome do Ingrediente"
    const newIngredientDiv = document.createElement('div');
    newIngredientDiv.classList.add('col-md-6');

    const newLabel1 = document.createElement('label');
    newLabel1.textContent = `Nome do Ingrediente ${productCount}`;

    const newInput1 = document.createElement('input');
    newInput1.setAttribute('type', 'text');
    newInput1.setAttribute('name', `form-${productCount}-nome`);
    newInput1.setAttribute('id', `id_form-${productCount}-nome`);
    newInput1.setAttribute('class', 'form-control');
    newInput1.setAttribute('placeholder', 'Adicione ingrediente');

    newIngredientDiv.appendChild(newLabel1);
    newIngredientDiv.appendChild(newInput1);

    // Criar o novo campo "Quantidade"
    const newQuantityDiv = document.createElement('div');
    newQuantityDiv.classList.add('col-md-6');

    const newLabel2 = document.createElement('label');
    newLabel2.textContent = `Quantidade ${productCount}`;

    const newInput2 = document.createElement('input');
    newInput2.setAttribute('type', 'number');
    newInput2.setAttribute('name', `form-${productCount}-quantidade`);
    newInput2.setAttribute('id', `id_form-${productCount}-quantidade`);
    newInput2.setAttribute('class', 'form-control');
    newInput2.setAttribute('placeholder', 'Quantidade usada');

    newQuantityDiv.appendChild(newLabel2);
    newQuantityDiv.appendChild(newInput2);

    // Adicionar ambos os campos na nova linha
    newRow.appendChild(newIngredientDiv);
    newRow.appendChild(newQuantityDiv);

    // Adicionar o novo <div> ao contêiner de ingredientes
    container.appendChild(newRow);

    // Atualiza o total de formulários do formset
    const totalForms = document.getElementById('id_form-TOTAL_FORMS');
    totalForms.setAttribute('value', productCount);
}
