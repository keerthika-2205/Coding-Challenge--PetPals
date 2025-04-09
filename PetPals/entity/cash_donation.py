from entity.donation import Donation

class CashDonation(Donation):
    def __init__(self, donor_name=None, amount=None, donation_date=None):
        super().__init__(donor_name, amount)
        self._donation_date = donation_date

    @property
    def donation_date(self):
        return self._donation_date

    @donation_date.setter
    def donation_date(self, value):
        self._donation_date = value

    def record_donation(self):
        return f"Cash donation recorded: {self._donor_name} donated ${self._amount} on {self._donation_date}"