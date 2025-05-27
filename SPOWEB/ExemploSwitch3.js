//Estações do ano

let mes = "Setembros";

switch(mes){
    case "Dezembro":
    case "Janeiro":
    case "Fevereiro":
        console.log("Verão... \n");
        break;

    case "Março":
    case "Abril":
    case "Maio":
        console.log("Outono... \n");
        break;

    case "Junho":
    case "Julho":
    case "Agosto":
        console.log("Inverno... \n");
        break;

    case "Setembro":
    case "Outubro":
    case "Novembro":
        console.log("Primavera... \n");
        break;

    default:
        console.log("Mês inválido... \n");
        break;
}