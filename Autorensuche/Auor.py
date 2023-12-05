import RandomListGenerator
import random

def search(listeVonAutoren, nachname):
    for index in range(0,len(listeVonAutoren)):
        kandidat = nachname[index]
        if kandidat == nachname:
            print(f"gefunden in der Kiste nr {index}")
            break
        print("nicht gefunden")

def GenerateRandomAutor():
    groesse = 100
    random_Autor = random.randint(1,groesse)
    for i in groesse:
        random_Autor.append(RandomListGenerator.generate_random_autor(i))
    return random_Autor

class Autor:
    def __init__(self, name, vname, lfdnr):
        self.name = name
        self.vname = vname
        self.lfdnr = lfdnr

    def get_name(self):
        return self.name

    def get_vorname(self):
        return self.vorname

    def to_string(self):
        return f"{self.name}, {self.vname} ({self.lfdnr})"

search(GenerateRandomAutor(), "Peter")