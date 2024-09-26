
from typing import Any


class Singleton(type):
    instance = None


    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = super().__call__(*args,**kwargs)
        else:
            self.instance.__init__(*args,**kwargs)
        
        return self.instance
        

class RectangleMetaSingleton(metaclass=Singleton):

    __slots__ = ('__longueur','__largeur')

    def __init__(self,longueur:int=1,largeur:int=1) -> None:
        if longueur>0 and largeur>0:
            self.longueur = longueur
            self.largeur = largeur

    
    @classmethod
    def build_from_str(cls,line):            
        # a = line.split(';') # ["12","5"]
        lng,lrg = [int(i) for i in line.split(';')] # [12,5]
        r = cls(lng,lrg) # Rectangle(lng,lrg)
        return r
    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur

    @longueur.setter
    def longueur(self,l):
        if l<=0:
            raise Exception('Hooooo! la longueur')
        self.__longueur = l
    
    @largeur.setter
    def largeur(self,l):
        if l<=0:
            raise Exception('Hooooo! la largeur')
        self.__largeur = l

    @property
    def surface(self):
        return self.__longueur*self.__largeur
    
    def __str__(self) -> str:
        return f"{__class__} {self.__longueur=}, {self.__largeur=}"

    def __eq__(self, value: object) -> bool:
        return self.__longueur == value.__longueur and self.__largeur == value.__largeur
    

    def __del__(self):
        print("def __del__(self)")

    # longueur = property(get_longueur,set_longueur,doc="La longueur")
    # largeur = property(get_largeur,set_largeur,doc="La largeur")