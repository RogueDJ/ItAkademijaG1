import time
def f(cbf):
    for i in range(10):
        if i == 5:
            cbf()
        time.sleep(1)

def mojslusac():
    print("Poluvreme bato!!!")

f(mojslusac)