import json

# otwieram plik json 'lang_dict.json' zawierający poszczególne alfabety
# popracuję nad dodaniem innych  :-)

with open('/home/lang_dict.json') as f:
    data = json.load(f)

file_name = '/home/example (kopia).txt'
# kopia pliku - dodane kilka znaków niepożądanych - *, &, #
# w kilku pierwszych wyrazach do testów
# ładujemy plik txt i zmieniamy wszystkie litery na małe

introduction_file_text = open(file_name).read().lower()
sep = introduction_file_text.split()
# wybieram konkretny alfabet z pliku JSONa
alfabet = data['alfabet_pl']

# sprawdzam czy każdą litera w słowie jest z alfabetu, jeśłi nie to zmieniam na spacje "  "
# oddzielam podzielone wyrazy - jeżeli podzieli to wyraz na co najmniej dwie części
#traktujemy je jako oddzielne wyrazy

strings = sep
new_strings = []

for string in strings:
    new_string = string
    for ch in string:
        if ch not in alfabet:
            new_string = new_string.replace(ch, " ")
    new_strings.extend(new_string.split())

# do każdego wyrazu na początku dodajemy znak '<' i '>', które będą oznaczać początek i koniec wyrazu.
lista = ['<' + item + '>' for item in new_strings]

# podaje się minimalne i maksymalne N, ale maksymalne N jest opcjonalne i jeżeli nie będzie podane
# to szukane są N gramy dla minimalnego N

n_min = int(input("Podaj minimalny N: "))
try:
    n_max = int(input("Podaj maksymaly N: "))
except (TypeError, ValueError):
    n_max = n_min
    print()
    print("Nie podałeś max N, rozumiem, że interesuje Cię tylko min N")

# albo tak ale nie jest odporne na str.
'''
n_min = int(input("Podaj minimalny N: "))
in_value = int(input("Podaj maksymaly N: "))
if in_value == '':
    n_max = n_min
else:
    n_max = int(in_value)

'''

plik_zapis = open('ngams.txt', 'wt')

count = {}

for s in lista:
    for nlen in range(n_min, n_max + 1):
        for ii in range(len(s) - nlen + 1):
            ngram = s[ii:(ii + nlen)]
            print(ngram)# jeśli chcemy widzieć w konsoli
            print(ngram, file=plik_zapis)
            if len(ngram) not in count:
                count[len(ngram)] = 0
            count[len(ngram)] += 1

print()
print("Ilość poszczególnych N-gramów:", count)
print("Ilość poszczególnych N-gramów:", count, file=plik_zapis)  # jeśli ma być zapis do pliku
plik_zapis.close()

# wczytuję zapisany plik

#ngrams_txt = '/home/pattom/PycharmProjects/N-grams-CLARIN-pl/ngams.txt'
#resault = open(ngrams_txt).read()
#print(resault)
