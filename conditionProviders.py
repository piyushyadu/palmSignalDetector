
def listCal(lmList):
    res = [0, 0, 0, 0, 0]
    if lmList[19][2] > lmList[20][2]:
        res[0] = 1
    if lmList[15][2] > lmList[16][2]:
        res[1] = 1
    if lmList[11][2] > lmList[12][2]:
        res[2] = 1
    if lmList[7][2] > lmList[8][2]:
        res[3] = 1
    if lmList[3][1] < lmList[4][1]:
        res[4] = 1
    return res

def valueCal(res):
    n=0
    for i in range(len(res)):
        n+=(2**i)*res[i]
    return n

def alphaCal(n):
    if n==0:
        return ""
    elif n<=26 :
        return chr(64+n)
    elif n==31:
        return "Hi"
    else:
        return ": )"

