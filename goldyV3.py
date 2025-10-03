import time
class pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happines = 20
        self.energy = 30
    
    def display(self):
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Energy: {self.energy}/100")
        
    def feed(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 10)
            self.happiness = min(100, self.happiness + 14)
            print(f"You fed {self.name}.. Wow...")
        else:
            print(f"{self.name} is not hungry right now..")
            
    def play(self):
        if self.energy > 0:
            self.energy -= 20
            self.hungry = max(0, self.hungry -17)
            self.happiness = min(100, self.happiness + 20)
            print(f"You played with{self.name}... Hurrrah....!")
        else:
            print(f"{self.name} is too tierd to play..")
            
    def sleep(self):
        self.hunger += 5
        self.energy =  max(0, self.energy + 20)
        print(f"{self.name} is sleeping....ZZzz...")            
        time.sleep(2)
        print(f"{self.name} is ready to play...")
        
    def update(self):
        self.hunger = max(0, self.hunger - 4)
        self.happiness = min(100, self.happiness + 6)
        self.energy = min(100, self.energy + 9)
    
def main():
    pet_name = input("Enter your pet name: ")
    my_pet = pet(pet_name)                         
    
    print(f"welcome to the simple simulator here is your {my_pet.name}")
    while True:
        my_pet.update()
        
        my_pet.status()
        
        action = input("What do you want to do with your pet?").lower()
        if action == "feed":
            my_pet.feed()
        elif action == "play":
            my_pet.play()
        elif action == "sleep":
            my_pet.sleep()
        elif action == "quit":
            print("Thanku for playing, see ya..")
            break
        else:
           print("Invalid action!..")
if __name__ == "__main__":
    main()
           