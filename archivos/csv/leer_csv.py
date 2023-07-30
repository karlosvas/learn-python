import csv

with open("archivos\\csv\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)