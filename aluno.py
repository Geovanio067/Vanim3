class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = float(nota)

    def exibir(self):
        print(f'Nome: {self.nome} | Nota: {self.nota}')

    def aprovado(self):
        return 'Aprovado' if self.nota >= 6 else 'Reprovado'
