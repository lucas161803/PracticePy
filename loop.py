for ee in range(1,10):
    print(ee)

def fbnumListRec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fbnumListRec(n-1)+fbnumListRec(n-2)

print("fbnum: " + str(fbnumListRec(5)))

def fbnumListLoop(n):
    x1 = 0
    x2 = 1
    val = 0
    index = 0
    while index < n:
        index += 1
        if index == 1:
            val = 0
            continue
        if index == 2:
            val = 1
            continue

        val = x1 + x2
        x1 = x2
        x2 = val
        
    
    return val

print("fbnum: " + str(fbnumListLoop(5)))