import numpy as np

a=np.array([0,1,2,3,4])
print(a.size)#tamaño del array
print(a.ndim)#dimension del array
print(a.shape)#el tamaño en cada dimesion( en este caso como es una sola dimesion el size de esa unica dimesion es 5)
print(a.dtype)
#NOTA: la variable 'a' se comporta como una lista
#cuando queremos cambiar un elemento o recortar la lista

x=np.array([1,2,3,4,5,4])
y=np.array([5,6,7,8,9,5])
z=x+y
print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(2*x)
print(x/2)
print(y.mean())#devulve el promedio
print(x.max())#devulve el maximo valor
print(x.min())#devuelve el minimo valor
x=np.array([0, np.pi/2, np.pi])
print(x)
y=np.sin(x)
for item in y:
    print(int(item))

list_test=np.linspace(-2,2, num=10)
#devulve una lista con el rango del 1er parametro pero con el tamaño del 2do parametro
print(list_test)
print("****************************************************************************************************")
b=np.array([[1,2,3],[4,5,6],[7,8,9]])#la 1ra lista representa la 1ra dimension y el set de listas representa la 2da dimension, siendo esto un array de dos dimensiones

print(b)
print(b.shape)
print(b.ndim)
print(b[1][2])
print(b[0:2,2])
print("///////////////////////////////////////////")
a=np.array([-1,1]) 

b=np.array([1,1]) 
print(a*b)

print(np.dot(a,b) )
X=np.array([[1,0,1],[2,2,2]]) 

out=X[0:5,2]
print(out)