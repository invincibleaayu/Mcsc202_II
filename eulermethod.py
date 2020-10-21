
def f(x,y):
    return (x**2 + x)

def euler(x0,y0,xn,n):
    h = (xn-x0)/n
    print('x0\ty0\tslope\tyn')
    print('-----------------------------------')
    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope
        print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0,y0,slope,yn) )
        print("-----------------------------------")
        y0 = yn
        x0 = x0+h
    print('\nAt x=%.4f, y=%.4f' %(xn,yn))
print('Enter calculation point: ')
xn = float(input('xn = '))
print('Enter number of steps:')
step = int(input('Number of steps = '))
euler(0,1,xn,step)