#сортировка вставкой
#O(n^2)

# I. INSERTION sort, O(n^2)
def insertionSort(array):
    # First step: choose next element from the unsorted (right) part
    for elem_index in range(1, len(array)):
        elem_value = array[elem_index]

        # Second step: compare the element with each position
        # on the left (sorted part) till the lower one is found
        index_to_compare = elem_index - 1
        while index_to_compare >= 0 and elem_value < array[index_to_compare]:
            array[index_to_compare + 1] = array[index_to_compare]
            index_to_compare -= 1

        # Third step: put the element at the next position after the lower value
        array[index_to_compare + 1] = elem_value
    return array

# не так оптимален по памяти
def InsortSort(array):
    newArr = []
    # находим наимеьший; добавляем в новый массив и удаляем из старого
    for i in range(len(array)):
        minel = array[0] # фиксируем нулевой для начала старта
        minIndex = 0
        for j in range(1,len(array)): # идем с 1 всегда
            if array[j] < minel:
                minel = array[j]
                minIndex = j
        newArr.append(minel)
        array.pop(minIndex)
    return newArr

n = [5,3,6,2,10]
print(InsortSort(n))

# лучший случай O(n) так как каждый элемент сравниться только 1 раз



