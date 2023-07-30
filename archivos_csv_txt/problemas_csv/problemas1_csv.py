import pandas as pd
df = pd.read_csv("archivos\\problemas_csv\\datos.csv")
#Conveertir a string los datos de una cilumna.
df["edad"] = df["edad"].astype(str)
#mostrar el tipo de dato del primer elemento de la columna edad.
print(type(df["edad"][0]))
#replace() remplaza el primer elemento con el segundo.
df["apellido"].replace("Vasquez", "Maestro", inplace=True)
print(df["apellido"])
#Dropna() elemina las filas a las que les falte un elemento o dato.
df = df.dropna()
#drop_duplicates() elimina las filas repetidas.
df = df.drop_duplicates()
df.to_csv("archivos\\problemas_csv\\datos_limpios.csv")
#Duplica u archivo a la ruta que le demos.
