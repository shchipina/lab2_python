def sumDigits(n):
    # Перетворення числа у рядок
    n_str = str(n)
    digit_sum = sum(int(digit) for digit in n_str)
    return digit_sum
