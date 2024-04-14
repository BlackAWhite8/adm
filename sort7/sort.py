#Мищенко_Денис,Чулков_Роман,Соин_Вадим



#Сортировка Деревом
class Top:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def insert_top(root, value):
    if root is None:
        return Top(value)
    else:
        if value < root.value:
            root.left = insert_top(root.left, value)
        else:
            root.right = insert_top(root.right, value)
    return root



def bypass_tree(root, result):
    if root is not None:
        bypass_tree(root.left, result)
        result.append(root.value)
        bypass_tree(root.right, result)



def tree_sorting(numbers):
    root = None
    for value in numbers:
        root = insert_top(root, value)
    result = []
    bypass_tree(root, result)
    return result


# Блочная сортировка
def bucket_sorting(numbers):
    max_val = max(numbers)
    size = max_val / len(numbers)
    buckets = [[] for _ in range(len(numbers))]

    
    for i in range(len(numbers)):
        j = int(numbers[i] / size)
        if j != len(numbers):
            buckets[j].append(numbers[i])
        else:
            buckets[len(numbers) - 1].append(numbers[i])

    
    for bucket in buckets:
        bucket.sort()

    
    sorted_numbers = []
    for bucket in buckets:
        sorted_numbers += bucket

    return sorted_numbers


def main():
    try:
        user_input = input("Введите числа через пробел: ")
        arr = [int(num) for num in user_input.split() if num.isdigit()]

        if len(arr) == 0:
            print("Некорректный ввод. Пожалуйста, введите целые числа через пробел.")
            return

        print("Исходный массив:", arr)

        sorted_numbers_tree = tree_sorting(arr)
        print("Отсортированный массив через дерево:", sorted_numbers_tree)

        sorted_numbers_bucket = bucket_sorting(arr)
        print("Отсортированный массив блочной сортировкой:", sorted_numbers_bucket)

    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целые числа через пробел.")


if __name__ == "__main__":
    main()
