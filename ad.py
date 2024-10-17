
import pandas as pd 


#crear arreglo de datos 

datos={
    'nombre':[' Andres ', 'juan' , 'carlos ','maria'],
    'edad':[12,21,12,32],
    'nota':[3.2,4.2,1.2,1.5]
}

df = pd.DataFrame(datos)
df 

#sacar promedio o media 
media =df['edad'].mean()
media 


mediaC = df['nota'].mean()
mediaC 

#mayores de nota
cal_4 = df[df['nota']>3]


print (cal_4)
















#datos = [1,2,3,0,95,68,77,86,95,104,113,122]
#print(datos[10])



#añadir un dato
#datos.append(5)
#print(datos)



#cambiar datos 
#datos[3] = 6
#print(datos[3])


