import pandas as pd
#VARIABLES
## %var: saber si cierra en negativo o en positivo
## vol 0: volumen en el día de hoy (en la tabla es la fila 1)
## vol 1: volumen en el día de ayer (en la tabla es la fila 2)
## vol 2: volumen en el día anteayer (en la tabla es la fila 3)

## Leer el archivo en formato pandas
df = pd.read_csv("VSA_Datos_Nasdaq100.csv")
print(df.head)

vol_0 = 0
vol_1 = 0
vol_2 = 0
comparacion_volumen = []

## Crear un bucle para leer el dataframe y almacenar el volumen en la lista
for i in df:
    vol_0 = int(df.iloc[i,5])
    vol_1 = int(df.iloc[i+1,5])
    vol_2 = int(df.iloc[i+2,5])

comparacion_volumen = [vol_0, vol_1, vol_2]
print(comparacion_volumen)