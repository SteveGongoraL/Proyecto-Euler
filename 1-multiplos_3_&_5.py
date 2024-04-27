#Buscar los numeros que son multiplos de 3 o 5 y sumarlos (incluir los numeros por debajo del numero proporcionado).

def multiplesOf3and5(number):
  x=0
  for i in range(1,number):
    if i%3==0 or i%5==0:
      x += i
      #print(x)
  return x

print(multiplesOf3and5(10))
