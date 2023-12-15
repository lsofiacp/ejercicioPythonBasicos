producto = input("Escoga el producto: A. 270  B.  340  C. 390: ")

costo = 0
if producto == "A": 
    print("Seleccionaste el producto A")
    costo = 270

elif producto == "B": 
    print("Seleccionaste el producto B")
    costo = 340

elif producto == "C": 
    print("Seleccionaste el producto C")
    costo = 390

else:
 print("El codigo escogido no es correcto")

sumamonedas = 0

while sumamonedas < costo:
    monedas=int(input("Ingrese sus monedas: "))

    if monedas == 10:
       monedas = 10

    elif  monedas == 50:
        monedas = 50

    elif monedas == 100:
        monedas = 100

    sumamonedas = sumamonedas+monedas

regreso = sumamonedas - costo

if  regreso == 0:
    print("Su regreso es 0 ")

while regreso!=0:
    if regreso >= 100:
        regresototal = regreso - 100
        print("100")

    elif regreso >=50 and regreso < 100:    
        regrestotal = regreso - 50
        print("50")
            
    elif regreso < 50:
        regresototal = regreso - 10
        print("10")

    regreso = regresototal




