import concurrent.futures.thread as t
import time
executor = t.ThreadPoolExecutor(100)

def f():
    print("Hello World")
    time.sleep(1)
    print("How are you")

executor.submit(f)
executor.submit(f)
executor.submit(f)
executor.submit(f)
