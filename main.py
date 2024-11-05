class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.intelligence = 5 
        self.weight = 1 
        self.energy = 5 

    def play(self):
        print(f"{self.name} is playing...")
        self.weight -= 0.01
        self.energy -= 1

    def eat(self):
        print(f"{self.name} is eating...")
        self.weight += 0.5
        self.energy += 2
        self.intelligence -= 0.1

    def sleep(self):
        print(f"{self.name} is eating...")
        self.energy += 5

    def show_stats(self):
        print(f"""Cat Stats:
Intelligence: {self.intelligence} 
Weight: {self.weight}       
Energy: {self.energy}         
""")