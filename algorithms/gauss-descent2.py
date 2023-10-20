
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# Генерируем примеры данных для обучения
X_train = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y_train = np.array([2, 4, 6, 8, 10])

# Инициализация и настройка гауссовского процесса
kernel = C(1.0, (1e-3, 1e3)) * RBF(0.5, (1e-2, 1e2))
model = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

# Обучение модели
model.fit(X_train, y_train)

# Генерируем примеры данных для тестирования
X_test = np.array([6, 7, 8, 9, 10]).reshape(-1, 1)

# Предсказание значений для тестовых данных
y_pred, sigma = model.predict(X_test, return_std=True)

# Вывод результатов
print("Предсказанные значения:", y_pred)
print("Доверительные интервалы:", sigma)