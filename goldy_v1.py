import random
import time
class pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 15
        self.energy = 100
    def display(self):
        print(f"{self.name}'s status: ")
        print(f"humger {self.hunger}/100: ")
        print(f"happiness {self.happiness}/100: ")
        print(f"Energy {self.energy}/100: ")
    
    def feed(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 20)
            self.happiness = min(100, self.happiness + 10)
            print(f"You feed {self.name} yum!..")
        else:
            print(f"{self.name} is not hungry right now.")    
    
    def play(self):
        if self.energy > 0:
            self.energy -= 20
            self.happiness = min(100, self.happiness + 20)
            self.hunger = min(100, self.hunger + 10)
            print(f"You played with {self.name} hurrah!..")
        else:
            print(f"{self.name} is too tierd to play")
            
    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.hunger += 5
        print(f"{self.name} is sleeping... ZZzzzzz....!")
        time.sleep(2)
        print(f"{self.name} felling freshed ready to play...")
        
    def update(self):
        self.hunger = min(100, self.hunger + 5)
        self.happiness = max(0, self.happiness - 3)
        self.energy = max(0, self.energy - 3)
        
def main():
    pet_name = input("name your pet : ")
    my_pet = pet(pet_name)
    
    print(f"Wlcm to virtual pet simulator{pet_name}")
    while True:
        my_pet.update()
        
        my_pet.display()
        
        
        action = input("What do you want to do:(play.. feed.. sleep.. quit..)").lower()
        if action == "feed":
            my_pet.feed()
            
        elif action == "play":
            my_pet.play()
        elif action == "sleep":
            my_pet.sleep()
        elif action == "quit":
            print("Good byy see you later.....")
            break   
        else:
            print("Invalid action!..")
if __name__ == "__main__":
    main()