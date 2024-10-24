#creaceion lista ordenada


import pandas as pd
datos ={
    'nombres':['jhon','andres','ana','juan','marios'],
    'edad':[22,None,16,None,21],
    'carrera':['sistemas','electronica','sistemas','electronica','sistemas']
    
    
}
df = pd.DataFrame(datos)
df

print (df['nombres'])


#sacar promedo 


promedio =df['edad'].mean()
print (promedio)


#sacar estudiantes de tal carrera


sietasm=df[df['carrera']=='sistemas']
print (sietasm)


#estudiantes  de sistemas que tienen mas de 21 años 


sietasms=df[(df['carrera']=='sistemas') & (df['edad']>21)]
print (sietasms)


#como imputar datos 

dfnull = pd.DataFrame(datos)
print (dfnull)



#sin valores nulos

df_sin_nulos = dfnull.dropna(subset=['edad'])
print (df_sin_nulos)


#rellena datos faltantes

dfnull['edad']=dfnull['edad'].fillna(df['edad'].mean())
print (dfnull)