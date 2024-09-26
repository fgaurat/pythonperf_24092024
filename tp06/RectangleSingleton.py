


class RectangleSingleton:

    __slots__ = ('__longueur','__largeur')
    __cpt = 0


    instance = None


    def __new__(cls,*args,**kwargs): 
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self,longueur:int=1,largeur:int=1) -> None:
        if longueur>0 and largeur>0:
            self.longueur = longueur
            self.largeur = largeur
            RectangleSingleton.__cpt +=1

    
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
    
    @staticmethod
    def get_cpt():
        return RectangleSingleton.__cpt

    def __del__(self):
        print("def __del__(self)")
        RectangleSingleton.__cpt-=1

    # longueur = property(get_longueur,set_longueur,doc="La longueur")
    # largeur = property(get_largeur,set_largeur,doc="La largeur")