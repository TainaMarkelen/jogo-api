from dataclasses import dataclass

@dataclass
class FightRequest:
    
    name1: str
    name2: str
    
    def __str__(self):
        return (self.name1, self.name2)
        