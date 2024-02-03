import random


class Kitten:
    def __init__(self, name):
        self.name = name
        self.mood = 50
        self.energy = 50
        self.hunger = 25
        self.alive = True

    def to_eat(self):
        print(f"{self.name} is eating")
        self.hunger += 6
        self.energy -= 1

    def to_sleep(self):
        print(f"{self.name} is sleeping")
        self.mood += 2
        self.hunger -= 5
        self.energy += 7

    def to_play(self):
        print(f"{self.name} is playing")
        self.mood += 5
        self.hunger -= 7
        self.energy -= 4

    def kitten_alive(self):
        if self.mood <= 0:
            print(f"{self.name} got bored. Game over")
            self.alive = False
        elif self.energy <= 0:
            print(f"{self.name} is so tired. Game over")
            self.alive = False
        elif self.hunger <= 0:
            print(f"{self.name} is too hungry. Game over")
            self.alive = False
        elif i == 365:
            print(f"Congratulations! {self.name} made it!")
            self.alive = False


    def day_end(self):
        print(" ")
        print(f"{self.name}'s statistics")
        print(" ")
        print(f"Mood = {self.mood}")
        print(f"Energy = {self.energy}")
        print(f"Hunger = {self.hunger}")

    def live(self, day):
        d = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:—^80}")
        if self.hunger <= 30:
            self.to_eat()
        elif self.hunger < 100:
            self.hunger = 100
        else:
            random_cube = random.randint(1, 2)
            if random_cube == 1:
                self.to_play()
            else:
                self.to_sleep()
        self.day_end()
        self.kitten_alive()


name = input("Input you kitten's name please: ")
kitten = Kitten(name=name)
for i in range(1, 366):
    if kitten.alive == False:
        break
    kitten.live(i)
