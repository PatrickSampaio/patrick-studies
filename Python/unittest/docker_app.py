class Application:
    def get_next_person(self, user):
        person = self.get_random_person()
        while person in user['people_seen']:
            person = self.get_random_person()
        return person

    def get_random_person():
        pass

    def evaluate(self, person1, person2):
        if person1['name'] in person2['likes']:
            self.send_email(person1['name'])
            self.send_email(person2['name'])
        elif person1['name'] in person2['dislikes']:
            self.let_down_gently(person1['name'])
        elif person1['name'] not in person2['likes'] and person1.name not in person2['dislikes']:
            self.give_it_a_time(person1['name'])

    @classmethod
    def give_it_a_time(cls, person):
        pass

    @classmethod
    def let_down_gently(cls,person):
        pass
 
    @classmethod
    def send_email(cls, person):
        pass
