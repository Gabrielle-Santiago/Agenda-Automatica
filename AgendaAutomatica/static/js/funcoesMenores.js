// As funções abaixo servem para alternar as respostas

function mostra() {
    const grid = document.querySelectorAll(".col");
    let conteudos = document.getElementsByClassName("conteudo");
    for (let i = 0; i < conteudos.length; i++) {
        conteudos[i].style.display = "block";
    };
    
    grid.forEach(grid => {
        grid.style.gridTemplateColumns = "repeat(7, 1fr)";
    });
}

function esconde() {
    const grid = document.querySelectorAll(".col");
    let conteudos = document.getElementsByClassName("conteudo");
    for (let i = 0; i < conteudos.length; i++) {
        conteudos[i].style.display = "none"; 
    };
    
    grid.forEach(grid => {
        grid.style.gridTemplateColumns = "repeat(4, 1fr)";
    });
}

function mostraID(id) {
    const conteudo = document.getElementById(id);
    const menos = document.getElementById(id + "Menos");

    conteudo.style.display = "block";
    menos.style.display = "block";
}

function escondeID(id) {
    const conteudo = document.getElementById(id);
    const menos = document.getElementById(id + "Menos");

    conteudo.style.display = "none";
    menos.style.display = "none";
}

// A função foca em mudar a quantidade de ml para 100 ao selecionar o produto hidratante
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
