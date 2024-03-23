
#Watto needs a new system for organizing his inventory of podracers. 
#Help him do this by implementing an Object Oriented solution according to the following criteria.

#First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 

class Podracer:
    def _init_(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

#Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        print(f"My podracer is now {self.condition}.")
        self.condition = "repaired"


    
#Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod:
    def _init_(self, max_speed, condition, price):
        super()._init_(max_speed, condition, price)

    def boost(self):
        print(f"My podracer's max speed is now {self.max_speed}.")
        self.max_speed *= 2


#Define another class that inherits Podracer and call this one SebulbasPod. 
#This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod:
    def _init_(self, max_speed, condition, price):
        super()._init_(max_speed, condition, price)

    def flame_jet(self, podracer):
        print(f"My podracer's new condition is now: {podracer.condition}.")
        podracer.condition = "trashed"

