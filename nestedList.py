if __name__ == '__main__':
    estudante = []  # lista geral
    notas = []
    nomeFinal = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # juntar nome e ponto na lista estudante
        estudante.append([name, score])
        # formando uma unica lista

    # adiciona as notas do aluno em uma lista de notas
    for aluno in estudante:
        notas.append(aluno[1])

    SegundaMenorNota = sorted(set(notas))[1]

    for aluno in estudante:
        notas.append(aluno[1])
        # verificar segunda menor nota
        if aluno[1] == SegundaMenorNota:
            nomeFinal.append(aluno[0])

    # se a nota for igual printar em ordem alfabetica
    nomeFinal.sort()
    for nome in nomeFinal:
        print(nome)


