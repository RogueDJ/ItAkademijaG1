import _thread, time
def f1():
    for i in range(10):
        print(i)
        time.sleep(1)
for i in range(100):
    _thread.start_new_thread(f1, ())


print("Hello from dovla")
time.sleep(50)