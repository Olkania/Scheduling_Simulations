#!/usr/bin/python3
from queue import Queue #importowanie kolejki FIFO
licznik_stron= dict()

def find_mfu(ramka):
    max = 0
    max_key = 0
    for key in ramka:
        if licznik_stron[key] > max:
            max = licznik_stron[key]
            max_key = key
    return max_key

def read_file(rf, start_line, counter_lines):  #odczyt pliku do tabeli
    iterator = 0
    file = open("Stron.txt", "r")
    for value in file:              #szukanie linii od ktorej ma pobierac dane
        if iterator < start_line:
            iterator += 1
            continue

        rf.append(int(value))
        licznik_stron[int(value)] = 0
        iterator += 1

        if iterator >= start_line + counter_lines:
            break
    
def replace_page(ts, n, r, liczba_procesow):
    ramka = list()   #ramki ze stronami
    licznik = 0
    for i in range(n):
        if len(ramka) < r:      #dodawania do ramki, jak nie jest pelna
            if ts[i] not in ramka:
                ramka.append(ts[i])
                licznik += 1
                licznik_stron[ts[i]] += 1
        else:
            if ts[i] not in ramka:      #wyrzucanie z kolejki i dodanie na koniec
                mfu = find_mfu(ramka)
                ramka.remove(mfu)
                ramka.append(ts[i])
                licznik += 1
                licznik_stron[ts[i]] += 1      
    file = open("WynikiMFU.txt", "a")
    print(str(licznik/liczba_procesow), file = file)
    print('---------', file = file)

liczba_procesow = 100
liczba_testow = 100
   
if __name__ == "__main__":
    file = open("WynikiMFU.txt", "w+")     #czyszczenie pliku, aby był pusty przy wykonywaniu/ tworzenie pliku jezeli go nie ma
    print('---------', file = file)
    file.close()
    for r in range(3):
        if r == 0:
            r1 = 3      #moje wybrane parametry R={3, 4, 7}
        if r == 1:
            r1 = 4
        if r == 2:
            r1 = 7
        for k in range(0, liczba_testow):
            t_stron = list()  
            read_file(t_stron, k * liczba_procesow, liczba_procesow)
            replace_page(t_stron, liczba_procesow, r1, liczba_procesow)