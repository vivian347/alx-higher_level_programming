def print_last_digit(number):
    num = number % 10
    temp = number
    if temp < 0:
        temp *= -1
        num = (temp % 10)
    print(num, end="")
    return num
