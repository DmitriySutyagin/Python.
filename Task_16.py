# Вычислить число C заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
number_n = input('Enter a real number n: ')
while number_n.isalpha():
    number_n = input('Enter number n: ')
number_n = float(number_n)
b = int(input('What precision class do you want to round the number with?: '))
print(round(number_n, b))