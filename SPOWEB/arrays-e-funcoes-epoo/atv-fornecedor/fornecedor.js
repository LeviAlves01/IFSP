class Fornecedor{
    constructor(nome = "Sem nome", fone="(00)00000-0000"){
        this._nome = nome;
        this._fone = fone;
    }

    get nome(){
        return this._nome;
    }

    set nome(novoNome){
        this._nome = novoNome;
    }

    get fone(){
        return this._fone;
    }

    set fone(novoFone){
        this._fone = novoFone;
    }

}

export default Fornecedor;