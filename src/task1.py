import math

def calculate_fun(x):
    e_to_x = math.exp(x)
    sqrt_x = math.sqrt(x)
    fun = e_to_x + sqrt_x
    return fun

x = float(input('Введіть значення x: '))
result = calculate_fun(x)

# огруглення до двух знаків після коми
rounded_result = round(result, 2)
print(f'Результат обчислень = {rounded_result}')


# Імпорт функції
from module import sumDigits

n = int(input('Введіть число n: '))
result = sumDigits(n)
print(f'Сума цифр числа {n} дорівнює {result}')
