import mysql.connector
from dao.ipet_repository import IPetRepository
from entity.pet import Pet
from entity.dog import Dog
from entity.cat import Cat  # Also needed for Cat check
from entity.cash_donation import CashDonation
from entity.donation import Donation
from entity.item_donation import ItemDonation
from util.db_conn_util import DBConnUtil

class PetRepositoryImpl(IPetRepository):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def add_pet(self, pet: Pet) -> bool:
        cursor = self.connection.cursor()
        if isinstance(pet, Dog):
            query = "INSERT INTO Pets (name, age, breed, type, dog_breed) VALUES (%s, %s, %s, 'Dog', %s)"
            cursor.execute(query, (pet.name, pet.age, pet.breed, pet.dog_breed))
        elif isinstance(pet, Cat):
            query = "INSERT INTO Pets (name, age, breed, type, cat_color) VALUES (%s, %s, %s, 'Cat', %s)"
            cursor.execute(query, (pet.name, pet.age, pet.breed, pet.cat_color))
        self.connection.commit()
        return True

    def list_pets(self) -> list:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Pets")
        rows = cursor.fetchall()
        pets = []
        for row in rows:
            if row[4] == 'Dog':
                pet = Dog(row[1], row[2], row[3], row[5])
            elif row[4] == 'Cat':
                pet = Cat(row[1], row[2], row[3], row[6])
            pet.pet_id = row[0]
            pets.append(pet)
        return pets

    def record_donation(self, donation: Donation) -> bool:
        cursor = self.connection.cursor()
        if isinstance(donation, CashDonation):
            query = "INSERT INTO Donations (donor_name, amount, donation_type, donation_date) VALUES (%s, %s, 'Cash', %s)"
            cursor.execute(query, (donation.donor_name, donation.amount, donation.donation_date))
        elif isinstance(donation, ItemDonation):
            query = "INSERT INTO Donations (donor_name, amount, donation_type, item_type) VALUES (%s, %s, 'Item', %s)"
            cursor.execute(query, (donation.donor_name, donation.amount, donation.item_type))
        self.connection.commit()
        return True

    def register_event_participant(self, event_id: int, participant_type: str) -> bool:
        cursor = self.connection.cursor()
        query = "INSERT INTO Participants (event_id, participant_type) VALUES (%s, %s)"
        cursor.execute(query, (event_id, participant_type))
        self.connection.commit()
        return True