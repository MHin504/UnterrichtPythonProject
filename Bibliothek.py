class Buch:
    def __init__(self, titel, autoren):
        self.titel = titel
        self.autoren = autoren

    def to_string(self):
        ergebnis = "Titel: " + self.titel
        for autor in self.autoren:
            ergebnis += " " + autor.to_string()
        return ergebnis


class Autor:
    def __init__(self, name, vorname):
        self.name = name
        self.vorname = vorname

    def to_string(self):
        return f"Autor: {self.name}, Vorname: {self.vorname}"


class Bibliothek:
    def __init__(self):
        self.katalog = Katalog()
        self.nutzerkonten = Nutzerkonto()

    def get_katalog(self):
        return self.katalog


class Katalog:
    def __init__(self):
        self.buecher = []

    def buch_hinzufuegen(self, neues_buch):
        self.buecher.append(neues_buch)

    def suche(self, suchbegriff):
        result = []
        for buch in self.buecher:
            if suchbegriff in buch.to_string():
                result.append(buch.to_string())
        return result

    def to_string(self):
        ergebnis = ""
        for buch in self.buecher:
            ergebnis += " " + buch.to_string() + "\n"
        return ergebnis


class Nutzerkonto:
    def __init__(self):
        self.nutzerkonten = []


a1 = Autor("Lucas", "George")
a2 = Autor("Rowling", "J.K.")
autorenliste1 = [a1, a2]
a3 = Autor("Pan", "Peter")
a4 = Autor("Hook", "Captain")
autorenliste2 = [a3, a4]
buch1 = Buch("Star Wars", autorenliste1)
buch2 = Buch("Lummerland", autorenliste2)
bibliothek = Bibliothek()
bibliothek.get_katalog().buch_hinzufuegen(buch1)
bibliothek.get_katalog().buch_hinzufuegen(buch2)

suche = input("Geben Sie einen Suchbegriff ein: ")
print(bibliothek.get_katalog().suche(suche))
