def valorNoVetor(vetor, valor):
    for i in range(len(vetor)):
        if valor == vetor[i]:
            return True
    return False