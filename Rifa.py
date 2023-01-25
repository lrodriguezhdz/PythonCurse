# Usar listas# Leer el archivo txt de los nombres# Usar random()
# # Usar pycountry para generar el país
# # Usar openpyxl para exportar datos a excel
# # Genear un archivo de Excel donde aparezca en la primera columna los nombres de todos los participantes
# # del día 5. En la segunda columna, poner el monto que cada quien obtuvo de la lotería (ejemplo, 1,000,000)
# # En la tercera columna, debe reflejarse el país que se le asignó de manera aleatoria.
import openpyxl
import random
from pycountry import countries
wb = openpyxl.Workbook()

archivo=open('Lista_20_enero.txt')
partners=archivo.read()
partners=partners.split("\n")

paises=[]
montos=[]
total=1000000
for i in partners:
    restar=random.randint(0,total)
    total=total-restar
    montos.append(restar)
    if i==1:
      montos.append(total)
      break


for i in partners:
    paises.append(list(countries)[random.randint(0,len(countries)-1)].name)


hoja = wb.active
hoja.append(('Nombre','Monto','Pais'))

resultado=[]
objeto=[]
limit=int(len(partners)-1)
print(limit)
for i in range(limit):
    objeto.append(partners[i])
    objeto.append(montos[i])
    objeto.append(paises[i])
    resultado.append(objeto)
    objeto=[]

print(montos)
print(paises)
print(resultado)

for i in resultado:
    hoja.append(i) 

wb.save('paises.xlsx')
    


            