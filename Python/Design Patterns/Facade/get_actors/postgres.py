from sqlalchemy import create_engine
from .abs_facade import AbsFacade
from . import PROVIDER

some_engine = create_engine(PROVIDER)

class GetActorsFacade(AbsFacade):    
    def __init__(self):
        self.query_executor = some_engine
 
    def get_actors(self):
        from .import QUERY
        for actor in some_engine.execute(QUERY):
           yield actor
