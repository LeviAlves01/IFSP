let numero = document.getElementById("numero").value
let mensagem = document.getElementById("mensagem") 

if (isNaN(numero) || numero===""){
    mensagem.textContent = "Por favor, insira um número";
    mensagem.className = "erro";
} else{
    numero = Number(numero);
}

if (numero>10){
    mensagem.textContent = "O número é maior que 10";
    mensagem.className = "maior10"
} else if(numero<=10 && numero>5){
    mensagem.textContent = "O número é maior que 5 mas menor ou igual a 10";
    mensagem.className = "menor10"
}
