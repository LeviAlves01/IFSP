import Fornecedor from "./fornecedor.js";

class FornecedorPessoa extends Fornecedor{
    constructor(nome = "Sem nome", fone = "(00)00000-0000", rg, cpf){
        super(nome, fone);
        this._rg = rg;
        this._cpf = cpf;
    }

    get cpf(){
        return this._cpf;
    }

    set cpf(novoCpf){
        this._cpf = novoCpf;
    }

    get rg(){
        return this._rg;
    }

    set rg(novoRg){
        this._rg = novoRg;
    }
}

export default FornecedorPessoa;