# 1st program
result = 9 ** 0.5 * 5
print(result)

# 2nd program
result = (9.99 > 9.98) and (1000 != 1000.1)
print(result)

# 3rd program
without_priority = 2 * 2 + 2
with_priority = 2 * (2 + 2)
comparison_result = (without_priority == with_priority)

print(without_priority)
print(with_priority)
print(comparison_result)

# 4th program
number_str = '123.456'
number = float(number_str)
number *= 10

first_digit_after_point = int(number) % 10
print(first_digit_after_point)
