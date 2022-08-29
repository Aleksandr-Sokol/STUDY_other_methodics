# Функции высших порядков

# 1 map() используется для применения функции к каждому элементу итерируемого объекта
# map(function, iterable, [iterable 2, iterable 3, ...])
# map(lambda item: item[] expression, iterable)

numbers = [10, 15, 21, 33, 42, 55]
mapped_numbers = list(map(lambda x: x * 2 + 3, numbers))
print(mapped_numbers)

# 2 filter применяет функцию ко всем элементам последовательности и возвращает итератор с теми объектами, для которых функция вернула True.
print(list(filter(lambda x: x % 2 == 0, [10, 111, 102, 213, 314, 515])))

# 3 reduce превращает итерируемую последовательность, в требуемое единственное значение.
# reduce(function, iterable[, initializer])
from functools import reduce
sum_all = reduce(lambda x,y: x + y, [10, 20, 30, 40, 50])
print(sum_all)

# 3 zip Функция zip() в Python определяется как zip(* iterables).
# Функция принимает итераторы (то есть последовательности) в качестве аргументов и возвращает то же итератор.
# Этот итератор генерирует серию кортежей, содержащих элементы из каждой итерации.
