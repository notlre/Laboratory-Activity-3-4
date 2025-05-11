from abc import ABC, abstractmethod
import random
import os

# Abstract Base Class
class Musical_Instrument(ABC):
    def __init__(self, name, instrument_type, brand="Unknown"):
        self._name = name
        self._instrument_type = instrument_type
        self.brand = brand
        
    @property
    def name(self):
        return self._name

    @property
    def instrument_type(self):
        return self._instrument_type

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
        super().__init__(name, "chordophone", brand)
        
    def play(self):
        styles = ["a melancholic solo", "a vibrant concerto", "a gentle lullaby"]
        return f"{self.name} plays {random.choice(styles)} on the bow."

    def tune(self):
        return f"{self.name} is carefully tuned string by string with precision."

    def description(self):
        return f"I'm {self.name}! A violin by {self.brand} from {self.instrument_type} group!"


class Flute(Musical_Instrument):
    def __init__(self, name, instrument_type='woodwind', material="silver", key="C"):
        super().__init__(name, instrument_type)
        self.material = material
        self.key = key


    def play(self):
        styles = ["a bright and cheerful tune", "a dreamy note run", "a delicate trill"]
        return f"{self.name} plays {random.choice(styles)} in the key of {self.key}."

    def tune(self):
        return f"{self.name} is being aligned and adjusted for pitch accuracy."

    def description(self):
        return f"Wasuppp! I'm {self.name}, a {self.material} flute in the key of {self.key}, from the {self.instrument_type} group! Nice to meet ya!"


class Guitar(Musical_Instrument):
    def __init__(self, name="Marcin the Guitar", instrument_type="chordophone", type="null", brand="Generic"):
        super().__init__(name, instrument_type, brand)
        self._type = type

    @staticmethod
    def choose_guitar_personality():
        while True:
            guitar_type = input("Choose Marcin's Personality (Acoustic/Electric): ").lower()
            if guitar_type in ["acoustic", "electric"]:
                return guitar_type
            else:
                print("❗ Invalid choice. Please choose either Acoustic or Electric.")

    def play(self):
        if self._type == "acoustic":
            playstyles = ["a sweet country melody", "a mellow chord progression", "a warm, soft strum"]
            return f"{self.name} plays {random.choice(playstyles)}."
        elif self._type == "electric":
            playstyles = ["an out of this world riff", "a fiery, screaming solo", "a sizzling fingerslick"]
            return f"{self.name} shreds {random.choice(playstyles)}."
        else:
            return f"{self.name} strums something unusual."

    def tune(self):
        if self._type == "acoustic":
            return f"{self.name} stays steadily as you tune its 6 strings."
        elif self._type == "electric":
            return f"{self.name} flails everywhere as you tune its 6 strings."
        else:
            return f"{self.name} makes weird noises as you tune it."

    def description(self):
        if self._type == "acoustic":
            return f"{self.name} sings with a warm tone. \"Hello, I am Marcin the Guitar! From the {self.instrument_type} group!\""
        elif self._type == "electric":
            return f"{self.name} screams with a deafening tone. \"Sup lads! The name's Marcin! From the {self.instrument_type} group!\""
        else:
            return f"{self.name} seems confused about its personality."


class Ukulele(Musical_Instrument):
    def __init__(self, name, instrument_type="chordophone", brand="Generic", size="soprano", origin="Hawaii"):
        super().__init__(name, instrument_type, brand)
        self.size = size
        self.origin = origin
        self.moods = ["sunny", "bubbly", "laid-back", "playful"]

    def play(self):
        melodies = [
            "a tropical island melody",
            "a fun strumming pattern",
            "a happy-go-lucky tune",
            "a soft lullaby that makes you smile"
        ]
        return f"{self.name} strums {random.choice(melodies)} with a {random.choice(self.moods)} vibe."

    def tune(self):
        tuning_styles = [
            "G-C-E-A tuning for a classic sound",
            "low-G tuning for deeper vibes",
            "a quirky half-step up"
        ]
        return f"{self.name} is being tuned to {random.choice(tuning_styles)}."

    def description(self):
        return (
            f"Halloo! I'm {self.name}, a {self.size} ukulele from {self.origin}, "
            f"crafted by {self.brand}. I'm part of the {self.instrument_type} group!"
        )

    

#Menu System
def menu():
    print("\n🎶 Welcome to the Instrument Universe 🎶")
    print("1. Marcin (Guitar)")
    print("2. Violin")
    print("3. Flute")
    print("4. Ukulele")
    print("5. Exit")
    


def interact(instrument):
    while True:
        interaction = input("🎵 How would you like to interact (Introduce/Play/Tune/Stop): ").lower()
        if interaction == "introduce":
            print(f"\n{instrument.description()}\n")
        elif interaction == "play":
            print(f"\n{instrument.play()}\n")
        elif interaction == "tune":
            print(f"\n{instrument.tune()}\n")
        elif interaction == "stop":
            print(f"\nYou’ve stopped interacting with {instrument.name}.\n")
            break
        else:
            print("Invalid choice! Please try again.\n")


def create_violin():
    name = input("Enter a name for your Violin: ")
    brand = input("Enter the Violin's brand: ")
    return Violin(name, "string", brand)


def create_flute():
    name = input("Enter a name for your Flute: ")
    material = input("Enter the Flute's material (default: silver): ") or "silver"
    key = input("Enter the key of the Flute (default: C): ") or "C"
    return Flute(name, "woodwind", material, key)

def create_ukulele():
    name = input("Enter a name for your Ukulele: ")
    size = input("Enter the Ukulele's size (default: soprano): ") or "soprano"
    brand = input("Enter the Ukulele's brand (default: Generic): ") or "Generic"
    origin = input("Where is your Ukulele from? (default: Hawaii): ") or "Hawaii"
    return Ukulele(name, brand=brand, size=size, origin=origin)

def main():
    while True:
        menu()
        choice = input("🎼 Choose your instrument: ")
        if choice == "1":
            guitar_type = Guitar.choose_guitar_personality()
            guitar = Guitar("Marcin the Guitar", "chordophone", guitar_type)
            interact(guitar)
        elif choice == "2":
            violin = create_violin()
            interact(violin)
        elif choice == "3":
            flute = create_flute()
            interact(flute)
        elif choice == "4":
            ukulele = create_ukulele()
            interact(ukulele)
        elif choice == "5":
            print("Thanks for jamming with us! Come back anytime.")
            break
        else:
            print("Oops! That was an invalid choice. Please try again!")

        clear()

    

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
