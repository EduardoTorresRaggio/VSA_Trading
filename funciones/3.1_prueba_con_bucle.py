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
  df.columns = ["Fecha","Ultimo","Apertura","Maximo","Minimo","Vol","#variacion","VSA"]
  
#dejar solo cifras (llamada a la funcion)
  df["Vol"] = df["Vol"].map(dejar_solo_cifras)

#cambiar la coma de #variacion por punto
  df["#variacion"] = df["#variacion"].apply(lambda x: x.replace(",","."))
#quitar el porcentaje
  df["#variacion"] = df["#variacion"].apply(lambda x: x.replace("%",""))
  #print(df)

## Declaración varibles y la lista

  # subset[j] = 0
  # subset[j+1] = 0
  # subset[j+2] = 0
  #variacion = 0
  #variacion_1 = 0
  #variacion_2 = 0
  #comparacion_volumen = []
  subset =[]
  column = df["Vol"]
  for index in range(0,len(df),3):
    
    if not subset:
      print("La lista está vacía")
      subset = column.iloc[0:index+3].values
      subset_ult3 = subset
      print( "                                                                     ")
      print( "#######################################################################" )
      print( "######################### COMPROBACIÓN ################################" )
      print( "#######################################################################" )
      print( "                                                                     ")
      print(subset)
      print(subset_ult3)
      #subset[j] = int(float(df.iloc[index,5]))
      #subset[j+1] = int(float(df.iloc[index,5]))
      #subset[j+2] = int(float(df.iloc[index,5]))
      ##variacion = float(df.iloc[(index,6)])

      for j in range(len(subset_ult3)-1):

          if (subset_ult3[j] > subset_ult3[j+1]) and (subset_ult3[j] > subset_ult3[j+2]):   ##variacion < 0 :
            df["VSA"][index] = "S"
            print( "                                                                     ")
            print( "#####################################################################" )
            print( "######################### METODO VSA ################################" )
            print( "#####################################################################" )
            print( "                                                                     ")
            print(df)

        ## DEMANDA
        ## Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
          elif subset_ult3[j] > subset_ult3[j+1] and subset_ult3[j] > subset_ult3[j+2]: #and #variacion > 0 :
            df["VSA"][index] = "D"
            print( "                                                                     ")
            print( "#####################################################################" )
            print( "######################### METODO VSA ################################" )
            print( "#####################################################################" )
            print( "                                                                     ")
            print(df)

          elif (subset_ult3[j] > subset_ult3[j+1]) and (subset_ult3[j] > subset_ult3[j+2]): #and  #variacion < 0 :
            df["VSA"][index] = "S"
            print( "                                                                     ")
            print( "#####################################################################" )
            print( "######################### METODO VSA ################################" )
            print( "#####################################################################" )
            print( "                                                                     ")
            print(df)

        ## NO DEMANDA
        ### Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
          elif subset_ult3[j] < subset_ult3[j+1] and subset_ult3[j] < subset_ult3[j+2]: #and #variacion > 0:
            df["VSA"][index] = "Nd"
            print( "                                                                     ")
            print( "#####################################################################" )
            print( "######################### METODO VSA ################################" )
            print( "#####################################################################" )
            print( "                                                                     ")
            print(df)

        ## NO OFERTA
        ### Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
          elif subset_ult3[j] < subset_ult3[j+1] and subset_ult3[j] < subset_ult3[j+2]: #and #variacion < 0:
            df["VSA"][index] = "Ns"
            print( "                                                                     ")
            print( "#####################################################################" )
            print( "######################### METODO VSA ################################" )
            print( "#####################################################################" )
            print( "                                                                     ")
            print(df)
        
          else:
            df["VSA"][index] = "Nada"
            print( "                                                                     ")
            print( "#####################################################################" )
            print( "######################### METODO VSA ################################" )
            print( "#####################################################################" )
            print( "                                                                     ")
            print(df)
      break
    else:
      subset_ult3 = subset[1:]
      print( "                                                                     ")
      print( "#######################################################################" )
      print( "######################### COMPROBACIÓN ################################" )
      print( "#######################################################################" )
      print( "                                                                     ")
      print(subset)
      print(subset_ult3)
    
      for j in range(len(subset_ult3)):

          if (subset_ult3[j] > subset_ult3[j+1]) and (subset_ult3[j] > subset_ult3[j+2]):   ##variacion < 0 :
            df["VSA"][index] = "S"

        ## DEMANDA
        ## Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
          elif subset_ult3[j] > subset_ult3[j+1] and subset_ult3[j] > subset_ult3[j+2]: #and #variacion > 0 :
            df["VSA"][index] = "D"

          elif (subset_ult3[j] > subset_ult3[j+1]) and (subset_ult3[j] > subset_ult3[j+2]): #and  #variacion < 0 :
            df["VSA"][index] = "S"

        ## NO DEMANDA
        ### Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
          elif subset_ult3[j] < subset_ult3[j+1] and subset_ult3[j] < subset_ult3[j+2]: #and #variacion > 0:
            df["VSA"][index] = "Nd"

        ## NO OFERTA
        ### Si el %var es < 0 + volumen de ese día es mayor que los dos anteriores
          elif subset_ult3[j] < subset_ult3[j+1] and subset_ult3[j] < subset_ult3[j+2]: #and #variacion < 0:
            df["VSA"][index] = "Ns"

          
          else:
            df["VSA"][index] = "Nada"

          print( "                                                                     ")
          print( "#####################################################################" )
          print( "######################### METODO VSA ################################" )
          print( "#####################################################################" )
          print( "                                                                     ")
          print(df)
          break

VSA_Method()