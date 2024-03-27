def mediaVetor(vetor):
    soma = 0
    media = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    media = soma / len(vetor)
    return media