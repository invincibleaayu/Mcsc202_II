import numpy as np
def u_cal(u, n): 

	temp = u  
	for i in range(1, n): 
		temp = temp * (u - i)  
	return temp  

def fact(n): 
	f = 1  
	for i in range(2, n + 1): 
		f *= i  
	return f  


n = 6  
x = [ 0.20,0.22,0.24,0.26,0.28,0.30 ]  
	
 
y = [[0 for i in range(n)] 
		for j in range(n)]  
y[0][0] = 1.6596
y[1][0] = 1.6698  
y[2][0] = 1.6804  
y[3][0] = 1.6912  
y[4][0]=1.7024
y[5][0]=1.7139

# Calculating the forward difference 
# table 
for i in range(1, n): 
	for j in range(n - i): 
		y[j][i] = np.around(y[j + 1][i - 1] - y[j][i - 1] , decimals=3)

# Displaying the forward difference table 
for i in range(n): 
	print(x[i], end = "\t")  
	for j in range(n - i): 
		print(y[i][j], end = "\t")  
	print("")  
def calculate(value):
    # Value to interpolate at 
 

    # initializing u and sum 
    sum = y[0][0]  
    u = (value - x[0]) / (x[1] - x[0])  
    for i in range(1,n): 
        sum = sum + (u_cal(u, i) * y[0][i]) / fact(i)  

    print("\nValue at", value, 
        "is", round(sum, 6))  

calculate(0.21)
calculate(0.29)





