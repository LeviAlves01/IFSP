import Fornecedor from "./fornecedor.js";
import FornecedorEmpresa from "./fornecedorEmpresa.js";
import FornecedorPessoa from "./fornecedorPessoa.js";

const empresa1 = new FornecedorEmpresa("AdLances", "(11)98761-9087", "123456789-0", "78.123.456/0001-87");
const fornecedor1 = new FornecedorPessoa("Mário", "(11) 91541-1452");

console.log("Fornecedor pessoa: ", fornecedor1.nome);
console.log(`\nEmpresa: ` + `${empresa1.nome}`, 
    `\nTelefone: ${empresa1.fone}`,
    `\nIE da empresa: ${empresa1.ie}`,
    `\nCNPJ: ${empresa1.cnpj}`)