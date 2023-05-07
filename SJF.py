#!/usr/bin/python3

def read_file(rf, start_line, counter_lines):  #odczyt pliku do tabeli
    iterator = 0
    file = open("Czasu_Burst.txt", "r")
    for value in file:              #szukanie linii od ktorej ma pobierac dane
        if iterator < start_line:
            iterator += 1
            continue

        rf.append(int(value))
        iterator += 1

        if iterator >= start_line + counter_lines:
            break
            
def waiting_time(tp, wt):
    wt[0]=0         #pierwszy proces nie czeka to- czas oczekiwania
    for i in range(1, liczba_procesow):
        wt[i] = tp[i-1] + wt[i-1]        
        
def turn_time(tp, wt, tt):              #tp- czas przetwarzania procesu; wt- "waiting time", czekania; tt- czas cyklu
    for i in range(liczba_procesow):
        tt[i] = tp[i] + wt[i]
    
def average_time(t_przetwarzania):
    t_czekania = [0] * liczba_procesow
    t_cyklu = [0] * liczba_procesow
    suma_czekania = 0
    suma_cyklu = 0
    
    waiting_time(t_przetwarzania, t_czekania)
    turn_time(t_przetwarzania, t_czekania, t_cyklu)
    
    for i in range(liczba_procesow):
        suma_czekania = suma_czekania + t_czekania[i]
        suma_cyklu = suma_cyklu + t_cyklu[i]
    
    file = open("WynikiSJF.txt", "a")
    print(str(suma_czekania/liczba_procesow), file = file)
    print(str(suma_cyklu/liczba_procesow), file = file)
    print('---------', file = file)

liczba_procesow = 100
liczba_testow = 100
   
if __name__ == "__main__":
    file = open("WynikiSJF.txt", "w+")     #czyszczenie pliku, aby był pusty przy wykonywaniu/ tworzenie pliku jezeli go nie ma
    print('---------', file = file)
    file.close()
    for k in range(0, liczba_testow):
        t_przetwarzania = list() #tworzenie tablicy 100 elementowej wypełnionymi 0; t_t- czas trwania procesu
        read_file(t_przetwarzania, k * liczba_procesow, liczba_procesow)
        t_przetwarzania.sort()
        average_time(t_przetwarzania)