from dao.pet_repository_impl import PetRepositoryImpl
from entity.dog import Dog
from entity.cat import Cat
from entity.cash_donation import CashDonation
from entity.item_donation import ItemDonation
from exception.exceptions import *
from entity.pet_shelter import PetShelter

class MainModule:
    def __init__(self):
        self.repo = PetRepositoryImpl()
        self.shelter = PetShelter()

    def menu(self):
        while True:
            print("\n=== PetPals: The Pet Adoption Platform ===")
            print("1. Add Pet")
            print("2. List Available Pets")
            print("3. Record Cash Donation")
            print("4. Record Item Donation")
            print("5. Register for Adoption Event")
            print("6. Exit")
            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    name = input("Enter pet name: ")
                    age = int(input("Enter pet age: "))
                    if age <= 0:
                        raise InvalidPetAgeException("Pet age must be positive")
                    breed = input("Enter pet breed: ")
                    pet_type = input("Enter pet type (Dog/Cat): ").lower()
                    if pet_type == "dog":
                        dog_breed = input("Enter dog breed: ")
                        pet = Dog(name, age, breed, dog_breed)
                    elif pet_type == "cat":
                        cat_color = input("Enter cat color: ")
                        pet = Cat(name, age, breed, cat_color)
                    else:
                        raise AdoptionException("Invalid pet type")
                    self.repo.add_pet(pet)
                    self.shelter.add_pet(pet)
                    print("Pet added successfully!")

                elif choice == "2":
                    pets = self.repo.list_pets()
                    if not pets:
                        raise NullReferenceException("No pets available")
                    for pet in pets:
                        print(pet)

                elif choice == "3":
                    donor_name = input("Enter donor name: ")
                    amount = float(input("Enter donation amount: "))
                    if amount < 10:
                        raise InsufficientFundsException("Donation amount must be at least $10")
                    donation_date = input("Enter donation date (YYYY-MM-DD): ")
                    donation = CashDonation(donor_name, amount, donation_date)
                    self.repo.record_donation(donation)
                    print(donation.record_donation())

                elif choice == "4":
                    donor_name = input("Enter donor name: ")
                    amount = float(input("Enter donation value: "))
                    item_type = input("Enter item type: ")
                    donation = ItemDonation(donor_name, amount, item_type)
                    self.repo.record_donation(donation)
                    print(donation.record_donation())

                elif choice == "5":
                    event_id = int(input("Enter event ID: "))
                    self.repo.register_event_participant(event_id, "Shelter")
                    print("Registered for adoption event!")

                elif choice == "6":
                    print("Exiting...")
                    break

                else:
                    print("Invalid choice!")

            except InvalidPetAgeException as e:
                print(f"Error: {e}")
            except NullReferenceException as e:
                print(f"Error: {e}")
            except InsufficientFundsException as e:
                print(f"Error: {e}")
            except AdoptionException as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = MainModule()
    app.menu()