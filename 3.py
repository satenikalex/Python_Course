class Person:
    def __init__(self, name, likes, hates):
        self.name = name
        self.likes = likes
        self.hates = hates
    
    def taste(self, food):
        result = f"{self.name} eats the {food}"
        
        if food in self.likes:
            result += " and loves it!"
        elif food in self.hates:
            result += " and hates it!"
        else:
            result += "!"
        
        return result