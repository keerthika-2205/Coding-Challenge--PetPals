from entity.donation import Donation

class ItemDonation(Donation):
    def __init__(self, donor_name=None, amount=None, item_type=None):
        super().__init__(donor_name, amount)
        self._item_type = item_type

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value

    def record_donation(self):
        return f"Item donation recorded: {self._donor_name} donated {self._item_type} worth ${self._amount}"