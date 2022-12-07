from typing import List, Tuple
from general_inventory import GeneralInventory


class Client:
    def __init__(self, client_id: int, order: List[Tuple[int, int]], budget: int, inventory: GeneralInventory):
        self.client_id = client_id
        self.order = order
        self.budget = budget
        self.inventory = inventory

    def get_order(self) -> List[Tuple[int, int]]:
        return self.order
