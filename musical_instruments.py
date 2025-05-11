from abc import ABC, abstractmethod
import random

# Abstract Base Class (Parent)
class Musical_Instrument(ABC):

    def __init__(self, name, type):
        self._name = name
        self._type = type
        
    @property
    def name(self):
        return self._name
    
    @property
    def type(self):
        return self._type
    
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def tune(self):
        pass

    @abstractmethod
    def description(self):
        pass
      

class Violin(Musical_Instrument):
    def __init__(self, name, instrument_type, brand):
        super().__init__(name, instrument_type)
        self.brand = brand
        self.bow_type = "standard"

    def play(self):
        print(f"{self.name} is playing a soft classical melody.")

    def tune(self):
        print(f"Tuning the strings of {self.name}")
     
    def description(self):
        return f"{self.name} is a beautiful {self.type} instrument by {self.brand}. It uses a {self.bow_type} bow."
        
    
    

class Guitar(Musical_Instrument):
    def __init__(self, name = "Marcin the Guitar", type = "null"):
        super().__init__(name, type)
    
    @property
    def name(self):
        return self._name
    
    @property
    def type(self):
        return self._type
    
    def play(self):
        if self._type == "acoustic":
            playstyles = ["a sweet country melody", "a mellow chord progression", "a warm, soft strum"]
            return f"{self.name} plays {random.choice(playstyles)}."
        elif self._type == "electric":
            playstyles = ["an out of this world riff", "a fiery, screaming solo", "a sizzling fingerslick"]
            return f"{self.name} shreds {random.choice(playstyles)}."

    def tune(self):
        if self._type == "acoustic":
            return f"{self.name} stays steadily as you tune its 6 strings."
        elif self._type == "electric":
            return f"{self.name} flails everywhere as you tune its 6 strings."
    
    def description(self):
        if self._type == "acoustic":
            return f"{self.name} sings with a warm tone. \"Hello, I am Marcin the Guitar\""
        elif self._type == "electric":
            return f"{self.name} screams with a deafening tone. \"Sup lads! The name's Marcin\""
        
# Menu
def menu():
    print("\n Welcome to the Instrument Universe")
    print("1. Marcin (Guitar)")
    print("2. Exit")

def interact(instrument):
    while True:
        interaction = input("How would you like to interact (Introduce/Play/Tune/Stop): ").lower()
        if interaction == "introduce":
            print(f"{instrument.description()}\n")
        elif interaction == "play":
            print(f"{instrument.play()}\n")
        elif interaction == "tune":
            print(f"{instrument.tune()}\n")
        elif interaction == "stop":
            print(f"You've stopped interacting with {instrument.name}\n")
            break
        else:
            print("Invalid choice! Please try again.\n")

def choose_guitar_personality():
    while True:
        guitar_type = input("Choose Marcin's Personality (Acoustic/Electric): ").lower()
        if guitar_type in ["acoustic", "electric"]:
            return guitar_type
        else:
            print("Invalid choice. Please choose either Acoustic or Electric.")

def actions():
    while True:
        menu()
        choice = input("Choose your instrument: ")
        if choice == "1":
            guitar_type = choose_guitar_personality()
            guitar = Guitar("Marcin the Guitar", guitar_type)
            interact(guitar)
        elif choice == "2":
            print("Thanks for jamming with us! Come back anytime.")
            break
        else:
            print("Oops! That was an invalid choice. Please try again!")


if __name__ == "__main__":
    actions()
    
    



