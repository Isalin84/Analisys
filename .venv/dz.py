import pandas as pd

# Полный путь к файлу
file_path = 'dz.csv'
data = pd.read_csv(file_path)

# Вывод первых 5 строк данных для понимания структуры данных
print("Первые 5 строк данных:")
print(data.head())

# Группировка данных по городу и расчет средней зарплаты
average_salary_by_city = data.groupby('City')['Salary'].mean()

# Вывод средней зарплаты по городу
print("\nСредняя зарплата по городу:")
print(average_salary_by_city)
