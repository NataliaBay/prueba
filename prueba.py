n1 = int(input("Ingresa un  número: "))
n2 = int(input("Ingresa un  número: "))

opcion = 0
while True: 
    print("""
            Elige la operación que deseas realizar:
          
                1) Suma
                2) Resta
                3) División
                4) Multiplicación
                
                opcion = int(input("Ingresa el número de la operación a realizar: "))  
""")
  
 
if opcion == 1:
    print("El resultado de la suma es de " ,n1,"+",n2," es igual a: ", n1+n2) 
elif opcion == 2:
    print("El resultado de la resta es de " ,n1,"-",n2," es igual a: ", n1-n2) 
elif opcion == 3:
    print("El resultado de la división es de " ,n1,"/",n2," es igual a: ",n1/n2)
elif opcion == 4:
    print("El resultado de la multiplicación es de " ,n1,"*",n2," es igual a: ", n1*n2) 
else:
    print("Opción incorrecta")
