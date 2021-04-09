from math import sin, cos, exp, log, acos, atan, tan

def Newton (f, fder, x0, epsilon, Nitermax) :
    xold = x0
    xnew = f(x0)
    n = 1
    while abs (xnew - xold) > epsilon and n < Nitermax :
        xold = xnew
        xnew = xold - (f(xold) / fder(xold))
        n = n + 1
    return xnew, n

epsilon = 1e-10
Nitermax = 500
'''
Une fonction definie avec le suffixe "der" est la derivee de celle associee
'''
def f1 (x) :
    x = x**4 + 3*x - 9
    return x

def f1der (x) :
    x = 4*x**3 + 3
    return x

alpha1 = Newton (f1, f1der, 2, epsilon, Nitermax)
print (alpha1)

alpha11 = Newton (f1, f1der, -1, epsilon, Nitermax)
print (alpha11)

def f2 (x) :
    x = x - 3 * cos (x) + 2
    return x

def f2der (x) :
    x = 1 + 3 * sin (x)
    return x

alpha2 = Newton (f2, f2der, -5, epsilon, Nitermax)
print (alpha2)

alpha22 = Newton (f2, f2der, 0, epsilon, Nitermax)
print (alpha22)

alpha222 = Newton (f2, f2der, 1, epsilon, Nitermax)
print (alpha222)

def f3 (x) :
    x = x * exp(x) - 7
    return x

def f3der (x) :
    x = exp(x) + x * exp(x)
    return x

alpha3 = Newton (f3, f3der, 2, epsilon, Nitermax)
print (alpha3)

def f4 (x) :
    x = exp(x) - x - 10
    return x

def f4der (x) :
    x = exp(x) - 1
    return x

alpha4 = Newton (f4, f4der, 3, epsilon, Nitermax)
print (alpha4)

alpha44 = Newton (f4, f4der, 0, epsilon, Nitermax)
print (alpha44)

def f5 (x) :
    x = 2 * tan(x) - x - 5
    return x

def f5der (x) :
    x = 2 * (1 / ((cos(x))**2)) - 1
    return x

alpha5 = Newton (f5, f5der, -2, epsilon, Nitermax)
print ("alpha5", alpha5)

def f6 (x) :
    x = exp(x) - x**2 - 3
    return x

def f6der (x) :
    x = exp(x) - 2 * x
    return x

alpha6 = Newton (f6, f6der, 1, epsilon, Nitermax)
print (alpha6)

def f7 (x) :
    x = 3 * x + 4 * log(x) - 7
    return x

def f7der (x) :
    x = exp(x) + (4/x)
    return x

alpha7 = Newton (f7, f7der, 2, epsilon, Nitermax)
print (alpha7)

def f8 (x) :
    x = x**4 - 2 * x**2 + 4 * x - 17
    return x

def f8der (x) :
    x = 4 * x**3 - 2 * x + 4
    return x

alpha8 = Newton (f8, f8der, -2.5, epsilon, Nitermax)
print (alpha8)

alpha88 = Newton (f8, f8der, 2.1, epsilon, Nitermax)
print (alpha88)

def f9 (x) :
    x = exp(x) - 2 * sin (x) - 7
    return x

def f9der (x) :
    x = exp(x) - 2 * cos(x)
    return x

alpha9 = Newton (f9, f9der, 2.5, epsilon, Nitermax)
print (alpha9)

def f10 (x) :
    x = log(x**2 + 4) * exp(x) - 10
    return x

def f10der (x) :
    x = (2 * x / (x**2+4) ) * exp(x) +  log(x**2 + 4) * exp(x)
    return x

alpha10 = Newton (f10, f10der, 2, epsilon, Nitermax)
print (alpha10)