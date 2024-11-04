// A função desta página é alternar as respostas ao clicar no botão de mais na tela onde mostra a lista dos agendados

// Função para mostrar o conteúdo
function mostra() {
    let conteudos = document.getElementsByClassName("conteudo");
    for (let i = 0; i < conteudos.length; i++) {
        conteudos[i].style.display = 'block';
    }
}

// Função para esconder o conteúdo
function esconde() {
    let conteudos = document.getElementsByClassName("conteudo");
    for (let i = 0; i < conteudos.length; i++) {
        conteudos[i].style.display = 'none'; 
    }
}
