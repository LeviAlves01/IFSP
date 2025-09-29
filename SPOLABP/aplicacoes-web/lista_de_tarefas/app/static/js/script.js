// Aguarda o doc HTML ser completamente carregado

document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.check-tarefa').forEach(checkbox => {
        checkbox.addEventListener('change', function(){
            const tarefaid = this.dataset.tarefaid
            const textoTarefa = document.getElementById(`texto-tarefa-${tarefa_id}`);
            
            // A "mágica" do AJAX: envia uma requisição POST em segundo plano
            fetch(`/tarefa/concluir/${tarefaid}`, {
                method: "POST"
            }).then( res => res.json()).then(data =>{
                if(data.status === 'sucesso'){
                    textoTarefa.classList.toggle('concluida', data.concluida)
                }
            })
            .catch(error => console.error("Houve um erro na requisição AJAX.", error))
        })
    })
})