import pandas as pd

# Полный путь к файлу
file_path = 'Wprld population growth rate by cities 2024.csv'
data = pd.read_csv(file_path)

# Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(data.head())

# Вывод информации о данных
print("\nИнформация о данных:")
print(data.info())

# Настройка формата отображения чисел
pd.options.display.float_format = '{:,.2f}'.format

# Вывод статистического описания данных
print("\nСтатистическое описание данных:")
print(data.describe())
