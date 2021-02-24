def money():
    try:
        hours = float(input('Выработка в часах '))
        zp = int(input('Ставка '))
        prem = int(input('Премия  '))
        res = hours * zp + prem
        print(f'Итого зарплата за период  {res}')
    except ValueError:
        return print('Введите число!')
money()
