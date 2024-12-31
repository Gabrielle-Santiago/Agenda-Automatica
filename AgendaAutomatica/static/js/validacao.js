// Essa área foca na validação dos formulários

const camposInput = document.getElementsByClassName("required")
const spans = document.getElementsByClassName("span-required")
const emailRegex = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}(?:\.[a-z]{2,})?$/i;

function setError(index, message) {
    camposInput[index].style.border = "2px solid #e63636";
    spans[index].style.display = "block";
    spans[index].textContent = message; 
}


function clearError(index) {
    camposInput[index].style.border = "";   
    spans[index].style.display = "none";   
    spans[index].textContent = ""; 
}


function nameValidate() {
    if (camposInput[0].value.length < 5) {  
        setError(0, "Por favor, escreva seu nome completo");
    } else {
        clearError(0);
    }
}


function emailValidate() {

    if (emailRegex.test(camposInput[1].value)) {
        clearError(1);
    } else {
        setError(1, "Por favor, acrescente um email válido");
    }
}


function contactValidate() {
    if (camposInput[2].value.length < 10) {
        setError(2, "Por favor, adicione um número corretamente ex: (73) 95555-4444");  
    } else {
        clearError(2);
    }
}

function procedAvaliacao() {
    const opcoesAvaliacao = ["SL", "LP", "LA", "PE", "ES", "NF", "RE", "MH"];
    const procedSelect = document.querySelector('select[name="proced"]');
    const modal = document.getElementById("divAvaliacao");

    procedSelect.addEventListener("change", function () {
        const proced = procedSelect.value;

        if (opcoesAvaliacao.includes(proced)) {
            modal.style.display = "flex";
        } else {
            modal.style.display = "none"; 
        }
    });
}


function modalSim() {
    alert("Confirmação que já realizou a avaliação. Termine de preencher o formulário e agende seu procedimento");
    document.getElementById("divAvaliacao").style.display = "none";
}


function modalNao() {
    document.getElementById("divAvaliacao").style.display = "none";
    const avaliacao = document.getElementById("descAvaliacao");
    avaliacao.style.display = "flex";  

    const descricao = confirm("A avaliação tem duração de 30min, e a profissional informará se é cabível a realização do procedimento posteriormente. Deseja continuar e agendar sua avaliação?");

    if (descricao) {
        alert("Finalize seu cadastro para sua avaliação ser agendada.");
    } else {
        document.querySelector('select[name="proced"]').value = "Select"; 
    }
}


