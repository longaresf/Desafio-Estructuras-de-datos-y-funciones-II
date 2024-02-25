opcion = input("Favor ingrese 'f' para factorial o 'p' para productoria: ")
while opcion != "f" and opcion != "p":
    opcion = input("Error, favor ingrese 'f' para factorial o 'p' para productoria: ")
    
def calc_factorial_productoria(opcion):
    if opcion == "f":
        num = int(input("Ingrese un numero entero positivo: "))
        num_fact = num
        fact = 1
        while num > 0:
            fact *= num
            num -= 1
        print(f"El factorial de {num_fact} es {fact}")
    else:
        num_acum = []
        acum_frec = 0

        while int(acum_frec) < 5: 
            num_prod = input(f"Favor digite 5 números, empezando con número: {acum_frec}: ")
            num_acum.append(num_prod)
            acum_frec += 1
            prod:int = 1
        for i in num_acum:
            prod *= int(i)
        print(f"La productoria de {num_acum} es: {prod}\n")

calc_factorial_productoria(opcion)