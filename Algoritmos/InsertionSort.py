# Esse algorismo vai comparar o elemento que está do lado dele
# até ordenar a lista do menor para o maior. 
# Funciona com letras também.


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            print(arr)

# arr = [2, 5, 6, 4, 3, 7, 9, 1, 8, 0]
arr = ['g', 'b', 'c', 'a', 'e', 'f', 'd']
insertion_sort(arr)
print(f'Resultado final: {arr}')
