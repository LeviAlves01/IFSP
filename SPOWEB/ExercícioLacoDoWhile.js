// Utilizando o laco de repeticao do...while. imprima o primeiro numero divisivel por 19
// Leve em consideração o valor do primeiro número 100 e do segundo número 200

let numero = 100;

do{  
    if(numero%19==0){
        console.log("O primeiro número divisível por 19 entre 100 e 200 é", numero);
        break;
    }

    numero++;
}while(numero<=200)