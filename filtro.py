import sys

precios = {'Notebook': 700000,
 'Teclado': 25000,
 'Mouse': 12000,
 'Monitor': 250000,
 'Escritorio': 135000,
 'Tarjeta de Video': 1500000}

if len(sys.argv) == 1:
     print("Debe indicarse umbral")
     sys.exit()
elif len(sys.argv) > 2 and sys.argv[2] == "menor":
    arg_2 = sys.argv[2]
elif len(sys.argv) > 2 and sys.argv[2] != "menor":
        print("Lo sentimos, no es una operación válida")
        sys.exit()
else:
    arg_2 = None

umbral = [int(sys.argv[1])]
umbral.append(arg_2)

def filtro_precio(precios:dict, umbral): 
    if umbral[1] == "menor":
         for k,v in precios.items():
            print(f"Los productos menores al umbral son: {k}: {v < int(umbral[0])}")
    else:
            for k,v in precios.items():
                print(f"Los productos mayores al umbral son: {k}: {v > int(umbral[0])}")
    return filtro_precio

print(filtro_precio(precios, umbral))