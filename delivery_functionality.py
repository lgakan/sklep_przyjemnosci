class Delivery:

    def __init__(self, list_of_conditions: list):
        self.func = build_func(list_of_conditions)

    def get_cost(self, weight):
        return self.get_func()(weight)

    def get_func(self):
        return self.func


def build_func(conditions: list):
    string_to_lambda = ""
    for i, pair in enumerate(conditions):
        if i not in [0, len(conditions) - 1]:
            string_to_lambda += "("
        if len(pair) == 2:
            string_to_lambda += f"{pair[0]} if x < {pair[1]} else "
        else:
            string_to_lambda += f"{pair[0]}"
    string_to_lambda += (len(conditions) - 2)*")"
    return lambda x: eval(string_to_lambda)
