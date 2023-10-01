
class Multiplicando():    
    def __init__(self, value1, value2):
        self.value3 = value1 * value2
    
    def __str__(self) -> str:
        return (f"{self.value3}")
    

class Somando():
    def __init__(self, value1, value2):
        self.value3 = value1 + value2
    
    def __str__(self) -> str:
        return (f"{self.value3}")
    

class Subtrair():
    def __init__(self, value1, value2):
        self.value3 = value1 - value2
    
    def __str__(self) -> str:
        return (f"{self.value3}")
    
class Dividindo():
    def __init__(self, value1, value2):
        self.value3 = value2 / value1
    
    def __str__(self) -> str:
        return (f"{self.value3}")