"""9. Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр."""

a = int(input('Введите кол-во цифр которые будете вводить '))
c = 0
d = 0
e = 0
for i in range(a):
    b = int(input(f' Введите числа через "ENTER" '))
    c = 0
    for t in str(b):
        c += int(t)
    if c > d:
        d = c
        e = b
print(f'Число с максимальной суммой цифр - {e}, сумма цифр равна - {d}')

