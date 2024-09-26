from abc import ABC,ABCMeta,abstractmethod



class CalcGeo(metaclass=ABCMeta):


    # def surface(self):
        # raise NotImplementedError('Hooooo! La surface')
    
    @property
    @abstractmethod
    def surface(self):
        pass