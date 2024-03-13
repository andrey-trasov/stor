from classes import Category, Product
from utils.functions import open_file


def main():
    global i
    file_json = 'products.json'
    file = open_file(file_json)
    list_category = []
    for i in file:
        list_product = []
        for j in i["products"]:
            product = Product(j["name"], j["description"], j["price"], j["quantity"])
            list_product.append(product)  # список классов Product
        category = Category(i['name'], i['description'], list_product)
        list_category.append(category)  # список классов Category
    # печатаем данные из списка Category

    for i in list_category:
        print(f'Название категории: {i.name}')
        print(f'Описание категории: {i.description}')
        print("Товары:")
        for j in i.products:
            print(f'Название товара: {j.name}')
            print(f'Описание товара: {j.description}')
            print(f'Цена товара: {j.price}')
            print(f'Количество в наличии: {j.quantity}')
            print()
        print()
    print(f'Общее количество категорий: {i.category_count}')
    print(f'Количество уникальных продуктов: {i.product_count}')


if __name__ == '__main__':
    main()
