def selection_sort(vetor):
  comp, trocas = 0, 0
  n = len(vetor)

  for i in range(n):
    id_minimo = i
    for j in range(i + 1, n):
      if vetor[id_minimo] > vetor[j]:
        comp += 1
        id_minimo = j
    temp = vetor[i]
    vetor[i] = vetor[id_minimo]
    vetor[id_minimo] = temp
    trocas += 1
  
  return comp, trocas



