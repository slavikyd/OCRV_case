#issues with execution
import numpy as np
from scipy.optimize import minimize

class GaussianProcess:
    """
    Класс для построения и использования гауссовских процессов.
    """

    def __init__(self, kernel, noise=1e-10):
        """
        Инициализация гауссовского процесса.

        Параметры:
        kernel - ядро ковариационной функции
        noise - шум, добавляемый к диагональной матрице ковариаций
        """
        self.kernel = kernel
        self.noise = noise

    def fit(self, X, y):
        """
        Обучение гауссовского процесса.

        Параметры:
        X - обучающие данные
        y - значения целевой функции на обучающих данных
        """
        self.X = X
        self.y = y
        self.K = self.kernel(X, X) + np.eye(len(X)) * self.noise

    def predict(self, X_star):
        """
        Предсказание значений целевой функции на новых данных.

        Параметры:
        X_star - новые данные

        Возвращает:
        mean - среднее значение предсказаний
        var - дисперсия предсказаний
        """
        K_star = self.kernel(self.X, X_star)
        K_star_star = self.kernel(X_star, X_star) + np.eye(len(X_star)) * self.noise
        K_inv = np.linalg.inv(self.K)

        mean = K_star.T.dot(K_inv).dot(self.y)
        var = np.diag(K_star_star - K_star.T.dot(K_inv).dot(K_star))

        return mean, var

def gp_descent(f, grad_f, bounds, max_iter=100, tol=1e-6):
    """
    Реализация алгоритма градиентного спуска с использованием гауссовского процесса.

    Параметры:
    f - функция, которую нужно минимизировать
    grad_f - градиент функции f
    bounds - ограничения на значения переменных
    max_iter - максимальное число итераций
    tol - точность решения

    Возвращает:
    x - точку минимума
    """
    kernel = lambda x, y: np.exp(-0.5 * np.sum((x[:, None] - y[None, :])**2, axis=2))
    gp = GaussianProcess(kernel)

    # инициализация переменных
    x = np.random.uniform(bounds[:, 0], bounds[:, 1])
    f_val = f(x)
    grad = grad_f(x)
    gp.fit(np.array([x]), np.array([f_val]))

    # цикл по итерациям
    for i in range(max_iter):
        # предсказание значений функции и ее градиента на новых данных
        X_star = np.random.uniform(bounds[:, 0], bounds[:, 1], size=(100, len(bounds)))
        mean, var = gp.predict(X_star)
        x_star = X_star[np.argmin(mean)]
        grad_star = grad_f(x_star)

        # обновление гауссовского процесса
        gp.fit(np.vstack([gp.X, x_star]), np.hstack([gp.y, f(x_star)]))

        # обновление точки
        x_new = minimize(lambda x: -gp.predict(np.array([x]))[0], x_star, bounds=bounds).x
        f_new = f(x_new)
        grad_new = grad_f(x_new)

        # проверка на сходимость
        if np.linalg.norm(grad_new) < tol:
            break

        # обновление переменных
        x = np.copy(x_new)
        f_val = f_new
        grad = np.copy(grad_new)

    return x

# пример использования
def f(x):
    return x[0]**2 + 2 * x[1]**2

def grad_f(x):
    return np.array([2 * x[0], 4 * x[1]])

bounds = np.array([[-5, 5], [-5, 5]])
x = gp_descent(f, grad_f, bounds)

print("Точка минимума: ", x)
print("Значение функции в точке минимума: ", f(x))