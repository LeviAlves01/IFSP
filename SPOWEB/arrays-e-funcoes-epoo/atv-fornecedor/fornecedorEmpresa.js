import Fornecedor from "./fornecedor.js";

class FornecedorEmpresa extends Fornecedor{
    #nome
    #fone
    #ie
    #cnpj

    constructor(nome = "Sem nome", fone = "(00)00000-0000", ie, cnpj){
        super(nome, fone);
        this.#ie = ie;
        this.#cnpj = cnpj;
    }

    get ie(){
        return this.#ie;
    }

    set ie(novoIe){
        this.#ie = novoIe;
    }

    get cnpj(){
        return this.#cnpj;
    }

    set cnpj(novoCnpj){
        this.#cnpj = novoCnpj;
    }
}

export default FornecedorEmpresa;