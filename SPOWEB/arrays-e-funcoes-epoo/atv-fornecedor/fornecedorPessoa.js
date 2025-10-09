import Fornecedor from "./fornecedor.js";

class FornecedorPessoa extends Fornecedor{
    #rg
    #cpf

    constructor(nome = "Sem nome", fone = "(00)00000-0000", rg, cpf){
        super(nome, fone);
        this.#rg = rg;
        this.#cpf = cpf;
    }

    get cpf(){
        return this.#cpf;
    }

    set cpf(novoCpf){
        this.#cpf = novoCpf;
    }

    get rg(){
        return this.#rg;
    }

    set rg(novoRg){
        this.#rg = novoRg;
    }
}

export default FornecedorPessoa;