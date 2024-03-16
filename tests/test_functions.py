import pytest

from utils.classes import Category, Product

goods = [
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]
  },
  {
    "name": "Телевизоры",
    "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    "products": [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]
  }
]

commodity = [
    {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    },
    {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
    },
    {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
    }
]


@pytest.fixture()
def category():
    return Category(goods[0]["name"], goods[0]["description"], goods[0]["products"])


def test_init_category(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert category.category_count == 1
    assert category.product_count == 3


@pytest.fixture()
def product():
    return Product(goods[0]["products"][0]["name"], goods[0]["products"][0]["description"], goods[0]["products"][0]["price"], goods[0]["products"][0]["quantity"])


def test_init_product(product):
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

@pytest.fixture()
def dictionary():
    return Product.from_dictionary(commodity[0])

def test_class_product(dictionary):
    assert dictionary.name == "Samsung Galaxy C23 Ultra"
    assert dictionary.description == "256GB, Серый цвет, 200MP камера"
    assert dictionary.price == 180000.0
    assert dictionary.quantity == 5


