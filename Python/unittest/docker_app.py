class Application:
    def get_next_person(self, user):
        person = self.get_random_person()
        while person in user['people_seen']:
            person = self.get_random_person()
        return person

    def get_random_person():
        pass
