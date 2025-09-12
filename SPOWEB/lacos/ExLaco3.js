//valdação de sexo - laco do while
// para criar array em C: 
// char nome[10]; -> lê um conjunto de caracteres com 10 espaços (reserva um espaço de 10 endereços de memória)
// vetor = array unidimensional (uma linha com várias colunas) estático, ou seja, começa com 0 sempre e só aceita um tipo de dado
// lista = 

do{
    let texto = "Feminino";
    let sexo = texto.charAt[0];

    if(sexo!='F' && sexo!='M'){
        console.log("Erro na validação do sexo");
    }
}
while(sexo!='F' && sexo!='M');

console.log("Sexo validado");