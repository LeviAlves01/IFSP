const formulario = document.getElementById("registrationForm")
const mensagem = document.getElementById("mensagem")

function validar_formulario(event){
    event.preventDefault()

    let password = document.getElementById("password").value;
    let user = document.getElementById("username").value;
    let email = document.getElementById("email").value;

    if ((password=="" || email=="" || user=="") || (password=='' && email=='' && user=='')){ 
        mensagem.textContent = "Preencha todos os campos corretamente";
        return false;
    } else if ((!email.includes("@gmail.com")) && (!email.includes("@hotmail.com")) && (!email.includes("@yahoo.com"))){
        mensagem.textContent = "Insira um e-mail válido";
        return false;
    } else{
        event.target.submit();
    }
}

formulario.addEventListener('submit', validar_formulario)