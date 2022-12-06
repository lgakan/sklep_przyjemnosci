from delivery_functionality import build_func


class Discount:

    def __init__(self, list_of_conditions: list):
        self.discount = build_func(list_of_conditions)

    def get_new_cost(self, old_cost, amount):
        disc = self.get_disc()(amount)
        return [cost * disc for cost in old_cost]

    def get_disc(self):
        return self.discount

    def __repr__(self):
        return f'{self.discount}'


def main():
    x_price = [100, 40, 22, 36]
    handle_disc = Discount([[1, 10], [0.90]])
    x_new = handle_disc.get_new_cost(x_price, 10)
    print(x_new)


if __name__ == '__main__':
    main()
