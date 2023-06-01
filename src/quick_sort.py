import sys

def particao(vetor, inicio, final):
  sys.setrecursionlimit(9999999)
  comp, trocas = 0, 0
  pivo = vetor[final]
  i = inicio - 1

  for j in range(inicio, final):
    if vetor[j] <= pivo:
      comp += 1
      i += 1
      vetor[i], vetor[j] = vetor[j], vetor[i]
      trocas += 1
  vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
  trocas += 1

  return i + 1, comp, trocas

def quick_sort(vetor, inicio, final):
  sys.setrecursionlimit(9999999)
  comp, trocas = 0, 0

  if inicio < final:
    posicao, comp, trocas = particao(vetor, inicio, final)
    # Esquerda
    quick_sort(vetor, inicio, posicao - 1)
    # Direito
    quick_sort(vetor, posicao + 1, final)
  return comp, trocas


