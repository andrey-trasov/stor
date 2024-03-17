class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name                              #название
        self.description = description                #описание
        self.__products = products                    #список товаров
        Category.category_count += 1                  #общее количество категорий
        Category.product_count += len(self.__products)  #количество уникальных продуктов


    def add_product(self, product):
        self.__products.append(product)


    @property
    def products(self):
        list_products = []
        for j in self.__products:
            list_products.append(f"{j.name}, {int(j.price)} руб. Остаток: {j.quantity} шт.")

