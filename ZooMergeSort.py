import RandomList
import ZooBubbleSort
import time

def merge(linke_hl, rechte_hl):
    sortierte_liste = [None] * (len(linke_hl) + len(rechte_hl))
    zeiger_l = 0
    zeiger_r = 0
    index = 0
    while zeiger_l < len(linke_hl) and zeiger_r < len(rechte_hl):
        if linke_hl[zeiger_l] < rechte_hl[zeiger_r]:
            sortierte_liste[index] = linke_hl[zeiger_l]
            zeiger_l += 1
            index += 1
        else:
            sortierte_liste[index] = rechte_hl[zeiger_r]
            zeiger_r += 1
            index += 1
    while zeiger_l < len(linke_hl):
        sortierte_liste[index] = linke_hl[zeiger_l]
        zeiger_l += 1
        index += 1
    while zeiger_r < len(rechte_hl):
        sortierte_liste[index] = rechte_hl[zeiger_r]
        zeiger_r += 1
        index += 1
    return sortierte_liste


def merge_sort(array):
    if len(array) <= 1:
        return array
    mitte = len(array) // 2
    lh = array[:mitte]
    rh = array[mitte:]
    return merge(merge_sort(lh), merge_sort(rh))

zoo=['🐶','🐱','🐒','🐧','🐍','🦎','🦉','🐫','🐘']
start = time.time()
merge_sort(RandomList.random_list(100000))
ende = time.time()
print(f"Zeit zwischen Start und Ende MergeSort {(ende-start):.6f}")
start = time.time()
ZooBubbleSort.bubble_sort(RandomList.random_list(100000))
ende = time.time()
print(f"Zeit zwischen Start und Ende BubbleSort {(ende-start):.6f}")