import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df=pd.read_csv('http://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

#print(df.head(20))

#filtrar y mostrar los que sobrevivieron y mayores a 60 años
#sobrevivientes = df[(df['Survived']==1) & (df['Age']>60)]
#print(sobrevivientes)


#promedio
#sobrevivientes = df[df['Survived']==0] 
#muertos = sobrevivientes['Age'].mean()
#print(muertos)


#visualizacion driagrama  de barras usando 

sbn.countplot(x='Sex', hue='Survived', data=df)
plt.title('Grafica de sobrvivientes vs edad')
plt.show()
