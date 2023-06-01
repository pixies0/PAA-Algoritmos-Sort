def bubble_sort(lista):
    comp, trocas = 0, 0
    num = len(lista)

    for i in range(num):
        for j in range(0, num - i - 1):
            comp += 1
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
                trocas += 1

    return comp, trocas





