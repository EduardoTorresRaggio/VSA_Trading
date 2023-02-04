

def VSA_Method(): 
  import pandas as pd
#VARIABLES
## %var: saber si cierra en negativo o en positivo
## vol 0: volumen en el día de hoy (en la tabla es la fila 1)
## vol 1: volumen en el día de ayer (en la tabla es la fila 2)
## vol 2: volumen en el día anteayer (en la tabla es la fila 3)
  print(df)
## Leer el archivo en formato pandas
  df = pd.read_csv("VSA_Datos_Nasdaq100.csv",decimal=",")
  df.head

#quitar la M del volumen
  df["Vol."] = df["Vol."].replace({"M",""}, inplace = True)
#quitar el % del %_var ya que no lo reconoce como variable
  df["%_var."] = df["%_var."].replace({"%_var.","variacion"}, inplace = True) 
#cambiar columna volumenes, las comas por puntos
  #df["Vol."] = df["Vol."].replace({",","."}, inplace = True)
  #df= df.replace({",","."}, regex = True) 
## Declaración varibles y la lista
  print(df)

VSA_Method()