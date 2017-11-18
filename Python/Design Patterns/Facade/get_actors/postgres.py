from sqlalchemy import create_engine
from abs_facade import AbsFacade
from get_actors import PROVIDER

some_engine = create_engine(PROVIDER)

class GetActorsFacade(AbsFacade):    
    def __init__(self):
        self.set_query_executor(some_engine)
 
    def get_actors(self):
        from get_actors import QUERY
        for actor in some_engine.execute(QUERY):
           yield actor

    @property
    def query_executor(self):
        return self._query_executor

    def set_query_executor(self, query_executor):
        self._query_executor = query_executor
