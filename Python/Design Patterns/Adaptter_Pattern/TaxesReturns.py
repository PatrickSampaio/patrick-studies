import abc

class TaxesReturns(metaclass=abc.ABCMeta):

    @abc.abstractproperty
    def is_fake_tax_return(self):
        return self.tax_type

    @abc.abstractproperty
    def total_income(self):
        return self.total_income

    @abc.abstractproperty
    def total_outcome(self):
        return self.total_outcome

    @abc.abstractproperty
    def balance(self):
        return self.total_income - self.total_outcome
