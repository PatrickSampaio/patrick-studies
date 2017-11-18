import sys
import os
from get_actors.abs_facade import AbsFacade

class FacadeFactory(object):
     @staticmethod
     def create_facade(module_name):
         import pdb; pdb.set_trace()
         sys.path.append(os.path.dirname(os.path.abspath(__file__)))
         source_module = __import__(module_name)

         GetterActors = source_module.GetActorsFacade
         #if isclass(GetterActors) and not isabstract(GetterActors) and issubclass(GetterActors, AbsFacade):
         return GetterActors()
         #return "Sorry we could not find a source for the data"
