import names
import Auor as Autor
# Beispiel für die Erstellung eines zufälligen Autoren
def generate_random_autor(index):
        name = names.get_last_name()
        vname = names.get_first_name()
        return Autor(name, vname, index)