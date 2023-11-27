import random

zbior_hasla = ['kot', 'pies', 'samochód', 'bidon']  #Zbiór haseł

wylosowane_haslo = zbior_hasla[random.randint(0, len(zbior_hasla)-1)]  #Losowanie hasła z tablicy

print(f"Witamy w grze wisielec! \nNa to hasło masz {len(wylosowane_haslo) * 2} prób!")

przeliterowane_haslo = []

for i in wylosowane_haslo:  #Przeiterowanie hasła
    przeliterowane_haslo.append(i)

proby_zle = 0 #Próby do przerwania gry gdy gracz przegra
proby_dobre_i_zle = 0 #Próby do wyświetlenia statystyki

wyswietalnie = ['_ '] * len(wylosowane_haslo)

print(''.join(wyswietalnie))

while True:
    zgadywanie_gracza = input("Podaj literę:") #Litera gracza
    zgadywanie_gracza = zgadywanie_gracza.lower()
    if len(zgadywanie_gracza) == 1 and zgadywanie_gracza in przeliterowane_haslo: #Instrukcja warunkowa sprawdzająca poprawność litery
        proby_dobre_i_zle += 1 #Doliczenie próby do statystyki
        print("Brawo zgadłeś")
        index = przeliterowane_haslo.index(zgadywanie_gracza) #Sprawdzenie pod jakim indeksem znajduje się litera
        wyswietalnie[index] = zgadywanie_gracza #Wyświetlenie lietery na ekranie żeby pomagać graczowy
        print(''.join(wyswietalnie))
        if '_ ' not in wyswietalnie: #instrukcja sprawdzająca czy są jeszcze jakieś litery do zgadnięcia
            print(f"BRAWO WYGRAŁEŚ HASŁEM BYŁ: {wylosowane_haslo.upper()} ") #Wyświetalnie tekstu końcowego
            print(f"Udało Ci się to zarobić w {proby_dobre_i_zle} ruchów") #Wyświetlanie statystyki gracza
            break #Przerwanie programu
    else:
        print("Przykro mi nie zgadłeś") #Wyświetalnie komunikatu gdy gracz przegra
        proby_dobre_i_zle +=1 #Zliczanie prób
        proby_zle += 1 #Zliczanie prób do przegrania gry
        if proby_zle > len(wylosowane_haslo) * 2: #Instrukcja sprawdzająca czy gracz już przegrał
            print(f"Przegrałeś, hasłem było : {wylosowane_haslo}") #Komunikat gdy gracz przegra
