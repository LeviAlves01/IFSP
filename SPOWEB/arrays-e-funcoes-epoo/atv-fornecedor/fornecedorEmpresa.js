import Fornecedor from "./fornecedor.js";

class FornecedorEmpresa extends Fornecedor{
    constructor(nome = "Sem nome", fone = "(00)00000-0000", ie, cnpj){
        super(nome, fone);
        this._ie = ie;
        this._cnpj = cnpj;
    }

    get ie(){
        return this._ie;
    }

    set ie(novoIe){
        this._ie = novoIe;
    }

    get cnpj(){
        return this._cnpj;
    }

    set cnpj(novoCnpj){
        this._cnpj = novoCnpj;
    }
}

export default FornecedorEmpresa;