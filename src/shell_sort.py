def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    comp = 0
    trocas = 0
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                trocas += 1
                comp += 1
            arr[j] = temp
            comp += 1
        gap //= 2
    return comp, trocas

