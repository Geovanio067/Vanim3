from aluno import Aluno

alunos = []

while True:
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Sair')
    op = input('Opção: ')

    if op == '1':
        n = input('Nome: ')
        nota = input('Nota: ')
        a = Aluno(n, nota)
        alunos.append(a)
        print('OK\n')

    elif op == '2':
        for a in alunos:
            a.exibir()
            print(f'Situação: {a.aprovado()}\n')

    elif op == '3':
        with open('alunos.txt', 'w') as arq:
            for a in alunos:
                arq.write(f'{a.nome},{a.nota},{a.aprovado()}\n')
        print('Salvo. Fim.')
        break

    else:
        print('Inválido\n')