import numpy as np

def heavy_ball(f, grad_f, x0, alpha=0.1, beta=0.5, max_iter=1000, tol=1e-6, M=10):
    """
    Реализация алгоритма тяжелого шарика для минимизации функции f.
    
    Параметры:
    f - функция, которую нужно минимизировать
    grad_f - градиент функции f
    x0 - начальное приближение
    alpha - параметр выбора шага
    beta - параметр контроля скорости
    max_iter - максимальное число итераций
    tol - точность решения
    M - параметр, определяющий количество предыдущих значений x
    
    Возвращает:
    x - точку минимума
    """
    
    # инициализация переменных
    x_prev = np.copy(x0)
    x = np.copy(x0)
    v = np.zeros_like(x0)
    
    # цикл по итерациям
    for i in range(max_iter):
        grad = grad_f(x)
        grad_prev = grad_f(x_prev)
        
        # обновление скорости
        v_new = beta * (v - alpha * grad_prev) + alpha * grad
        v_prev = np.copy(v)
        v = np.copy(v_new)
        
        # обновление точки
        x_new = x - v + ((i - 1) / (i + M)) * (x - x_prev)
        x_prev = np.copy(x)
        x = np.copy(x_new)
        
        # проверка на сходимость
        if np.linalg.norm(grad) < tol:
            break
    
    return x

# пример использования
def f(x):
    return x[0]**2 + 2 * x[1]**2

def grad_f(x):
    return np.array([2 * x[0], 4 * x[1]])

x0 = np.array([1, 1])
x = heavy_ball(f, grad_f, x0)

print("Точка минимума: ", x)
print("Значение функции в точке минимума: ", f(x))