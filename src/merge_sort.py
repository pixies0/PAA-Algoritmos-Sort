def merge_sort(vetor):
  comp, trocas = 0, 0

  if len(vetor) > 1:
    divisao = len(vetor) // 2
    esquerda = vetor[:divisao].copy()
    direita = vetor[divisao:].copy()

    merge_sort(esquerda)
    merge_sort(direita)

    i = j = k = 0

    # Ordena esquerda e direita
    while i < len(esquerda) and j < len(direita):
      if esquerda[i] < direita[j]:
        comp += 1
        vetor[k] = esquerda[i]
        i += 1
      else:
        comp += 1
        vetor[k] = direita[j]
        j += 1
      k += 1
      trocas += 1

    # Ordenação final
    while i < len(esquerda):
      comp += 1
      vetor[k] = esquerda[i]
      i += 1
      k += 1
    while j < len(direita):
      comp += 1
      vetor[k] = direita[j]
      j += 1
      k += 1
      trocas += 1

  return comp, trocas