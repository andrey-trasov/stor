class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name                              #название
        self.description = description                #описание
        self.__products = products                    #список товаров
        Category.category_count += 1                  #общее количество категорий
        Category.product_count += len(self.__products)  #количество уникальных продуктов


    def add_products(self, goods):
        self.__products.append(goods)


    @property
    def products(self):
        for j in self.__products:
            print(f"{j.name}, {int(j.price)} руб. Остаток: {j.quantity} шт.")



class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name                              #название
        self.description = description                #описание
        self.__price = float(price)                   #цена
        self.quantity = quantity                      #количество в наличии


    @classmethod
    def from_dictionary(cls, dictionary):
        name = dictionary["name"]
        description = dictionary["description"]
        price = dictionary["price"]
        quantity = dictionary["quantity"]
        return cls(name, description, price, quantity)


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price):
        if new_price <= self.__price:
            print('Цена введена некорректная')
        else:
            self.__price = new_price


    @price.deleter
    def price(self):
        self.__price = None



