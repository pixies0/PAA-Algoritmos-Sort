def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)
    
    comp = 0
    for num in arr:
        count[num] += 1
        comp += 1
    
    sorted_arr = []
    trocas = 0
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i)

    return comp, trocas




