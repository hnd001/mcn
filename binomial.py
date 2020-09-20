import math

def cProduct(n): #Tính giai thừa
    r = 1
    for i in range (1, n+1):
        r *= i
    return r

def comb(k, N): #Tính tổ hợp chập k của N
    r = cProduct(N) / (cProduct(k) * cProduct(N-k))
    return r

def prob(n, p, N):
    r = (p ** n) * ((1-p) ** (N - n))
    return comb(n, N) * r

def infoMeasure(n, p, N):
    r = prob(n, p, N)
    return - r * math.log2(r)

def sumProb(N, p):
    '''
    Trả về tổng xác suất của tất cả các symbols phân bố theo phân bố binomial
    :param N: int
    :param p: float
    '''
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p, N)
    return sum

def approxEntropy(N, p):
    '''
    Trả về giá trị float là trung bình lượng tin của tất cả symbols (entropy) của nguồn tin binomial
    :param N: int
    :param p: float
    '''
    sum = 0
    for i in range(1, N+1):
        sum += infoMeasure(i, p, N)
    return sum

help(sumProb)
help(approxEntropy)
print("sumProb(1000,0.4) = ",sumProb(1000,0.4))
print("approxEntropy(1000,0.5) = ",approxEntropy(1000,0.5))