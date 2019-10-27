numbers = [1, 2, 3, 4, 5, 6, 7, 8]

doubled_numbers = [number*2 for number in numbers]

print(doubled_numbers)

conditional_numbers = [num*2 if num % 2 == 0 else num/2 for num in numbers]

print(conditional_numbers)