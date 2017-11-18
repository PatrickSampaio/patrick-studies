from get_actors import SOURCE
from get_actors.facade_factory import FacadeFactory

def main():
    facade = FacadeFactory.create_facade(SOURCE)
    for actor in facade.get_actors():
        print(actor)

if __name__ == '__main__':
    main()
