from abc import ABC, abstractmethod

class Donation(ABC):
    def __init__(self, donor_name=None, amount=None):
        self._donor_name = donor_name
        self._amount = amount

    @property
    def donor_name(self):
        return self._donor_name

    @donor_name.setter
    def donor_name(self, value):
        self._donor_name = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @abstractmethod
    def record_donation(self):
        pass