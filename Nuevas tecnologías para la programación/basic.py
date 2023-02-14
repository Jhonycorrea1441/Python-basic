dato1=50
dato2=20

# Se usa para comentar una linea

"""
Se utiliza para comentar multiples lineas
"""

#print(dato1 + " "+ str(dato2))


#Estructuras condicionales

""""
if dato1 > dato2:
    if dato1 > 30:
        print("Dato1 es mayor que dato 1 y es mayor a 30")
    else:
            print("Dato1 solo es mayor a dato2 y no es mayor a 30")
else:
    print("Dato2 es mayor a dato1")
"""


""""
calificacion = 100
if calificacion >= 90:
    print("Aprobado con excelencia")
elif calificacion >= 80:
    print("Aprobado")
else:
    print("Reprobado")
"""

# Ciclos While
"""
contador = 10
while contador>0:
    print(contador)
    contador = contador -1
"""


# Coclos FOR
"""
for x in "banana":
    print(x)
"""

"""
fruits = ["apple","banana", "cherry"]
for x in fruits:
    print(x)
    if x == "apple":
        break
print("Se completo con exito la instrucción")
"""

"""
start = "20"
end= "200"
for x in range(int(start),int(end)):
    print(x)
print("Se completo con exito la instrucción")
"""

fruits =["apple", "banana", "cherry"]
for x in fruits:
    if x =="banana":
        continue
    print(x)