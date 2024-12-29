import multiprocessing
import time

def run_program(target_func, timeout=5):
    """
    嘗試判斷某個程式是否會停止（有限時間內）。
    :param target_func: 要執行的目標函數
    :param timeout: 超時限制（秒）
    :return: 若停止則返回 True；若超時則返回 False
    """
    def wrapper(queue):
        try:
            target_func()
            queue.put(True)
        except Exception:
            queue.put(False)

    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=wrapper, args=(queue,))
    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        process.join()
        return False  # 超時，可能不會停止
    else:
        return queue.get()

# 測試用例
def will_stop():
    for i in range(1000):
        pass  # 簡單的迴圈，會停止

def will_not_stop():
    while True:
        pass  # 無窮迴圈，不會停止

# 測試程式
print("測試程式 will_stop:", run_program(will_stop))       # 應返回 True
print("測試程式 will_not_stop:", run_program(will_not_stop)) # 應返回 False（超時）
