import random
#importar datos 
#numeros = [random.randint(1,100) for i in range(10)]
#print( "numeros generados" , numeros)
#crear lista de datos
texto = "hoy es miercoles y mañana es jueves"
#crear lista vacia para llenar los datos 
#split sirve para separar 
contador = {}
for palabra in texto.split():
        palabra= palabra.strip (",")
        if palabra in contador:
            contador[palabra] += 1
        else: 
            contador[palabra] = 1
 
print(contador)