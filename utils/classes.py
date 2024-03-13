class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name                              #название
        self.description = description                #описание
        self.products = products                      #список товаров
        Category.category_count += 1                  #общее количество категорий
        Category.product_count += len(self.products)  #количество уникальных продуктов




class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name                              #название
        self.description = description                #описание
        self.price = float(price)                     #цена
        self.quantity = quantity                      #количество в наличии


