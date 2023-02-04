# especificar el nombre del archivo y la columna que deseas crear
import csv
filename = "Datos_historicos_Nasdaq100.csv"
new_column = "VSA"

# abrir el archivo y crear un objeto de lectura y escritura
with open(filename, 'r') as file_in, open("VSA_Datos_NASDAQ100.csv", "w", newline="") as file_out:
    reader = csv.DictReader(file_in)
    fieldnames = reader.fieldnames
    fieldnames.append(new_column)
    writer = csv.DictWriter(file_out, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        row[new_column] = " " #aqui puedes asignar un valor por defecto
        writer.writerow(row)
