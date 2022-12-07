class Product:
    def __init__(self, product_id: int, product_name: str, product_weight: float):
        self.product_id = product_id  #jeśli lista przejdzie to inicjalizacja z None
        self.product_name = product_name
        self.product_weight = product_weight

    def get_product_weight(self):
        return self.product_weight

    def get_product_name(self):
        return self.product_name

    def __repr__(self):
        return f'{self.product_id}, {self.product_name}, {self.product_weight}'
