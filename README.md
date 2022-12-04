# Shop description
All necessary info about files is in zadaniabo2.txt 


Delivery functionality:

Posiada klasę Delivery do konstruktora podawana jest lista list:

[[a0,b0], [a1,b1], ..., [an,bn], [an+1]]

Cena przesyłki:      Waga produktów:

a0			waga < b0

a1			b0 < waga < b1

...

an			bn-1 < waga < bn

an+1			bn < waga

Delivery.get_cost(weight: int/float) - zwraca koszt przesyłki przy zadanej wadze


Discount functionality:

Posiada klasę Discount do konstruktora podawana jest lista list:

[[a0,b0], [a1,b1], ..., [an,bn], [an+1]]

Wartość zniżki:      Ilość produktów:

a0			ilość < b0

a1			b0 < ilość < b1

...

an			bn-1 < ilość < bn

an+1			bn < ilość

Discount.get_new_cost(old_price: List[int/float], amount: int) - zwraca wektor nowych cen produktów przy zadanej ilości produktów
