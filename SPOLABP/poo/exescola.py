class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Curso(Aluno):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def exibir(self):
        return(f"O aluno {self.nome} está matriculado no curso {self.curso} na turma {self.turma}")
    
    def trocar_curso(self, novo_curso, nova_turma):
        if novo_curso != self.curso:
            self.curso = novo_curso
            self.turma = nova_turma
            print(f"O aluno {self.nome} foi remanejado para o curso {self.curso}, na turma {self.turma}")
        else:
            print(f"O aluno {self.nome} já está matriculado neste curso.")
    
    def trocar_turma(self, nova_turma):
        if nova_turma != self.turma:
            self.turma = nova_turma
            print(f"O aluno {self.nome} foi remanejado para a turma {self.turma} do curso {self.curso}")
        else:
            print(f"O aluno {self.nome} já está matriculado nessa turma")

    def get_nome(self):
        return self.nome
    
    def get_turma(self):
        return self.turma
    
    def get_curso(self):
        return self.curso
    
levi = Curso("Levi", 16, "Desenvolvimento de Sistemas", 231)
igor = Curso("Igor", 15, "Telecomunicações", 131)

print(levi.exibir())
print(levi.trocar_curso("Mecânica", 232))

print(igor.exibir())
print(igor.trocar_turma(231))