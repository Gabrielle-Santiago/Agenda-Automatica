// A função desta página é alternar as respostas ao clicar no botão de mais na tela onde mostra a lista dos agendados

document.getElementById("sinal").onclick = function(){esconde(); mostra();}
let conteudo = document.getElementsByClassName("conteudo")

function mostra(el) {
    if (conteudo.style.display == 'none') {
        document.querySelector(el).style.display = 'block';
    }
}

function esconde(el) {
    if (conteudo.style.display == 'block') {
        document.querySelector(el).style.display = 'none';
    }
}