class Computer:
    __max_price = 1000


    def get_max_price(self):
        return self.__max_price

    def set_max_price(self, price):
        self.__max_price = price
        

comp = Computer()
print(comp.get_max_price())

comp.set_max_price(900)
print(comp.get_max_price())
