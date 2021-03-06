import sympy as sy
from sympy import *
import numpy as np
from sympy.functions import sin,cos
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# Define the variable and the function to approximate

#  fact = int(input('Enter a value for the factorial \n'))
# Factorial function
# def factorial(n):
#     if n <= 0:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# print(str(factorial(fact)))

# We have to create a "symbol" called x
x = Symbol('x')
fx= x**2/20
fx_prime = fx.diff(x)

fxOutputResult = lambdify(x,fx_prime)

print(fx_prime)
print(fxOutputResult(4))

# Define the variable and the function to approximate
x = sy.Symbol('x')
f = x**2/20

xAxisVal = np.array(range(10))
yAxisVal = xAxisVal ** 2/20

# Factorial function
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

# Taylor approximation at x0 of the function 'function'
def taylor(function,x0,n):
    i = 0
    p = 0
    while i <= n:
        print(i)
        p = p + (function.diff(x,i).subs(x,x0))/(factorial(i))(x-x0)*i
        i += 1
    return p

# Plot results
def plot():
    x_lims = [-5,5]
    x1 = np.linspace(x_lims[0],x_lims[1],800)
    y1 = []
    # Approximate up until 10 starting from 1 and using steps of 2
    for j in range(1,4,1):
        func = taylor(f,0,j)
        print('Taylor expansion at n='+str(j),func)
        for k in x1:
            y1.append(func.subs(x,k))
        plt.plot(x1,y1,label='order '+str(j))
        y1 = []
    fprime = f.diff(x)
    fxPrime    = lambdify(x, fprime)
    # Plot the function to approximate (sine, in this case)
    #plt.plot(x1,fxPrime,label='Original Function Plot')
    plt.xlim(x_lims)
    plt.ylim([-5,5])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title('Taylor series approximation')
    plt.show()

plot()