//Construtor da classe = serve para instanciar (inicializar) os atributos da classe
//Array = objeto ou biblioteca (função)
//operador new = trabalha com um método construtor
//const, dentro do array, altera o valor, mas não altera o endereço na memória
//O array n é nativo n JavaScript de acordo com a documentação

console.log(typeof Array);
console.log(typeof new Array);
console.log(typeof []);

//Criar array de objeto
let aprovados = new Array('Bia', 'Carlos', 'Ana');
console.log(aprovados);

//acessando cada elemento
console.log(aprovados[0]);
console.log(aprovados[1]);
console.log(aprovados[2]);

//exibindo conteudo que não existe no array
console.log(aprovados[3]);

//exibir conteudo no índice 3 (antes disso vai aparecer undefinied msm pq n existe teoricamente):
aprovados[3] = 'Fernando';
console.log(aprovados[3]);

//Inserir dado na última posição
aprovados.push("Abia");
console.log(aprovados);

//retornar o tamanho do array
console.log(aprovados.length);

//Incluindo dados fora do array
aprovados[9] = 'Rafael';
console.log(aprovados) //<4 empty items>, - espaços vazios na memória

//Comparar undefinied
console.log(aprovados[8]===undefined);

//comparar null
console.log(aprovados[8]===null);

//deletar conteúdo
delete aprovados[1];
console.log(aprovados);

//organizar em ordem alfabética
aprovados.sort();
console.log(aprovados); // desloca os espaços vazios para o final

//criando um array
aprovados = ['Bia', 'Carlos', 'Ana'];
console.log(aprovados);

aprovados.splice(1,1);
console.log(aprovados);

aprovados.splice(1,2);
console.log(aprovados);

//Inserir elementos
aprovados = ['Bia', 'Carlos', 'Ana'];
console.log(aprovados);

aprovados.splice(1, 2, "Elemento1", "Elemento2");
console.log(aprovados);

aprovados.splice(1, 0, "Elemento1", "Elemento2")
console.log(aprovados)