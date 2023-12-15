
dia = int(input("Escriba la cantidad de dias "))
print(dia)

valorDolar = []

for i in range (0,dia):
    valor = float(input(f"Escriba el valor del dia {i+1} "))
    valorDolar.append(valor)

incremento = 0
contador=0
for i in valorDolar:
    if contador != 0:
        if valorDolar[contador] - valorDolar[contador-1] > incremento:
            incremento = valorDolar[contador] - valorDolar[contador-1]
    contador+=1

print(incremento)




    

    