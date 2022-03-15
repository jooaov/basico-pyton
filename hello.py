from obj import Point
from obj2 import pont3D
# loop
#array
fruits = ["apple", "banana", "cherry"]
for x in fruits:
   print('') 
#loop while

#bolleanos começam em letra maiuscula
verdadeiro=True
contador=0
while verdadeiro:
    print()
    contador=contador+1
    if contador == 5:
        verdadeiro=False
# if
nome="joao"
if nome=="joao":
    print('')
#dicionario
dicio = {'chave': 'valor'}

#objeto
p=pont3D(0,0)
p.setX(1)
p.setY(2)

#
p.__alias="teste editado"
p.x=9
p.y=10
p.printAll()



