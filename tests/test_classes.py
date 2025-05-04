import pytest

from src.classes import Category, Product


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
    assert len(sample_category.products) == 2
    assert sample_category.products[0] == sample_product


def test_category_counts(sample_category):
    """Тест счетчиков категорий и продуктов"""

    assert Category.category_count == 1
    assert Category.product_count == 2

    product3 = Product("Another", "Desc", 5.0, 5)
    category2 = Category("Another Cat", "Desc cat", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3
