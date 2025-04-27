def merge_sort(array):
    # Если длина массива 1 или меньше, он уже отсортирован
    if len(array) <= 1:
        return array

    # Разделяем массив на две части
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Рекурсивно сортируем каждую часть
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Сливаем две отсортированные части
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = j = 0

    # Пока не дошли до конца одного из подмассивов
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # Добавляем меньший элемент
            i += 1
        else:
            result.append(right[j])  # Добавляем меньший элемент
            j += 1

    # Добавляем оставшиеся элементы из левого подмассива, если они есть
    while i < len(left):
        result.append(left[i])
        i += 1

    # Добавляем оставшиеся элементы из правого подмассива, если они есть
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort([3,4,5,6,1,2,3]))