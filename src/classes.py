class Product:
    """
    Класс для описания товара в магазине.
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data, products=None):
        """Класс-метод для создания товара из словаря с проверкой дубликатов"""
        if products is None:
            products = []
        name = product_data.get("name")
        # Проверка на дубликаты
        for prod in products:
            if prod.name == name:
                prod.quantity += product_data.get("quantity", 0)
                if product_data.get("price", 0) > prod.price:
                    prod.price = product_data.get("price")
                return prod
        return cls(
            name=name,
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity"),
        )

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        # Подтверждение снижения цены
        if new_price < self.__price:
            confirm = input(f"Цена снижается с {self.__price} до {new_price}. Продолжить? (y/n): ")
            if confirm.lower() != "y":
                print("Отмена изменения цены")
                return
        self.__price = new_price


class Category:
    """
    Класс для описания категории товаров.
    """

    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет продукт в приватный список"""
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только объекты Product")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для вывода списка товаров"""
        return "\n".join([f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products])
