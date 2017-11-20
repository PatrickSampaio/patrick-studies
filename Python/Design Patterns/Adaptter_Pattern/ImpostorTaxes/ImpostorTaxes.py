class ImpostorTaxes(object):
    def __init__(self, fake_first_name, fake_last_name, fake_income_and_outcome):
        self.first_name = fake_first_name
        self.last_name = fake_last_name
        self.income_and_outcome = fake_income_and_outcome

    @property
    def is_an_fake_taxe(self):
        return True
