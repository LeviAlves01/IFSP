//estrutura de seleção múltipla
// Criando um menu

//Criar uma variável
let opcao = '1';

//Criando o menu
console.log("Escolha: \n");
console.log("(s) - Solteiro")
console.log("(c) - Casado")
console.log("(d) - Divorciado \n \n")

switch(opcao){
    case 's':
        console.log("Solteiro"); 
        break;

    case 'c': 
        console.log("Casado"); 
        break;
    
    case 'd': 
        console.log("Divorciado"); 
        break;

    default: 
        console.log("Outros"); 
        break;
}