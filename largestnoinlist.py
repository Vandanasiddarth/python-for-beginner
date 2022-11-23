numbers = [99, 10, 8, 2, 10, 0]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)

#remove duplicate in a list
numbers.sort()
numbers_sort = numbers.copy()
print(numbers_sort)
duplicate = ''
for i in numbers_sort:
    if duplicate == i:
        numbers_sort.remove(i)
    duplicate = i
print(numbers_sort)
