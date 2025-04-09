from abc import ABC, abstractmethod
from entity.pet import Pet
from entity.donation import Donation

class IPetRepository(ABC):
    @abstractmethod
    def add_pet(self, pet: Pet) -> bool:
        pass

    @abstractmethod
    def list_pets(self) -> list:
        pass

    @abstractmethod
    def record_donation(self, donation: Donation) -> bool:
        pass

    @abstractmethod
    def register_event_participant(self, event_id: int, participant_type: str) -> bool:
        pass