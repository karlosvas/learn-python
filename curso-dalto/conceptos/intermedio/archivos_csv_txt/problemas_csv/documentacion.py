nombres = ["Lucas", "Matias", "Carlos", "Alberto"]
apellidos=["Dalto", "Roberrto", "Vasquez", "Chicote"]

with open("archivos\\problemas_csv\\nombre_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son: \n\n")
    [arch.writelines(f"Nombre {n}\n Apellido: {a}\n--------------------\n") for n,a in zip(nombres,apellidos)]