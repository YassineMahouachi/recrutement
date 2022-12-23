class Candiat:
    def __init__(self, cin:str, np:str, age:str, tel:str, xp:str, sexe:str, diplome:str) -> None:
        self.cin = cin
        self.np = np
        self.age = age
        self.tel = tel
        self.xp = xp
        self.sexe = sexe
        self.diplome = diplome

    def __repr__(self) -> str:
        return f"Candiat({self.cin} ** {self.np} ** {self.tel})"