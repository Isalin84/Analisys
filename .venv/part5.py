import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(100)
y = np.random.rand(100)

# Создание диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', alpha=0.7, edgecolor='black')
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
