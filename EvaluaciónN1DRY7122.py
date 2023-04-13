print("Evaluación N°1 Programación y Redes Virtualizadas")
asignatura = input("Ingrese el nombre de su asignatura: ")
cant_integrantes = int(input("Ingrese la cantidad de integrantes en el grupo: "))

integrantes = []

for i in range(cant_integrantes):
    nombre = input("Ingrese el nombre del integrante {}: ".format(i+1))
    integrantes.append(nombre)

print("La asignatura es: ", asignatura)
print("La cantidad de integrantes es: ", cant_integrantes)
print("Los integrantes son: ")
for integrante in integrantes:
    print("-", integrante)

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

alumnos = []

for i in range(cantidad_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    seccion = input("Ingrese la sección del alumno: ")
    sede = input("Ingrese la sede del alumno: ")

    alumnos.append((nombre, apellido, seccion, sede))

print("Información de los alumnos:")
for alumno in alumnos:
    print("Nombre:", alumno[0])
    print("Apellido:", alumno[1])
    print("Sección:", alumno[2])
    print("Sede:", alumno[3])
    print("--------------------------------------")

for i in range(3):
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    seccion = input("Ingrese su sección: ")
    sede = input("Ingrese su sede: ")

    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Código:", codigo)
    print("Sección:", seccion)
    print("Sede:", sede)

asignatura = input("Ingrese nombre de la asignatura: ")

integrante = input("Por favor, ingrese el nombre de 1 integrante: ")

acl_num = input("Ingrese el número de ACL IPv4: ")

try:
    acl_num = int(acl_num)
except ValueError:
    print("El número ingresado no es válido.")
    exit()

if acl_num >= 1 and acl_num <= 99:
    print("La ACL", acl_num, "es una ACL Estándar.")
elif acl_num >= 100 and acl_num <= 199:
    print("La ACL", acl_num, "es una ACL Extendida.")
else:
    print("El número ingresado no corresponde a una lista de acceso IPv4.")