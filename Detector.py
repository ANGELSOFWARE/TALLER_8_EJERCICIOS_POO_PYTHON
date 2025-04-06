import random 
class Detector:
    def __init__(self):
        self.mov1=True
        self.mov2=True
        self.mov3=True
        self.noche=True
    def detectar_datos(self):
        mov1=random.choice([True,False])
        mov2=random.choice([True,False])
        mov3=random.choice([True,False])
        noche=random.choice([True,False])
        return mov1,mov2,mov3,noche
