class Alien:
    
    numberOfAliens = 0
    numberAtThatPoint = 0
    
    def __init__(self, name):
        self.name = name
        self.numberAtThatPoint +=1
        Alien.numberAtThatPoint += 1
        Alien.numberOfAliens += 1
        
    def getNumberOfAliens(self):
        return f"The total number of aliens in this class is {self.numberOfAliens}"
    
    def __str__(self):
        return f"Alien name : {self.name} {self.numberAtThatPoint}"
    
listAliens = []  

for item in range(10):
    listAliens.append(Alien(str(item +1)))
    
    
print(listAliens[0].getNumberOfAliens())
