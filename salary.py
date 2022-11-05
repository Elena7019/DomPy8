
import pandas as pd

print('----' * 30)
print('Информация о заработной плате')

salary = {
    'ID': ['01', '02', '03', '04', '05'],
    'Оклад, руб.': ['100000', '80000', '85000', '50000', '45000']

}

cc = pd.DataFrame(data=salary)

with open('salary_size.csv', 'a', encoding='UTF-8') as cl:
    cl.write(f'{cc}')
    cl.write('\n')

print(cc)