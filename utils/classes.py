class Category:
    name: str
    description: str
    goods: list
    number_of_categories = 0
    number_of_unique_products = 0

    def __init__(self, name, description, goods, number_of_categories):
        self.name = name                              #название
        self.description = description                #описание
        self.goods = goods                            #список товаров
        self.number_of_categories = number_of_categories    #общее количество категорий
        Category.number_of_unique_products += len(goods)   #количество уникальных продуктов




class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name                              #название
        self.description = description                #описание
        self.price = float(price)                     #цена
        self.quantity = quantity                      #количество в наличии


