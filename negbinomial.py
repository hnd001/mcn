import math

def cProduct(n): #Tính giai thừa
    rs = 1
    for i in range (1, n+1):
        rs *= i
    return rs

def comb(k, N): #Tính tổ hợp chập k của N
    rs = cProduct(N) / (cProduct(k) * cProduct(N-k))
    return rs

def prob(n, p, r):
    rs = (p ** r) * ((1-p) ** (n))
    return comb(n, n + r - 1 ) * rs

def infoMeasure(n, p, r):
    rs = prob(n, p, r)
    return - rs * math.log2(rs)

def sumProb(N, p, r):
    '''
    Trả về tổng xác suất của tất cả các symbols phân bố theo phân bố Negative binomial
    :param N: int
    :param p: float
    '''
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p, r)
    return sum

def approxEntropy(N, p, r):
    '''
    Trả về giá trị float là trung bình lượng tin của tất cả symbols (entropy) của nguồn tin negative binomial
    :param N: int
    :param p: float
    '''
    sum = 0
    for i in range(1, N+1):
        sum += infoMeasure(i, p, r)
    return sum

help(sumProb)
help(approxEntropy)
print("sumProb(1000, 0.4, 9) = ",sumProb(1000, 0.4, 9))
print("approxEntropy(1000, 0.5, 9) = ",approxEntropy(1000,0.5, 9))