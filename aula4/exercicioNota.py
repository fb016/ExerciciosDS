isRunning = True

while isRunning:
    print("[1]Digitar as notas a mão:")
    print("[2]Automático")
    print("[0]Sair")

    opcao = int(input("Escolha a opcao: "))

    match opcao:
        case 1:
            soma = 0
            notaAluno = []
            mediaAluno = []
            acimaDaMedia = 0

            for aluno in range(10):
                for a in range(3):
                    nota = float(input(f"Digite a sua nota do aluno {aluno +1} : "))
                    while nota < 0 or nota > 10:
                        print("Nota inválida.")
                        nota = float(input("Digite uma nota válida: "))
                    notaAluno.append(nota)
                notaAluno.sort()
                mediaTemp = (notaAluno[1] + notaAluno[2])/2
                mediaAluno.append(mediaTemp)

            for media in range(10):
                soma = soma + mediaAluno[media]
                if mediaAluno[media] >= 9:
                    acimaDaMedia = acimaDaMedia + 1
            mediaTotal = soma/10

            print("A média da sala foi")
            print(mediaTotal)
            print("Alunos acima da média: ")
            print(acimaDaMedia)
            input("Pressione enter para continuar.")
        case 2:
            acimaDaMedia = 0
            soma = 0
            mediaAlunoAutomatico = [10, 8, 3, 5, 3, 10, 5, 7, 6, 4]
            for media in range(10):
                soma = soma + mediaAlunoAutomatico[media]
                if mediaAlunoAutomatico[media] >= 9:
                    acimaDaMedia = acimaDaMedia + 1
            mediaTotal = soma/10

            print("A média da sala foi")
            print(mediaTotal)
            print("Alunos acima da média: ")
            print(acimaDaMedia)
            input("Pressione enter para continuar.")
        case 0:
            isRunning = False
