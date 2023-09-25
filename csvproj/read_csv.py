import csv

def read_csv(path):  #el path es la entrada, y debemos decir donde esta ubicado el archivo csv que vamos a leer
  with open(path, 'r') as csvfile: #la r es para darle permiso solo de lectura, open es una instruccion que se da para abrir el archivo
    reader = csv.reader(csvfile, delimiter=',')#csv.reader viene de el paquete csv, se tiene que dar el nombre del archivo y un delimitador que depende del csv
    header = next(reader)#esto obtiene la primera fila de forma manual, el next se usa en iterables y da el siguiente valor, en este caso el primero
    data = []#se crea una lista de diccionarios
    for row in reader:#lee cada una de las filas, esta cada una en forma de lista
      iterable = zip(header, row)#con zip se unen dos listas en este caso header con row en tuplas
      country_dict = {key: value for key, value in iterable}#esto es un dictionary comprehension para convertir las tuplas en un diccionario
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])