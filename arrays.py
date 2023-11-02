#Criando um array:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#Acessando um elemento:
#import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])

#Verificar o tipo do array:
#import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

#Criando uma cópia do array sem afetar o original:
#import numpy as np
arr = np.array([1, 2, 3, 4])
x=arr.copy()
x[0]=42
print(arr)
print(x)

#View altera o array original:
#import numpy as np
arr = np.array([1, 2, 3, 4])
y=arr.view()
y[0]= 43
print(arr)
print(y)

#Iterando sobre o array:
#import numpy as np
arr = np.array([1, 2, 3, 4])
for x in arr:
    print (x)
