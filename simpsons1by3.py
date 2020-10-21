from math import pi,e,sqrt
def f(x):
    return (e**(-(x/2)))

def simpson(x0,xn,n):

    h = (xn - x0) / n
    
 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    

    integration = integration * h/3
    
    return integration
    
sub_interval = int(input("Enter number of sub intervals: "))

output = simpson(-4, 4, sub_interval)
output=sqrt(1/(2*pi)) * output
print("Simpson's 1/3 method gives integration: %0.4f" % (output) )