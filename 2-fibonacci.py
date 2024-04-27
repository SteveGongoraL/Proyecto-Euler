#Codigo de serie fibonacci que sume los numeros que sean pares y que sean menor o igual al numero de elementos deseados.

def fiboEvenSum(n):
    x=z=total = 0
    y = 1
    for i in range(0,n):
        z = x + y
        x = y
        y = z
        #print(z)
        if z % 2 == 0 and z <= n:
            total += z
    return(total)
    
print(fiboEvenSum(8))