

def singleton(cls):
    instance = None
    def wrapper(*args,**kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args,**kwargs)
        return instance
    
    return wrapper

@singleton
class RectangleDeco:

    __slots__ = ('__longueur','__largeur')

    def __init__(self,longueur:int=1,largeur:int=1) -> None:
        if longueur>0 and largeur>0:
            self.longueur = longueur
            self.largeur = largeur

    
    @classmethod
    def build_from_str(cls,line):            
        # a = line.split(';') # ["12","5"]
        lng,lrg = [int(i) for i in line.split(';')] # [12,5]
        r = cls(lng,lrg) # RectangleDeco(lng,lrg)
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