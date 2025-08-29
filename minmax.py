numbers = [42, 17, 56, 23, 89, 5, 77]
max_value = numbers[0]
min_value = numbers[0]

for m in numbers:
    if m >= max_value:
        max_value = m
    elif m <= min_value:
        min_value = m
print('最大値:',max_value)
print('最小値:',min_value)

