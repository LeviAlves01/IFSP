//Criando uma função

//Criar função anônima
const imprimirSoma = function(a, b){
    console.log(a + b);
}

imprimirSoma(2, 3);

//função de seta - arrow function
const soma = (a,b) =>{
    return a + b;
}

console.log(soma(2, 3));

//retorno implícito
const subtracao = (a, b) => a-b;
console.log(subtracao(2, 3));

const imprime1 = a => console.log(a);
imprime1('Legal');