let button = document.getElementById("botao")
let msg = document.getElementById("mensagem").value
let password = document.getElementById("password").value
let user = document.getElementById("username").value
let email = document.getElementById("email").value

button.addEventListener("submit", function(){
    if ((password=="" || msg=="" || user=="") || (password=='' && msg=='' && user=='')){
        msg = "Preencha todos os campos corretamente";
    }
})