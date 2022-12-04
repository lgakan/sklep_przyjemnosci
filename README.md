# Shop description
All necessary info about files is in zadaniabo2.txt 

Delivery functionality:\n
Posiada klasę Delivery:\n
do konstruktora podawana jest lista list:
[[a0,b0], [a1,b1], ..., [an,bn], [an+1]]
którą odczytywać należy w następujący sposób:
Cena przesyłki:      Waga produktów:
a0			waga < b0
a1			b0 < waga < b1
...
an			bn-1 < waga < bn
an+1			bn < waga

Aby otrzymać cenę przesyłki z obiektu klasy Delivery należy użyć metody self.get_cost(weight: int/float)