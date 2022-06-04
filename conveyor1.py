# Программа выполняет сортировку входящего списка данных
# Входящий список может состоять из вложенных списков
# Результирующий список не имеет вложенных списков
# На входе:  [1, 2, [3, 4, [5, 6], 7], 8]
# На выходе: [1, 2, 3, 4, 5, 6, 7, 8]

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
                # isinstance (x, collection.Iterable) Проверить, является ли элемент итеративным;
                # Если это так, тогда используйте yield from для рекурсивного повторяемого объекта
                #      в качестве подпрограммы, которая сгенерирует все значения
            yield from flatten(x)
        else:
            yield x

in_items = [1, 2, [3, 4, [5, 6], 7], 8]
out_items = []
for x in flatten(in_items):
    out_items.append(x)

print(out_items)