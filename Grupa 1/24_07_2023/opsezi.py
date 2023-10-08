x = 10
def poruka():
    print("Cao")
    print(x)
    a = 15
def proba():
    global y
    y = 15
    print(a)
    print(x)
poruka()
proba()
print(y)