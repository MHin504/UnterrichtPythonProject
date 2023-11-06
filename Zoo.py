python = {
    "name": "Python",
    "gefahr": 7,
    "futterbedarf": 10
}

tiger = {
    "name": "Tiger",
    "gefahr": 9,
    "futterbedarf": 100
}

baer = {
    "name": "Baer",
    "gefahr": 8,
    "futterbedarf": 50
}

def tier_hinzufuegen(zoo, tier):
    if str(tier['gefahr']).isnumeric() & str(tier['futterbedarf']).isnumeric():
        existing_tier = next((t for t in zoo if t['name'].lower() == tier['name'].lower()), None)
        if existing_tier is None:
            zoo.append(tier)
        else:
            print(f"Tier {tier['name']} existiert bereits im Zoo.")
            user_choice = input("Möchten Sie das Tier mit den neuen Parametern angeben? (ja/nein)\n")
            if user_choice.lower() == 'ja':
                zoo.append(tier)
            else:
                print("Tier wird nicht angelegt.")
    else:
        print(f"Bitte geben Sie als Gefahrenwert und Futterbedarf nur zahlen an. Tier {tier['name']} wurde nicht angelegt.")


def max_gefahr(zoo):
    max_tier = max(zoo, key=lambda x: x['gefahr'])
    return (max_tier['name'], max_tier['gefahr'])

def print_zoo(zoo):
    counter = 1
    for tier in zoo:
        print(f"Tier {counter}: {tier['name']}, Gefährlichkeit: {tier['gefahr']}, Futterbedarf: {tier['futterbedarf']}")
        counter = counter+1

def futterbedarf_berechnen(zoo):
    total_futterbedarf = sum(tier['futterbedarf'] for tier in zoo)
    return total_futterbedarf

def get_tier_index(zoo, tier_name):
    for i, tier in enumerate(zoo):
        if tier['name'].lower() == tier_name.lower():
            return i
    return -1

def loesche_tier(zoo, tier_name):
    index = get_tier_index(zoo, tier_name)
    if index != -1:
        del zoo[index]
        print(f"Tier {tier_name} wurde aus dem Zoo gelöscht.")
    else:
        print(f"Tier {tier_name} existiert nicht im Zoo.")

zoo = [python, tiger, baer]
tier_hinzufuegen(zoo, {"name": "Giraffe", "gefahr": 2, "futterbedarf": 30})
tier_hinzufuegen(zoo, {"name": "PythonTest", "gefahr": "abc", "futterbedarf": 10})
tier_hinzufuegen(zoo, {"name": "Python", "gefahr": 7, "futterbedarf": 10})
print(max_gefahr(zoo))
print_zoo(zoo)
print(f"Der gesamte Futterbedarf beträgt: {futterbedarf_berechnen(zoo)}")
loesche_tier(zoo, "Python")
loesche_tier(zoo, "Giraffe")
print_zoo(zoo)