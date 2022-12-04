from typing import List, Tuple, Dict

# można by zrobić jakoś, żeby id inicjalizowało się samo (następny wolny numer)
# i było wiązane z jakąś nazwą produktu
# wtedy potrzebowalibyśmy ogólnej listy z produktami


class ProductList: # na razie roboczo wstawione, do obgadania
    def __init__(self):
        self.product_list = []


class Product:
    def __init__(self, product_id: int, product_name: str, product_weight: float):
        self.product_id = product_id  #jeśli lista przejdzie to inicjalizacja z None
        self.product_name = product_name
        self.product_weight = product_weight

