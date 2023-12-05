def bubble_sort(liste):
    for durchgang in range(0, len(liste)):
        for j in range(0, len(liste) - 1):
            if (liste[j] > liste[j + 1]):
                temp = liste[j + 1]
                liste[j + 1] = liste[j]
                liste[j] = temp
    return liste
