# def heapify(array, N, i):
#     # На каждом шаге heapify мы ищем наибольшее значение среди родителя (i), левого ребенка и правого ребенка
#     largest = i
#     left_child = 2 * i + 1
#     right_child = 2 * i + 2
#
#     # Проверяем, существует ли левый ребенок и больше ли он родителя
#     if left_child < N and array[largest] < array[left_child]:
#         largest = left_child
#
#     # Проверяем, существует ли правый ребенок и больше ли он самого большого на текущий момент
#     if right_child < N and array[largest] < array[right_child]:
#         largest = right_child
#
#     # Если родительский элемент не самый большой, меняем его местами с самым большим ребенком
#     if largest != i:
#         array[i], array[largest] = array[largest], array[i]
#         print(f"После изменения мест {i} и {largest}: {array}")  # Добавляем вывод изменения массива
#         heapify(array, N, largest)
#
#
# def heapSort(array):
#     N = len(array)
#     # Первый шаг: преобразовать массив в кучу (Max Heap)
#     for i in range(N // 2 - 1, -1, -1):
#         heapify(array, N, i)
#
#     print(f"Массив после построения Max Heap: {array}")
#
#     # Второй шаг: продолжаем строить кучу и перемещаем максимальный корень в конец
#     for i in range(N - 1, 0, -1):
#         array[i], array[0] = array[0], array[i]  # Меняем корень с последним элементом
#         print(f"Меняем местами {0} и {i}: {array}")  # Выводим, что было изменено
#         heapify(array, i, 0)
#         print(f"После heapify для подмассива из {i} элементов: {array}")  # Выводим состояние массива после heapify
#
#     print(f"Отсортированный массив: {array}")
#     return array
#
# heapSort([1, 4, 5, 8, 0, 3, 4, 6, 5, 4])

def heapify(array,N,i):
    leader = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < N and array[left] > array[leader]:
        leader = left

    if right < N and array[right] > array[leader]:
        leader = right

    if leader != i:
        array[i],array[leader] = array[leader], array[i]
        heapify(array,N,leader)

def sort(array):
    N = len(array)

    for i in range(N//2 - 1, -1, -1): heapify(array,N,i)

    for i in range(N-1,0,-1):
        array[i],array[0] = array[0],array[i]
        heapify(array,i,0)

    return array
print(sort([1, 4, 5, 8, 0, 3, 4, 6, 5, 4]))
