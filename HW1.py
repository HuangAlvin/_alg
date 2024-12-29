def power2n_d(n):
    return 2 ** n
# 建立查表
power2n_table = [2**i for i in range(32)]  # 假設 n 的範圍是 0 到 31

def power2n_d(n):
    if 0 <= n < len(power2n_table):
        return power2n_table[n]
    else:
        raise ValueError("n is out of the supported range (0 to 31)")
# 測試
print(power2n_d(5))  # 輸出 32
print(power2n_d(10))  # 輸出 1024

# 測試超出範圍
try:
    print(power2n_d(40))
except ValueError as e:
    print(e)  # 輸出錯誤消息
