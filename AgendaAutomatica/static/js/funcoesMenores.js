// As funções abaixo servem para alternar as respostas ao clicar no botão de mais na tela onde mostra a lista dos agendados

function mostra() {
    let conteudos = document.getElementsByClassName("conteudo");
    for (let i = 0; i < conteudos.length; i++) {
        conteudos[i].style.display = "block";
    }
}

function esconde() {
    let conteudos = document.getElementsByClassName("conteudo");
    for (let i = 0; i < conteudos.length; i++) {
        conteudos[i].style.display = "none"; 
    }
}


// A função foca em mudar a quantidade de ml para 100 ao selecionar o produto hidratante na hora de efetuar um pedido de um produto
function atualizarML() {
    const produto = document.getElementById("produto").value;
    const quantidade = document.getElementById("quantidade"); 

    // O H é de hidratante
    if (produto == "H") {    
        while (quantidade.options.length > 0) {
            quantidade.remove(0);
        }        

        let option = document.createElement("option");
        option.value = "10";
        option.text = "100 ml";

        quantidade.add(option);
    } else {
         while (quantidade.options.length > 0) {
            quantidade.remove(0);
        }
        const opcoesIniciais = [
            { value: "1", text: "10ml" },
            { value: "3", text: "30ml" },
            { value: "5", text: "50ml" }
        ];

        opcoesIniciais.forEach(opcao => {
            let option = document.createElement("option");
            option.value = opcao.value;
            option.text = opcao.text;
            quantidade.add(option);
        });
    }
}