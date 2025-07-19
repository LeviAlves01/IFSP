// uml -> linguagem que permite esquematizar logicamente um projeto (representa
// uma classe)
// métodos -> comportamentos da classe (como se fossem funções ou subrotinas)

// Tipos de classe:
// JS: classes podem ser do tipo private ou public
// private: acesso restrito; public = acesso livre;
// uml: classes podem ser do tipo public, private, protect, package
// protect: private e public

// Tipos de métodos:
// Construtores =
// Com retorno =
// Sem retorno =

// Classe interna = classes dentro de um mesmo arquivo
// Classe externa = classes que podem estar no mesmo diretório ou diretórios diferentes

// Criando uma classe
class Carro{
   constructor(marca, modelo, ano){ // instancia os atributos marca, modelo e ano (reserva três espaços na memória)
       this.marca = marca; // o this referencia o endereço de memória como atributo
       this.modelo = modelo; // reserva 6 espaços na memória (6 variáveis e 6 atributos)
       this.ano = ano;
   }

   // Criando o método detalhes do carro
   detalhesDoCarro(){
       return `Carro: ${this.marca} ${this.modelo}, Ano: ${this.ano}`;
   }
}

// Criando meu objeto
const meuCarro = new Carro('Toyota', 'Corolla', 2022);

// Exibindo o resultado
console.log(meuCarro.detalhesDoCarro()); // referencia o método, pega os atributos e mostra ana tela com os valores da variável preenchida
// método sem parâmetro = procedimento
// em uml o objeto é representado por um gráfico