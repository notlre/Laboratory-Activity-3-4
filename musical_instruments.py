from abc import ABC, abstractmethod

# Abstract Base Class (Parent)
class Musical_Instrument:
    def __init__(self, name, instrument_type, brand):
        self.name = name
        self.instrument_type = instrument_type
        self.brand = brand

    @abstractmethod
    def play_sound(self):
        pass
    @abstractmethod
    def tune(self):
        pass

# Child Class
class Guitar(Musical_Instrument):
    
    def play_sound(self):
        print(f"{self.name} is strumming nonchalantly.")
    
    def tune(self):
        print(f"Tuning {self.name}")
    
guitar = Guitar("Electric Guitar", "String", "Yamaha")

guitar.play_sound()

guitar.tune()

# Child Class
class Piano(Musical_Instrument):
    
    def play_sound(self):
        print(f"{self.name} is playing a melodious tune.")
    
    def tune(self):
        print(f"Tuning {self.name}")

#Child Class
class Violin(Musical_Instrument):
    def __init__(self, name, instrument_type, brand):
        super().__init__(name, instrument_type, brand)
        self.bow_type = "Standard"

    def play_sound(self):
        print(f"{self.name} is playing a soft classical melody.")

    def tune(self):
        print(f"Tuning the strings of {self.name}")
        
violin = Violin("Acoustic Violin", "String", "Stentor")

violin.play_sound()

violin.tune()


