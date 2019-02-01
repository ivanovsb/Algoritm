# Иванов Сергей
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

count = input('Введи количество предприятий: ')
Company = namedtuple('Company', 'name, profit1, profit2, profit3, profit4, average_profit')
lst_company = []
title = ['Название компании: ', 'Прибыль за 1-ый кв.: ', 'Прибыль за 2-ой кв.: ', 'Прибыль за 3-ий кв.: ',
         'Прибыль за 4-ый кв.: ']
for i in range(int(count)):
    lst_company_row = []
    average_profit = 0
    print(f'\nВведи данные для {i + 1}-й компании: Название компании и прибыль за каждый квартал')
    for j in range(len(title)):
        el = input(title[j])
        if 0 < j < 5:
            average_profit += int(el)
        lst_company_row.append(el)
    average_profit = average_profit / 4
    lst_company_row.append(average_profit)
    lst_company.append(lst_company_row)
company_tuple = [Company(*x) for x in lst_company]
all_company_profit = 0
for c in company_tuple:
    all_company_profit += c.average_profit
all_company_profit = all_company_profit / int(count)

result_great = [c.name for c in company_tuple if c.average_profit > all_company_profit]
print(f'\nНаименование компаний, чья прибыль выше среднего {all_company_profit}: \n {result_great}\n')
result_less = [c.name for c in company_tuple if c.average_profit < all_company_profit]
print(f'Наименование компаний, чья прибыль ниже среднего {all_company_profit}: \n {result_less}\n')
