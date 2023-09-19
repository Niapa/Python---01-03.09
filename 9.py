'''Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
Задача 42: Узнать какая максимальная households в зоне минимального значения population.
'''

# В res2 получили единственное значение households, оно максимально.  → При попытке
# найти максимальное значение программа выдает ошибку.


import pandas as pd

data = pd.read_csv('california_housing_train.csv')

res1 = data.loc[data['population'] < 500]['median_house_value'].mean()
print(res1)

res2 = data.loc[data['population'].min(),'households']
print(res2)

