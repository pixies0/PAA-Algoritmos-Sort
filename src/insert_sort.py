def insert_sort(vetor):
  comp, trocas = 0, 0
  n = len(vetor)

  for i in range(1, n):
    marcado = vetor[i]

    j = i - 1
    while j >= 0 and marcado < vetor[j]:
      comp += 1
      vetor[j + 1] = vetor[j]
      j -= 1
      trocas += 1

    vetor[j + 1] = marcado
    trocas += 1

  return  comp, trocas

