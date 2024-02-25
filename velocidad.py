velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

def velocidad_promedio(velocidad:list):
    sum_vel:int = 0
    for i in velocidad:
        sum_vel += i
        
    Cant_element =  len(velocidad)
    promedio = (sum_vel / Cant_element )
    print(f"Cant_element: {Cant_element}\npromedio: {promedio}")
    lista_ordenada_velocidades = set([i for i in velocidad if i > promedio])
    print("Lista de velocidades superiores al promedio en cintas transportadoras")
    return lista_ordenada_velocidades

print(velocidad_promedio(velocidad))
