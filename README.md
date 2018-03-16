# Game of Life - Python
Generator losowych układów z prezentacją symulacji w oknie

Poprzez zmianę wartości można wpływać na to, jak będzie wyglądać układ (najważniejszy jest seed - od niego zależy początkowy układ: dla tego samego seedu zawsze zostanie wygenerowany ten sam układ (o ile nie zmieni się ilość początkowo żywych kratek i rozmiary planszy) )


Zasady gry w życie:
1. Komórka może być żywa (czarna) lub martwa (biała)
2. Każda generacja powstaje wg określonych zasad na podstawie ułożenia poprzedniej generacji:
  a) Jeżeli żywą komórkę otacza n żywych komórek, to pozostanie ona żywa
  b) Jeżeli martwą komórkę otacza m żywych komórek, to staje się ona żywa
  c) Jeżeli żywą komórkę otacza mniej lub więcej niż n żywych komórek, komórka umiera
  d) Martwa komórka, nieotoczona przez m żywych komórek, umiera
3. Dla podstawowej wersji Fry w Życie (zasady Conwaya): n = 2 lub 3, m = 3


Zmiana ustawień - na początku kodu:

Rzm - wymiary okna (okno jest kwadratowe, więc tylko jedna liczba)

s - rozmiar planszy (ilość kratek) - kratki są kwadratowe, więc plansza bęzie rozmiarów s na s, Rzm powinno być podzielne przez s

Seed - tutaj można podać liczbę, lub stringa - to definiuje sposób generowania początkowej planszy

Kratki - ilość kratek, która żyje (wybierane losowo) w pierwszej generacji, powinna być mniejsza od s^2 (inaczej może pojawić się ValueError)

czas - ilość czasu, która mija między wygenerowaniem i narysowaniem generacji, a rozpoczęciem robienia kolejnej, jest zawsze mniejszy od rzeczywistego - nie uwzględa czasu potrzebnego na obliczenia i rysowanie, który zależy od komputera

Pattern - tutaj należy podać pattern gry - przed ukośnikiem podajemy liczby sąsiadów (od 0 do 8), aby żywa komórka przyżyła, po ukośniku - aby martwa mogła ożyć. Dla reguł Conwaya jest to "23/3": przy 2 i 3 sąsiadach komórka może przyeżyć, przy 3 może ożyć



Lista patternów (z Wikipedii):

23/3 - "Zasady Conwaya" - Domyślny wzór, bardzo złożone zachowania

/2 - "Seeds" - Wzrost intensywny, chaotyczny

/234 - "Serwety" - Przypomina koronki, serwety

012345678/3 - "Płatki, Życie bez śmierci" - Wzory przypominają drabiny

1/1 - "Narośl" - Tworzy interesujące formy, startuje nawet od pojedynczej komórki

12345/3 - "Labirynt" - Tworzy wzory przypominające labirynty

125/36 - "2x2" - Ma dużo oscylatorów i statków

1357/1357 - "Replikator" - Każda struktura jest z czasem zastępowana przez jej kilka kopii

1358/357 - "Ameba" - Dobrze zbalansowana między życiem a śmiercią, ma statki

23/36 - "HighLife" - Podobne do Conwaya (część jej struktur działa w HighLife), w dodatku struktura samoreplikująca

2345/45678 - "Miasta otoczone murem" - Tworzy aktywne centra otoczone statycznymi ścianami

235678/3678	- "Plamy" - Szybko się stabiliuje

235678/378 - "Koagulacje" - Wzory rozszerzają się, w przeciwieństwie do plam

238/357 - "Pseudożycie" - Ewolucja przypomina 23/3, ale mało który wzór z Conwaya działa pod tymi regułami

245/368 - "Ruch" - Losowe struktury zwykle się stabilizują, ale wiele statków występuje naturalnie i często się pojawia. Najczęściej pojawiają się struktury stabilne, okresowe z okresem 2 lub 4, statek o okresie 7 i „dymiący pociąg” o okresie 170

34/34 - "Trzy cztery" - Początkowo sądzono, że ma ona tendencje do stabilizacji, ale dzięki symulacji komputerowej okazało się, że większe wzory eksplodują. Dużo małych oscylatorów i statki

34678/3678 - "Dzień i noc" - Dużo wzorów o złożonym zachowaniu. Wzory można odwracać – uczynić wszystkie żywe komórki martwymi i na odwrót, a będzie on działał identycznie.

4567/345 - "Asymilacja" - Tworzy statystyczne struktury przypominające diament, wnętrza kryształów częściowo wypełnione

45678/3 - "Koral" - Wzory rosną powoli, tworzą struktury przypominające rafę koralową

5/345 - "Długie życie" - Bardzo łatwo można spotkać oscylatory o długim okresie

5678/35678 - "Diameba" - Tworzy wielkie zwarte struktury z chaotycznie oscylującymi granicami



Możliwości jest 2^18 - więc to jest tylko kilka
