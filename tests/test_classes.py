import pytest

from src.classes import Category, Product, Smartphone, LawnGrass


def test_product_init():
    """Тест инициализации продукта"""
    product = Product("Test Book", "A book for testing", 100.50, 10)
    assert product.name == "Test Book"
    assert product.description == "A book for testing"
    assert product.price == 100.50
    assert product.quantity == 10


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового продукта"""
    return Product("Sample", "Sample desc", 10.0, 1)


@pytest.fixture
def sample_category(sample_product):
    """Фикстура для создания тестовой категории"""
    Category.category_count = 0
    Category.product_count = 0
    return Category("Samples", "Sample category", [sample_product, sample_product])


def test_category_init(sample_category, sample_product):
    """Тест инициализации категории"""
    assert sample_category.name == "Samples"
    assert sample_category.description == "Sample category"

    products_list = sample_category.products.split("\n")
    assert len(products_list) == 2

    expected_product_str = f"{sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity} шт."
    for product_str in products_list:
        assert product_str == expected_product_str


def test_private_products():
    category = Category("Test", "Test", [])
    category.add_product(Product("Test", "Test", 100, 5))
    assert "Test, 100 руб. Остаток: 5 шт." in category.products


def test_price_setter():
    product = Product("Test", "Test", 100, 5)
    product.price = -50  # Должно вызвать предупреждение
    assert product.price == 100
    product.price = 200
    assert product.price == 200


def test_category_counts(sample_category):
    """Тест счетчиков категорий и продуктов"""

    assert Category.category_count == 1
    assert Category.product_count == 2

    product3 = Product("Another", "Desc", 5.0, 5)
    category2 = Category("Another Cat", "Desc cat", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_new_product_with_duplicate():
    """Тест создания продукта с дубликатом (объединение количества и цены)"""
    # Создаем существующий продукт
    existing_product = Product("Test", "Desc", 100, 5)
    products_list = [existing_product]

    # Данные для нового продукта-дубликата
    new_data = {"name": "Test", "description": "New Desc", "price": 150, "quantity": 3}

    # Создаем "дубликат" через new_product
    result = Product.new_product(new_data, products_list)

    # Проверяем, что это тот же объект
    assert result is existing_product
    assert result.quantity == 8  # 5 + 3
    assert result.price == 150  # Новая цена выше


def test_new_product_without_duplicate():
    """Тест создания нового продукта"""
    new_data = {"name": "New", "description": "Desc", "price": 200, "quantity": 10}
    product = Product.new_product(new_data)
    assert product.name == "New"
    assert product.price == 200


def test_product_str():
    p = Product("Test", "Test desc", 100, 3)
    assert str(p) == "Test, 100 руб. Остаток: 3 шт."


def test_category_str():
    p1 = Product("A", "desc", 100, 2)
    p2 = Product("B", "desc", 200, 3)
    cat = Category("Test Cat", "desc", [p1, p2])
    assert str(cat) == "Test Cat, количество продуктов: 5 шт."


def test_add_products():
    p1 = Product("A", "desc", 100, 2)
    p2 = Product("B", "desc", 200, 3)
    result = p1 + p2
    assert result == 100 * 2 + 200 * 3


def test_category_iteration():
    p1 = Product("A", "desc", 100, 2)
    p2 = Product("B", "desc", 200, 3)
    cat = Category("Phones", "desc", [p1, p2])
    names = [p.name for p in cat]
    assert names == ["A", "B"]

def test_smartphone_init():
    smartphone = Smartphone(
        "iPhone", "Desc", 100000, 5, "High", "15 Pro", 512, "Black"
    )
    assert smartphone.name == "iPhone"
    assert smartphone.efficiency == "High"
    assert isinstance(smartphone, Product)

def test_lawn_grass_init():
    grass = LawnGrass(
        "Grass", "Desc", 500, 10, "Russia", "7 дней", "Green"
    )
    assert grass.country == "Russia"
    assert isinstance(grass, Product)

def test_add_same_class():
    p1 = Smartphone("A", "Desc", 100, 2, "High", "X", 128, "Black")
    p2 = Smartphone("B", "Desc", 200, 3, "Mid", "Y", 256, "White")
    assert p1 + p2 == 100*2 + 200*3

def test_add_different_classes():
    p1 = Smartphone("A", "Desc", 100, 2, "High", "X", 128, "Black")
    p2 = LawnGrass("B", "Desc", 200, 3, "USA", "5 дней", "Green")
    with pytest.raises(TypeError):
        p1 + p2

def test_add_non_product_to_category():
    category = Category("Test", "Test", [])
    with pytest.raises(TypeError):
        category.add_product("Not a product")