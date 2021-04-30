
def cube(a):
    try:
        a = int(a)
    except:
        print("input must be a number")
    if(a < 0):
        print("input must be positive")
    return a **3