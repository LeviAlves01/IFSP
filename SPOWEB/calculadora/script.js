alert("Bem-vindo a calculadora interativa!");
let valores = [];
let resultado;
let opcao = "";

const Menu = function(){
    alert(
        "Escolha uma opção:\n" +
        "1 - Somar\n" +
        "2 - Subtrair\n" +
        "3 - Multiplicar\n" +
        "4 - Dividir\n" +
        "5 - Sair"
    )
}

const Saida = function(){
    alert("Saindo...");
}

let verificarvalores = function(){
    if (valores.some(isNaN) || valores.length !== 2){
        alert("Por favor digite dois valores válidos");
        return false;
    }
    return true;
}

const soma = (a, b) =>{
    return a+b;
}

const subtracao = (a,b) =>{
    return a-b;
}

const multiplicacao = (a, b) => {
    return a*b;
}

const divisao = (a, b) => {
    return a/b;
}

while (opcao != "5"){
    Menu();
    opcao = prompt("Digite a opção aqui");

    switch(opcao){
        case "1":
            valores = prompt("Digite dois valores separados por vírgula").split(",").map(Number);
            if(verificarvalores()){
                resultado = soma(valores[0], valores[1]);
                alert("O resultado da soma é: " + resultado);
            }
            break;
        
        case "2":
            valores = prompt("Digite dois valores separados por vírgula").split(",").map(Number);
            if(verificarvalores()){
                resultado = subtracao(valores[0], valores[1]);
                alert("O resultado da subtração é: " + resultado);
            }
            break;

        case "3":
            valores = prompt("Digite dois valores separados por vírgula").split(",").map(Number);
            if(verificarvalores()){
                resultado = multiplicacao(valores[0], valores[1]);
                alert("O resultado da multiplicação é: " + resultado);
            }
            break;

        case "4":
            valores = prompt("Digite dois valores separados por vírgula").split(",").map(Number);
            if(verificarvalores()){
                resultado = divisao(valores[0], valores[1]);
                alert("O resultado da divisão é: " + resultado.toFixed(2));
            }
            break;

        case "5":
            Saida();
            break;

        default:
            alert("Opção inválida! Tente novamente");
            break;
    }
}