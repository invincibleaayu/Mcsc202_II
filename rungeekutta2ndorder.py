 
def dydx(x, y) : 
  
    return (x**2+x)   
 
def rungeKutta(x0, y0, x, h) :  
  

    n = round((x - x0) / h)  
      

    y = y0   
    print('x0\ty0\tk1\tk2\tyn')
    print('-----------------------------------')
      
    for i in range(1, n + 1) : 
 
        k1 = h * dydx(x0, y)   
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)   
  
 
        y = y + (1.0 / 6.0) * (k1 + 2 * k2)  
        print('%.4f\t%.4f\t%0.4f\t%.4f\t%.4f'% (x0,y0,k1,k2,y) )
        print('-----------------------------------') 
   
        x0 = x0 + h   
  

  
# x0 = 0 
# y = 1   
# x = 2  h = 0.2   
  
rungeKutta(0, 1, 2, 0.2)  