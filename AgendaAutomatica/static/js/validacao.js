const camposInput = document.getElementsByClassName("required")
const spans = document.getElementsByClassName("span-required")
const emailRegex = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}(?:\.[a-z]{2,})?$/i;


// Função para aplicar borda de erro e mostrar a mensagem
function setError(index, message) {
    camposInput[index].style.border = "2px solid #e63636";
    spans[index].style.display = "block";
    spans[index].textContent = message; 
}


// Função para limpar o erro e remover a borda vermelha
function clearError(index) {
    camposInput[index].style.border = "";   
    spans[index].style.display = "none";   
    spans[index].textContent = ""; 
}


// Validação do nome
function nameValidate() {
    if (camposInput[0].value.length < 5) {  
        setError(0, "Por favor, escreva seu nome completo");
    } else {
        clearError(0);
    }
}

// Validação da data


// Validação do horário


// Validação do formato do email
function emailValidate() {
    if (emailRegex.test(camposInput[4].value)) {
        clearError(4);
    } else {
        setError(4, "Por favor, acrescente um email válido");
        
    }
}


// Validação do número de contato
function contactValidate() {
    if (camposInput[5].value.length < 10) {
        setError(5, "Por favor, adicione um número corretamente ex: (XX) XXXXX-XXXX");
    } else {
        clearError(5);
    }
}
