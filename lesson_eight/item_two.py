class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"На ноль делить нельзя!")


print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 1))
