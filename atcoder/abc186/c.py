N = int(input())

def judge_ten(x):
    x = str(x)
    if "7" in  x:
        return True
    else:
        return False

def judge_seven(x):
    s = ""
    while x > 0:
        s = str(x % 8) + s