#abrimos los archivos y los asignamos a variables
archNombres = open("nombres_1.txt", "r", encoding="utf-8")
archNotas1 = open("eval1.txt", "r", encoding="utf-8")
archNotas2 = open("eval2.txt", "r", encoding="utf-8")

#guardo en listas
nomb=archNombres.read().split()
notas1=archNotas1.read().split(",")
notas2=archNotas2.read().split(",")

#inicializo la variablre nTotal donde sumo todas las notas y creo la lista estudiantes donde voy a guardar a cada estudiante
nTotal=0
estudiantes= []

#hago un for y en ambas notas guardo la suma de la primera y segunda nota, creo un diccionario para cada estudiante
#y lo guardo en la lista

for x in range(len(nomb)):
    ambasNotas = int(notas1[x]) + int(notas2[x])
    estudiante = {"nombre":nomb[x], "suma de ambas notas":ambasNotas}
    estudiantes.append(estudiante)
    nTotal = nTotal + ambasNotas

#calculo el promedio
promedio = nTotal / len(nomb)
#recorro la lista y pregunto a cada alumno si la suma de ambas notas es menor al promedio, informo los alumnos que tienen menos nota que el promedio
for i in range(len(nomb)):
    if estudiantes[i]["suma de ambas notas"] < promedio:
        print(estudiantes[i]["nombre"])

#cierro los archivos
archNombres.close()
archNotas1.close()
archNotas2.close()