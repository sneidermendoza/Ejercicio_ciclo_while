#teniendo como entrada un numero entero, determina cuantos digitos tiene, cuantos de ellos
#son pares e impares, calcule la sumatoria, la productoria y el promedio de estos.
sumatoria = 0
productoria = 1
count = 0
total_even = 0
odd_total = 0
integer_number = int(input("Por favor ingresa un numero entero positivo: \n"))

while integer_number != 0:
    last_digit = integer_number % 10
    if last_digit % 2 == 0:
        total_even +=1
    else: 
        odd_total += 1
    sumatoria += last_digit
    productoria *= last_digit 
    count += 1 
    integer_number = integer_number // 10

print(f"Hay {total_even} pares y {odd_total} impares")
print(f"este numero tiene {count} digitos ")       
print(f"la sumatoria de este es: {sumatoria}")       
print(f"la productoria es: {productoria}")       
print(f"el promedio es: {sumatoria / count} ")       
