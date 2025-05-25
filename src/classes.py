from abc import ABC, abstractmethod


class LogMixin:
    """Миксин для логирования создания объектов."""

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект {self.__class__.__name__} с параметрами: {self.__dict__}")


class BaseProduct(ABC, LogMixin):
    """Абстрактный класс, задающий обязательные методы для всех продуктов."""

    @abstractmethod
    def __add__(self, other):
        pass

    def __str__(self):
        pass


class Product(BaseProduct, LogMixin):
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
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price * self.quantity + other.price * other.quantity

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

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """Добавляет продукт в приватный список"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product и его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для вывода списка товаров"""
        return "\n".join([f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products])

    def __iter__(self):
        return CategoryIterator(self.__products)


class Smartphone(Product, LogMixin):
    """Класс для смартфонов."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product, LogMixin):
    """Класс для газонной травы."""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class CategoryIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __next__(self):
        if self.index < len(self.products):
            result = self.products[self.index]
            self.index += 1
            return result
        raise StopIteration

    def __iter__(self):
        return self
