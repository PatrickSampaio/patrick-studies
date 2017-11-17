from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

some_engine = create_engine('postgresql://postgres@localhost/dvdrental')

def get_actors():
    query = "select * from actor"
    for actor in some_engine.execute(query):
        print(actor)

get_actors()
