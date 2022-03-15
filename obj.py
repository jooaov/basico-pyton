class Point:
    """ representa conrdenada x e y"""
#self é como o this. no PHP
#sempre que mudar o propio obj usar o self
    def __init__(self,x,y):

        self.x = x
        self.y = y
        self.__alias="teste privado"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setY(self,y):
        self.y = y

    def setX(self,x):
        self.x = x

    def printAll(self):
        print('x  : ', self.x)
        print('y : ', self.y)
        print('alias : ', self.__alias)
    
#p = Point(1,2)         # Instantiate an object of type Point
#q = Point(6,5)         # and make a second point

#print(p.getY())
#print(p.getX())
#print(q)

#is compara o endereço de memoria do obj 
#print(p is q)