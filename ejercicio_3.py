# de los n elementos de la serie de fibonacci diga cuantos son pares,
# cuantos impares y cuantos Ceros 
a = 0
c = 0
b = 1
even = 0
odd = 0
n = int(input("Por favor, ingrese el numero limite de la secuencia del fibonacci: "))

while n > a :
   c = a 
   a = b
   b = c + a
   if a % 2 == 0:
      even += 1
   else:
      odd += 1
  
   print(a)

print(f"la catidad de pares es: {even}")
print(f"la catidad de impares es: {odd}")

   
