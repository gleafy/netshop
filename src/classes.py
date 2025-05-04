
class Product:
    """
    Класс для описания товара в магазине.
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """
        Метод для инициализации объекта класса Product.
        Задает значения атрибутам объекта при его создании.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    """
    Класс для описания категории товаров.
    """
    name: str
    description: str
    products: list[Product]


    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """
        Метод для инициализации объекта класса Category.
        Задает значения атрибутам объекта при его создании
        и обновляет счетчики категорий и товаров.
        """
        self.name = name
        self.description = description
        self.products = products


        Category.category_count += 1
        Category.product_count += len(products)