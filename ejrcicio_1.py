# De n numeros primos contenidos en un intervalo  (por ejemplo los numeros
# primos del 1 al 100), calcule la sumatoria, la productoria y el promedio.
def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

sumatoria = 0
productoria = 1
count = 0

interval_1 = int(input("Por favor, ingrese el primer numero del intervalo: "))
interval_2 = int(input("Por favor, ingrese el segundo nuero de intervalo: "))


while interval_1 <= interval_2:
    if  es_primo(interval_1):
        sumatoria += interval_1
        productoria *= interval_1
        count += 1
    interval_1 += 1

print(f"La sumatoria del intervalo es: {sumatoria}")
print(f"La productoria del intervalo es: {productoria}")
print(f"El promedio del intervalo es: {sumatoria / count}")
    