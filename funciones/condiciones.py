def VSA_Method():
  import pandas as pd
#VARIABLES
## %var: saber si cierra en negativo o en positivo
## vol 0: volumen en el día de hoy (en la tabla es la fila 1)
## vol 1: volumen en el día de ayer (en la tabla es la fila 2)
## vol 2: volumen en el día anteayer (en la tabla es la fila 3)

## Leer el archivo en formato pandas
  df = pd.read_csv("VSA_Datos_historicos_Nasdaq100.csv")
  df.head

#quitar la M del volumen
  df["Vol."] = df["Vol."].replace({"M",""}, regex = True)
#quitar el % del %_var ya que no lo reconoce como variable
  df["%_var"] = df["%_var"].replace({"%_var","variacion"}, regex = True) 

## Declaración varibles y la lista
  vol_0 = 0
  vol_1 = 0
  vol_2 = 0
  variacion = 0
  comparacion_volumen = []

## Crear un bucle para leer el dataframe y almacenar el volumen en la lista
  for i in df:
    vol_0 = df.iloc(i,5)
    vol_1 = df.iloc(i+1,5)
    vol_2 = df.iloc(i+2,5)
    variacion = df.iloc(1,6)

    comparacion_volumen = [vol_0, vol_1, vol_2]

# CONDICIONES
## OFERTA
## Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
  if (vol_0 > vol_1) and (vol_0 > vol_2) and  variacion < 0 :
    i["VSA"] = "S"

## DEMANDA
## Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
  elif vol_0 > vol_1 and vol_0 > vol_2 and variacion > 0 :
    i["VSA"] = "D"

## NO DEMANDA
### Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
  elif vol_0 < vol_1 and vol_0 < vol_2 and variacion < 0:
    i["VSA"] = "Nd"

## NO OFERTA
### Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
  elif vol_0 < vol_1 and vol_0 < vol_2 and variacion < 0:
    i["VSA"] = "Ns"
  else:
    i["VSA"] = " "