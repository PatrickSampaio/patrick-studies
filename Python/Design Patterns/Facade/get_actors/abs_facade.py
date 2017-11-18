import abc

class AbsFacade(metaclass=abc.ABCMeta):
     @abc.abstractmethod
     def get_actors(self):
         pass

     @abc.abstractproperty
     def query_executor(self):
         pass
