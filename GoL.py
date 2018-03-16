#Te rzeczy możesz zmieniać, aby uzyskiwać różne układy

Rzm = 800 #rozmiar okna: Rzm x Rzm (domyslnie 800x800)
s = 40 #rozmiar planszy: s x s, Rzm musi byc podzielne przez s (inaczej moze byc krzywo albo nie pokazywac czegos albo cos)
Seed = "Zwykły Seed" #seed do losowania - liczba albo string
Kratki = 800 #ile kratek bedzie poczatkowo "zywych" - musi byc mniej, niz s^2 (inaczej pokaze ValueError)
czas = 50 #ile milisekund czekac do zrobienia nowej generacji
#Uwaga - dla duzych ukladow program dziala wolniej - i nie mozna nic z tym zrobic


#Nizej faktyczny kod


import tkinter as tk
import random as rnd


#Klasa okna:
class Application:
    def __init__(self, rozmiar):
        self.Arr = [ [False for x in range(s)] for y in range(s) ] #Tablica o wymiarach s x s, poczatkowo falsz (martwa)

        self.window = tk.Tk()
        self.window.resizable(width = False, height = False)
        self.window.geometry(rozmiar)
        self.window.title("Game of Life")

        self.canvas = tk.Canvas(self.window, width = Rzm, height = Rzm)
        self.canvas.pack()

        self.createArray()

        #Tutaj sa ladne sobie kwadraty ktore beda sobie malowane
        self.Rct = [ [self.canvas.create_rectangle(x*krSz, y*krSz, krSz*(x+1), krSz*(y+1), fill="white") for x in range(s)] for y in range(s) ]

        self.updated()

        self.window.mainloop()

    #Funckja do uzupelnienia tablicy
    def createArray(self):
        #Wybiera *Kratki* liczb od 0 do s*s i odpowiednie miejsca w tablicy daje tam prawde (zywa)
        for z in rnd.sample(range(s*s), Kratki):
            self.Arr[z%s][z//s] = True

        #vvv tutaj byly customowe figury
        #self.Arr[3][1] = True
        #self.Arr[4][2] = True
        #self.Arr[4][3] = True
        #self.Arr[3][3] = True
        #self.Arr[2][3] = True


    #Dla kratki o koord. x, y oblicza, ile jest zywych dookola niej
    def liczObok(self, x, y):
        #Mniejsze i wieksze pola - przejscia, jezeli wychodza poza granice: (ifFalse, ifTrue)[condition]
        xm = ( x-1, s-1 )[ (x-1) == -1 ]
        xw = ( x+1, 0   )[ (x+1) ==  s ]
        ym = ( y-1, s-1 )[ (y-1) == -1 ]
        yw = ( y+1, 0   )[ (y+1) ==  s ]
        #Zwrocenie liczby pol
        wynik  = int(self.Arr[xm][ym]) + int(self.Arr[x][ym]) + int(self.Arr[xw][ym])
        wynik += int(self.Arr[xm][y])  +          0           + int(self.Arr[xw][y])
        wynik += int(self.Arr[xm][yw]) + int(self.Arr[x][yw]) + int(self.Arr[xw][yw])

        return wynik


    #Funkcja update
    def updated(self):

        #Rysowanie
        for x in range(s):
            for y in range(s):
                if self.Arr[x][y]:
                    self.canvas.itemconfig(self.Rct[x][y], fill="black") #Jeżeli jest żywe, robi czarne
                else:
                    self.canvas.itemconfig(self.Rct[x][y], fill="white") #A jak nie, to bialy


        #Tymczasowa tablica zawierajaca odswiezone stany
        OdswArr = [ [False for x in range(s)] for y in range(s) ]

        #Uzupelnienie tymczasowej tablicy nowa warstwa
        for x in range(s):
            for y in range(s):
                sasiedzi = self.liczObok(x, y)
                if sasiedzi <= 1:
                    OdswArr[x][y] = False
                elif 2 <= sasiedzi <= 3 and self.Arr[x][y] == True:
                    OdswArr[x][y] = True
                elif sasiedzi >= 4:
                    OdswArr[x][y] = False
                elif sasiedzi == 3 and self.Arr[x][y] == False:
                    OdswArr[x][y] = True
                else:
                    OdswArr[x][y] = self.Arr[x][y]

        #Podmiana tablicy
        self.Arr = OdswArr.copy()

        #Odpalenie ponownie po *podanej ilosci* ms
        self.window.after(czas, self.updated)



#Aktualne dzialanie programu - koniec definicji


krSz = Rzm/s #Wymiar jednej kratki - zeby bylo prosciej pisac

rnd.seed(Seed)

#String rozmiaru okna
rozmiar = str(Rzm) + "x" + str(Rzm)

#Tworzenie obiektu aplikacji
apl = Application(rozmiar)
