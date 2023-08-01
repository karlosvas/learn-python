import pandas as pd
df = pd.read_csv("archivos\\csv\\datos.csv")
df2 = pd.read_csv("archivos\\csv\\datos.csv")
#Slaising
#Obteniendo a los datos del nombre
nombres = df["nombre"]
cadena = "0123456789"
print(cadena[2:7])
#Ordenando el datafreme por la edad.
df_ordenado = df.sort_values("edad")
#Ordenando el dataframe por la edad de forma invertida
df_invertido = df.sort_values("edad",ascending=False)
#Concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])
#Devuelbe el dataframe de las columnas, accediendo a las 2 primeras filas con head()
primeras_filas = df.head(2)
#accediendo a las ultimas 2 filas con tail()
ultimas_filas = df.tail(2)
#Accediendo a la cantidad de filas y coklumnas con shape
filas_totales, columnas_totales = df.shape
#Accediendo a un elemento especifico del dataframe
df_info = df.describe()
#Accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2, "edad"]
elemento_especifico_loc = df.iloc[2, 2]
#Accediendo a todas las filas de una columna
apellidos = df.loc["apellidos", :]
apellidos = df.iloc[1, :]
apellidos = df.loc[2, :]
apellidos = df.iloc[2, :]
#Accediendo a los mayores de 30
menor_30 = df.loc[df["edad"] < 30,:]
print(apellidos)
