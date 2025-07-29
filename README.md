# Ocena zdolności kredytowej klienta na podstawie danych demograficznych i finansowych

Projekt miał na celu porównanie czterech metod klasyfikacyjnych służących do oceny zdolności kredytowej klientów banku. Analizie poddano rzeczywisty zbiór danych demograficznych i finansowych opisujących osoby ubiegające się o kredyt.


## Zastosowane metody klasyfikacji

- Regresja logistyczna  
- Metoda k-najbliższych sąsiadów (kNN)  
- Liniowa analiza dyskryminacyjna (LDA)  
- Model hybrydowy (średnia ważona wyników powyższych trzech metod)


## Zmienne wykorzystane w analizie

Dane pochodzą z repozytorium UCI Machine Learning:  
[Dua, D., & Graff, C. (1994). Statlog (German Credit Data)](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data)

Zbiór zawiera 1000 obserwacji oraz 15 cech klienta:

- Status rachunku bieżącego  
- Czas trwania kredytu  
- Historia kredytowa  
- Cel kredytu  
- Kwota kredytu  
- Oszczędności / obligacje  
- Staż zatrudnienia  
- Rata w stosunku do dochodu  
- Status osobisty i płeć  
- Obecność poręczyciela  
- Czas zamieszkania  
- Rodzaj majątku  
- Wiek klienta  
- Liczba aktualnych kredytów  
- Rodzaj pracy  

Dane nie zawierały braków. Obserwacje odstające zostały zachowane ze względu na ich realny charakter.


## Technologie

- **Python** – trenowanie modeli, obliczanie metryk skuteczności, wykresy ROC, macierze pomyłek  
- **R** – histogramy i boxploty  
- **Excel** – statystyki opisowe, wykresy porównawcze, eksploracja danych


## Wyniki

Wszystkie metody umożliwiły stosunkowo trafną klasyfikację zdolności kredytowej klientów. Najlepsze rezultaty osiągnęła regresja logistyczna, natomiast najsłabiej wypadł model kNN. Model hybrydowy uzyskał najwyższą wartość AUC-ROC, lecz cechował się mniejszą stabilnością. Największy wpływ na klasyfikację miały: status rachunku, historia kredytowa oraz czas trwania kredytu.

## Zawartość repozytorium

- `Ocena zdolności kredytowej klienta.pdf` - pełny raport klasyfikacji
  
- `Analiza Danych.xlsx` – plik Excela zawierający:
  - surowe dane wejściowe  
  - statystyki opisowe  
  - wykresy porównujące skuteczność klasyfikatorów  

- `BiH.R` – skrypt w języku R generujący histogramy i wykresy typu boxplot  

- `METDAN/` – folder z programem w Pythonie:
  - trenowanie modeli (regresja, kNN, LDA, hybryda)  
  - obliczanie miar skuteczności  
  - wykresy ROC i macierze pomyłek

-  `regresja_logistyczna/` – folder zawierający skrypt Pythona:
  - bliczanie współczynników regresji oraz wartości istotności (p-value)
dla każdej z cech,
  - wizualizację wpływu cech na wynik klasyfikacji


## Autorzy

- Maja Fiszer  
- Jakub Gilewski  
- Dominik Uchman  
