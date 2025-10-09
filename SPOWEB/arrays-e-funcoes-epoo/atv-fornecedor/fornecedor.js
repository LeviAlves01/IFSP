class Fornecedor{
    #nome
    #fone

    constructor(nome = "Sem nome", fone="(00)00000-0000"){
        this.#nome = nome;
        this.#fone = fone;
    }

    get nome(){
        return this.#nome;
    }

    set nome(novoNome){
        this.#nome = novoNome;
    }

    get fone(){
        return this.#fone;
    }

    set fone(novoFone){
        this.#fone = novoFone;
    }

}

export default Fornecedor;