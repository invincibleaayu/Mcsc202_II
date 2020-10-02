from math import sin,pow,sqrt

def f(x):
    return ((x**2)-sin(x))

# Implementing Bisection Method
def bisection(a,b,c):
    count = 1
    print('\n\n TABLE FOR BISECTION METHOD ')
    loop_control = True
    while loop_control:
        x0 = (a + b)/2
        print('Step number-%d, x0 = %0.6f and f(x0) = %0.6f' % (count, x0, f(x0)))

        if f(a) * f(x0) < 0:
            b = x0
        else:
            a = x0
        
        count += 1
        loop_control = abs(f(x0)) > c

    print('\nRequired Root is : %0.6f' % x0)


# Input Section
a = float(input('First Guess: '))
b = float(input('Second Guess: '))
correctness = float(input('Tolerable Error: '))




# Checking Correctness of initial guess values and bisecting
if f(a) * f(b) > 0.0:
    print('Please choose the valid value for a and b')
    
else:
    bisection(a,b,correctness)