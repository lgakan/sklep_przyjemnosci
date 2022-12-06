from typing import List, Tuple


class Client:
    def __init__(self, client_id: int, order: List[Tuple[int, int]], budget: int):
        self.client_id = client_id
        self.order = order
        self.budget = budget

    def get_order(self) -> List[Tuple[int, int]]:
        return self.order


if __name__ == '__main__':
    lista = [(1, 20), (7, 15), (3, 2)]
    client1 = Client(1, lista, 300)
    print(client1.get_order())
