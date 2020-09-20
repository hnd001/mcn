import math

def prob(n, p):
    r = (1 - p) ** (n - 1)
    return r * p

def infoMeasure(n, p):
    r = prob(n, p)
    return - r * math.log2(r)

def sumProb(N, p):
    '''
    Trả về tổng xác suất của tất cả các symbols phân bố theo phân bố geometric
    :param N: int
    :param p: float
    '''
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p)
    return sum

def approxEntropy(N, p):
    '''
    Trả về giá trị float là trung bình lượng tin của tất cả symbols (entropy) của nguồn tin geometric
    :param N: int
    :param p: float
    '''
    sum = 0
    for i in range(1, N+1):
        sum += infoMeasure(i, p)
    return sum

help(sumProb)
help(approxEntropy)
print("sumProb(1000,0.4) = ",sumProb(1000,0.4))
print("approxEntropy(1000,0.5) = ",approxEntropy(100,0.5))