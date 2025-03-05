import numpy as np

# Hàm để lấy thông tin về hàm tối ưu hóa
def Get_Functions_details3(F):
    if F == 'F1':
        return F1, -2, 2, 10
    elif F == 'F2':
        return F2, -10, 10, 10
    elif F == 'F3':
        return F3, -5.12, 5.12, 10
    elif F == 'F4':
        return F4, -30, 30, 10
    elif F == 'F5':
        return F5, -100, 100, 10
    elif F == 'F11':
        return F11, -500, 500, 10
    elif F == 'F9':
        return F9, -5.12, 5.12, 10
    elif F == 'F6':
        return F6, -32, 32, 10
    elif F == 'F44':
        return F44, -600, 600, 10
    elif F == 'F7':
        return F7, -50, 50, 10
    elif F == 'F8':
        return F8, -50, 50, 10
    else:
        return None, None, None, None

def Get_Functions_details2(F):
    if F == 'F1':
        return F1, -2, 2, 50
    elif F == 'F2':
        return F2, -10, 10, 50
    elif F == 'F3':
        return F3, -5.12, 5.12, 50
    elif F == 'F4':
        return F4, -30, 30, 50
    elif F == 'F5':
        return F5, -100, 100, 50
    elif F == 'F11':
        return F11, -500, 500, 50
    elif F == 'F9':
        return F9, -5.12, 5.12, 50
    elif F == 'F6':
        return F6, -32, 32, 50
    elif F == 'F44':
        return F44, -600, 600, 50
    elif F == 'F7':
        return F7, -50, 50, 50
    elif F == 'F8':
        return F8, -50, 50, 50
    else:
        return None, None, None, None

def Get_Functions_details1(F):
    if F == 'F1':
        return F1, -2, 2, 30
    elif F == 'F2':
        return F2, -10, 10, 30
    elif F == 'F3':
        return F3, -5.12, 5.12, 30
    elif F == 'F4':
        return F4, -30, 30, 30
    elif F == 'F5':
        return F5, -100, 100, 30
    elif F == 'F11':
        return F11, -500, 500, 30
    elif F == 'F9':
        return F9, -5.12, 5.12, 30
    elif F == 'F6':
        return F6, -32, 32, 30
    elif F == 'F44':
        return F44, -600, 600, 30
    elif F == 'F7':
        return F7, -50, 50, 30
    elif F == 'F8':
        return F8, -50, 50, 30
    else:
        return None, None, None, None



def F1(x):
    return np.sum(x**2)

def F2(x):
    return np.sum(np.abs(x)) + np.prod(np.abs(x))

def F3(x):
    dim = x.shape[0]
    o = 0
    for i in range(dim):
        o += np.sum(x[:i+1])**2
    return o



def F4(x):
    dim = x.shape[0]
    return np.sum(100 * (x[1:dim] - x[:dim-1]**2)**2 + (x[:dim-1] - 1)**2)

def F5(x):
    return np.sum(np.abs(x + 0.5)**2)


def F6(x):
    dim = x.shape[0]
    return -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / dim)) - \
        np.exp(np.sum(np.cos(2 * np.pi * x)) / dim) + 20 + np.exp(1)


def F7(x):
    dim = x.shape[0]
    a = np.array([3, 10, 30])
    c = np.array([1, 1.2, 3, 3.2])
    p = np.array([[0.3689, 0.117, 0.2673],
                  [0.4699, 0.4387, 0.747],
                  [0.1091, 0.8732, 0.5547],
                  [0.03815, 0.5743, 0.8828]])
    return (np.pi / dim) * (10 * ((np.sin(np.pi * (1 + (x[0] + 1) / 4)))**2) + \
        np.sum((((x[:dim-1] + 1) / 4)**2) * (1 + 10 * ((np.sin(np.pi * (1 + (x[1:dim] + 1) / 4)))**2))) + \
        (((x[dim-1] + 1) / 4)**2)) + np.sum(Ufun(x, 10, 100, 4))

def F8(x):
    dim = x.shape[0]
    a = np.array([3, 10, 30])
    c = np.array([1, 1.2, 3, 3.2])
    p = np.array([[0.3689, 0.117, 0.2673],
                  [0.4699, 0.4387, 0.747],
                  [0.1091, 0.8732, 0.5547],
                  [0.03815, 0.5743, 0.8828]])
    return 0.1 * ((np.sin(3 * np.pi * x[0]))**2 + \
        np.sum((x[:dim-1] - 1)**2 * (1 + (np.sin(3 * np.pi * x[1:dim]))**2)) + \
        ((x[dim-1] - 1)**2) * (1 + (np.sin(2 * np.pi * x[dim-1]))**2)) + np.sum(Ufun(x, 5, 100, 4))


def F11(x):
    return np.sum(-x * np.sin(np.sqrt(np.abs(x))))

def F9(x):
    dim = x.shape[0]
    return np.sum(x**2 - 10 * np.cos(2 * np.pi * x)) + 10 * dim

def F44(x):
    dim = x.shape[0]
    return np.sum(x**2) / 4000 - np.prod(np.cos(x / np.sqrt(np.arange(1, dim+1)))) + 1


def Ufun(x, a, k, m):
    return k * ((x - a)**m) * (x > a) + k * ((-x - a)**m) * (x < -a)

# Định nghĩa các hàm tối ưu hóa
def F24(x):
    A = 10
    n = len(x)
    return A * n + sum([xi**2 - A * np.cos(2 * np.pi * xi) for xi in x])