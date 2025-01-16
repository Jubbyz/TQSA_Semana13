from aluno import Aluno
from turma import Turma

alunos = []
alunos.append(Aluno('Fernanda', 'Torres', 11))
alunos.append(Aluno('Jade', 'Maria', 7))
alunos.append(Aluno('Gian', 'Carlo', 8))
alunos.append(Aluno('Joao', 'Victor', 9))
alunos.append(Aluno('Paulo', 'Santos', 6))

turmaObject = Turma()
turmaObject.cadastrarAlunos(alunos)

turmaObject.mostrarAlunos()
print('*' * 30)
print('Aluno com menor nota:', turmaObject.menorNota.mostrarAluno())
print('Aluno com maior nota:', turmaObject.maiorNota.mostrarAluno())
turmaObject.maiorNota.mostrarAluno()
