from abc import ABC, abstractmethod


class Optimizer(ABC):
    '''
    Abstract base class of setting out template for optimizer classes.
    '''
    def __init__(self, name: str=None, max_iter: int=300, min_gn: float=1e-6):
        if name is None:
            self._name = 'Optimizer'
        else:
            self._name = name
        self.max_iter = max_iter
        self.min_gn = min_gn

    def __str__(self):
        return self._name

    @abstractmethod
    def solve(self):
        ...

    def stop(self, n_iter: int, gn: float) -> bool:        
        if self.min_gn > gn:
            return True
        if self.max_iter <= n_iter:
            return True
        return False
