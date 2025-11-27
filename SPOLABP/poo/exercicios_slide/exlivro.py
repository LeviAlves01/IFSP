class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def detalhes(self):
        return(f"Titulo: {self.titulo} - Autor: {self.autor} - Numero de paginas: {self.num_paginas}")
    
impostora = Livro("Impostora", "R.F. Kuang", 352)
nona_casa = Livro("Nona Casa", "Leigh Bardugo", 432)
daisy_jones = Livro("Daisy Jones & The Six", "Taylor Jenkins Reid", 360)
pessoas_normais = Livro("Pessoas Normais", "Sally Rooney", 264)

ex_livros = [impostora.detalhes(), nona_casa.detalhes(), daisy_jones.detalhes(), pessoas_normais.detalhes()]
print(ex_livros)