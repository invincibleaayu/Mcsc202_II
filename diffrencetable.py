import numpy as np
from math import e
import pandas as import pdb; pdb.set_trace()

data=np.linspace(-1,1,19)
x_value=np.around(data,decimals=3)
count=(len(x_value))
print(count)
table=np.zeros((count,count))
y_value=[]
for i in x_value:
    y_value.append(np.around((e**i),decimals=3))
table[:,0]=y_value
#to calculate diffrence
for i in range(1, count): 
    for j in range(count - i): 
        table[j][i] = np.around(table[j + 1][i - 1] - table[j][i - 1],3)


#now to draw table
column_names = ["Y", "△1", "△2", "△3", "△4", "△5", "△6", "△7", "△8", "△9", "△10", "△11", "△12", "△13", "△14", "△15", "△16", "△17", "△18"]
draw=pd.DataFrame(table,x_value,column_names)
print(draw)









