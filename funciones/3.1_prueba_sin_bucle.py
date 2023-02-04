import pandas as pd

def dejar_solo_cifras(df):
  return "".join(c for c in df if c.isdigit())

def VSA_Method(): 
#VARIABLES
## %var: saber si cierra en negativo o en positivo
## vol 0: volumen en el día de hoy (en la tabla es la fila 1)
## vol 1: volumen en el día de ayer (en la tabla es la fila 2)
## vol 2: volumen en el día anteayer (en la tabla es la fila 3)

## Leer el archivo en formato pandas
  df = pd.read_csv("VSA_Datos_Nasdaq100.csv",decimal=",")
  df.head

#cambiar el nombre de los headers
  df.columns = ["Fecha","Ultimo","Apertura","Maximo","Minimo","Vol","Variacion","VSA"]
  
#dejar solo cifras (llamada a la funcion)
  df["Vol"] = df["Vol"].map(dejar_solo_cifras)

#cambiar la coma de variacion por punto
  df["Variacion"] = df["Variacion"].apply(lambda x: x.replace(",","."))
#quitar el porcentaje
  df["Variacion"] = df["Variacion"].apply(lambda x: x.replace("%",""))
  #print(df)

## Declaración varibles y la lista

  vol_0 = 0
  vol_1 = 0
  vol_2 = 0
  variacion = 0
  variacion_1 = 0
  variacion_2 = 0
  comparacion_volumen = []


  vol_0 = int(float(df.iloc[8,5]))
  vol_1 = int(float(df.iloc[9,5]))
  vol_2 = int(float(df.iloc[10,5]))
  variacion = float(df.iloc[8,6])
  #variacion_1 = int(float(df.iloc[2,6]))
  #variacion_2 = int(float(df.iloc[3,6]))

  #COMPROBACION DE LA LECTURA DEL DATAFRAME
  print( "                                                                     ")
  print( "#######################################################################" )
  print( "######################### COMPROBACIÓN ################################" )
  print( "#######################################################################" )
  print( "                                                                     ")
  print(df)
  print(vol_0)
  print(type(vol_0))
  print(vol_1)
  print(type(vol_1))
  print(vol_2)
  print(type(vol_2))
  print(variacion)
  print(type(variacion))

  if (vol_0 > vol_1) and (vol_0 > vol_2) and  variacion < 0 :
    df["VSA"][8] = "S"

## DEMANDA
## Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
  elif vol_0 > vol_1 and vol_0 > vol_2 and variacion > 0 :
    df["VSA"][8] = "D"

  elif (vol_0 > vol_1) and (vol_0 > vol_2) and  variacion < 0 :
    df["VSA"][8] = "S"

## NO DEMANDA
### Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
  elif vol_0 < vol_1 and vol_0 < vol_2 and variacion > 0:
    df["VSA"][8] = "Nd"

## NO OFERTA
### Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
  elif vol_0 < vol_1 and vol_0 < vol_2 and variacion < 0:
    df["VSA"][8] = "Ns"
  
  else:
    df["VSA"][8] = "Nada"
  print( "                                                                     ")
  print( "#####################################################################" )
  print( "######################### METODO VSA ################################" )
  print( "#####################################################################" )
  print( "                                                                     ")
  print(df)

VSA_Method()