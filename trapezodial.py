from math import sin,e,pi
def f(x):
    return ((sin(x))/(e**x))


def trapezoidal(x0,xn,n):

    h = (xn - x0) / n
    integration = f(x0) + f(xn)
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)
    integration = integration * h/2
    return integration
sub_interval = int(input("Enter number of sub intervals: "))
output = trapezoidal(0, pi, sub_interval)
print("The value of integration using trapezodial rule is : %0.5f" % (output) )