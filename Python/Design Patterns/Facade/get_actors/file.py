from abs_facade import AbsFacade
import os

class GetActorsFacade(AbsFacade):
    def __init__(self):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.source_file = "actors.txt"
        self.full_source_path = "{}/{}".format(self.current_path, self.source_file)

    def get_actors(self):
        with open(self.full_source_path, 'r') as reader:
            for line in reader:
                yield line
