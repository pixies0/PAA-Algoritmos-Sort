def counting_sorting(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    trocas = 0
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        trocas += 1
    
    for i in range(n):
        arr[i] = output[i]
    
    return trocas

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    comp = 0
    trocas = 0
    
    while max_num // exp > 0:
        trocas += counting_sorting(arr, exp)
        comp += 1
        exp *= 10
    
    return comp, trocas    


# Exemplo de uso
if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    comp, trocas = radix_sort(arr)
    
    print(comp, " comparações")
    print(trocas, " trocas")
    
