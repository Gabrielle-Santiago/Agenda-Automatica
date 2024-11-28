function confirmacaoProduto() {
    document.getElementById('formProduto').addEventListener('submit', async function (e) {
        e.preventDefault(); 
    
        const form = e.target;
        const formData = new FormData(form); 

        const confirmacaoPrompt = document.getElementById('confirmacaoPrompt');
        confirmacaoPrompt.style.display = 'block';
        
        const mensagemDiv = document.getElementById('responseMessageProduto');
        mensagemDiv.style.display = 'block';
        mensagemDiv.textContent = 'Processando...';
    
        try {
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            });
    
            const result = await response.json(); 
            mensagemDiv.textContent = result.message;

            if (result.success) {
                form.reset();
            }
    
        } catch (error) {
            console.error('Erro:', error);
            mensagemDiv.textContent = 'Houve um erro. Tente Novamente! Se persistir entre em contato: (73) 98873-4003';
            mensagemDiv.style.color = 'red';
        }
    });
}