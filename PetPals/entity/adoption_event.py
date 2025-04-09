from entity.iadoptable import IAdoptable

class AdoptionEvent:
    def __init__(self):
        self._participants = []

    def register_participant(self, participant: IAdoptable):
        self._participants.append(participant)

    def host_event(self):
        for participant in self._participants:
            participant.adopt()
        return "Adoption event hosted successfully!"
    