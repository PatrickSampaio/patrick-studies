from TaxesReturns import TaxesReturns
from GoodAsGoldTaxes import GoodAsGoldTaxes

class AdapterGoodAsGoldTaxes(GoodAsGoldTaxes, TaxesReturns):
    def __init__(GoodAsGoldTax):
        self.total_outcome = calculate_total_outcome(GoodAsGoldTaxes.total_outcome)
        self.total_income = calculate_total_income(GoodAsGoldTaxes.total_income)

    @property
    def is_fake_tax_return():
        return False

    @propety
    def balance(self):
        return self.balance

    @property
    def total_income(self):
        return self.total_income

    @property
    def total_outcome(self):
        return self.total_outcome
