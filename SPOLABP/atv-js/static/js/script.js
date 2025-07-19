const formulario = document.getElementById("registrationForm")
const mensagem = document.getElementById("mensagem")

function validar_formulario(event){
    event.preventDefault()

    let password = document.getElementById("password").value;
    let user = document.getElementById("username").value;
    let email = document.getElementById("email").value;

    if ((password=="" || email=="" || user=="") || (password=='' && email=='' && user=='')){ 
        mensagem.textContent = "Preencha todos os campos corretamente";
    } else if ((!email.includes("@gmail.com")) && (!email.includes("@hotmail.com")) && (!email.includes("@yahoo.com"))){
        mensagem.textContent = "Insira um e-mail válido";
    }

    localStorage.setItem('mensagem', mensagem)
    //else{
    //    mensagem.textContent = "Uusário {usuario} cadastrado com sucesso"
    //}
}

formulario.addEventListener('submit', validar_formulario)

document.addEventListener('DOMContentLoaded', () => {
    const mensagemSalva = localStorage.getItem('mensagem');
    if (mensagemSalva) {
        document.getElementById('mensagem').textContent = mensagemSalva;
    }
})