"""7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел
выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число."""

def num(n):
    c = 0

    for i in range(n):
        c = c + i+1
    return(f'{c} = {int(n*(n+1)/2)}')

print(num(9999))
