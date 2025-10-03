# import random
# import time
# from colorama import init, Fore, Back, Style
# init()

# class Pet:
#     def __init__(self, name):
#         self.name = name
#         self.hunger = 0
#         self.happiness = 50
#         self.energy = 100

#     def display_status(self):
#         print(f"{Fore.GREEN}{self.name}'s Status:")
#         print(f"Hunger: {self.hunger}/100")
#         print(f"Happiness: {self.happiness}/100")
#         print(f"Energy: {self.energy}/100{Style.RESET_ALL}")

#     def feed(self):
#         if self.hunger > 0:
#             self.hunger = max(0, self.hunger - 20)
#             self.happiness = min(100, self.happiness + 10)
#             print(f"{Fore.YELLOW}You fed {self.name}. Yum!{Style.RESET_ALL}")
#         else:
#             print(f"{Fore.YELLOW}{self.name} isn't hungry right now.{Style.RESET_ALL}")

#     def play(self):
#         if self.energy > 0:
#             self.energy -= 20
#             self.happiness = min(100, self.happiness + 15)
#             self.hunger = min(100, self.hunger + 10)
#             print(f"{Fore.CYAN}You played with {self.name}. Fun!{Style.RESET_ALL}")
#         else:
#             print(f"{Fore.CYAN}{self.name} is too tired to play.{Style.RESET_ALL}")

#     def sleep(self):
#         self.energy = min(100, self.energy + 30)
#         self.hunger += 5
#         print(f"{Fore.BLUE}{self.name} is sleeping... Zzz...{Style.RESET_ALL}")
#         time.sleep(3)
#         print(f"{Fore.BLUE}{self.name} woke up feeling refreshed!{Style.RESET_ALL}")

#     def update(self):
#         self.hunger = min(100, self.hunger + 5)
#         self.happiness = max(0, self.happiness - 3)
#         self.energy = max(0, self.energy - 3)

# def main():
#     pet_name = input("Name your pet: ")
#     my_pet = Pet(pet_name)

#     print(f"Welcome to Virtual Pet Simulator! Meet {pet_name}!")
#     while True:
#         my_pet.update()
        
#         my_pet.display_status()

#         action = input("What do you want to do? (feed/play/sleep/quit): ").lower()
#         if action == 'feed':
#             my_pet.feed()
#         elif action == 'play':
#             my_pet.play()
#         elif action == 'sleep':
#             my_pet.sleep()
#         elif action == 'quit':
#             print(f"Goodbye! {my_pet.name} will miss you!")
#             break
#         else:
#             print("Invalid action. Try again.")

# if __name__ == "__main__":
#     main()
    

import time
class pet:
    def __init__(self,name):
        self.name = name
        self.hunger = 0
        self.energy = 100
        self.happiness = 50
    
    def display_status(self):
        print(f"{self.name} status:")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Energy: {self.energy}/100 ")
        
    def feed(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger-10)
            self.happiness = min(0, self.happiness +12)
            print(f"You fed: {self.name} yum....!")
        else:
            print(f" {self.name} is not hungry..")
            
    def play(self):
        if self.energy> 0:
            self.energy -=14
            self.hunger = min(100, self.hunger +13)
            self.happiness = min(100, self.happiness +14)
            print(f"You played with {self.name} hurrah!..")
        else:
            print(f"{self.name} is tierd he need some sleep...")
            
    def sleep(self):
        self.energy = min(100, self.energy +17)
        self.happiness +=14
        print(f"{self.name}is sleeping..ZZzz...")
        time.sleep(3)
        print(f"{self.name} is woke up and filling refresed...")
        
    def update(self):
        self.happiness = max(0, self.happiness - 4)
        self.energy = min(100, self.energy - 3)
        self.hunger = min(100, self.hunger + 7)
        
def main():
    pet_name = input("Enter the name of your pet: ")
    my_pet = pet(pet_name)
    print(f"Welcome to pet Simpulaotor! meet {pet_name}")
    while True:
        my_pet.update()
        
        my_pet.display_status()
        action = input("what do you want to do ? (play/ feed/ sleep / quit): ").lower()
        if action == "feed":
            my_pet.feed()
        elif action == "play":
            my_pet.play()
        elif action == "sleep":
            my_pet.sleep()
        elif action == "quit":
            print(f"good byy {my_pet} will see you soon..")
            break
        else:
            print("invlaid choice please choose correct option..")
            
if __name__ == "__main__":
    main()
            
            