import numpy as np

def riemann_integration(n=100):
    """
    使用黎曼積分方法計算三重積分。
    ∫z=0→1 ∫y=0→1 ∫x=0→1 (3x^2 + y^2 + 2z^2) dx dy dz

    :param n: 分割區間數，n越大精度越高
    :return: 三重積分的數值結果
    """
    dx = 1 / n
    dy = 1 / n
    dz = 1 / n

    integral = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # 使用小矩形中心點來近似函數值
                x = (i + 0.5) * dx
                y = (j + 0.5) * dy
                z = (k + 0.5) * dz
                f_xyz = 3 * x**2 + y**2 + 2 * z**2
                integral += f_xyz * dx * dy * dz

    return integral

# 測試黎曼積分
riemann_result = riemann_integration(n=100)
print("黎曼積分結果:", riemann_result)
def monte_carlo_integration(num_samples=100000):
    """
    使用蒙地卡羅方法計算三重積分。
    ∫z=0→1 ∫y=0→1 ∫x=0→1 (3x^2 + y^2 + 2z^2) dx dy dz

    :param num_samples: 隨機點的數量，越大精度越高
    :return: 三重積分的數值結果
    """
    # 隨機生成樣本點
    x_samples = np.random.uniform(0, 1, num_samples)
    y_samples = np.random.uniform(0, 1, num_samples)
    z_samples = np.random.uniform(0, 1, num_samples)

    # 計算函數值
    f_values = 3 * x_samples**2 + y_samples**2 + 2 * z_samples**2

    # 平均函數值乘以體積 (這裡體積為 1)
    integral = np.mean(f_values)
    return integral

# 測試蒙地卡羅積分
monte_carlo_result = monte_carlo_integration(num_samples=100000)
print("蒙地卡羅積分結果:", monte_carlo_result)
