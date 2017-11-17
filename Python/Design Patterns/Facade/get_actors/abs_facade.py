import abc

class AbsFacade(metaclass=abc.ABCMeta):
     @abc.abstractmethod
     def get_employees(self):
         pass

     @abc.abstractproperty
     def query_executor(self):
         pass
