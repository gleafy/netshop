# Ядро интернет-магазина

Базовые классы для управления товарами и категориями.

## Основной функционал
- Класс `Product`: название, описание, цена, количество.
- Класс `Category`: название, описание, список товаров.
- Автоподсчет: 
  - Всего категорий (`Category.category_count`)
  - Всего товаров (`Category.product_count`)
- Загрузка данных из JSON (`products.json`)

## Пример использования
```python
from src.classes import Product, Category

# Создание товара
product = Product("Ноутбук", "Игровой", 150000, 3)

# Создание категории
category = Category("Техника", "Электроника", [product])

print(f"Категорий: {Category.category_count}, Товаров: {Category.product_count}")
```

## Запуск тестов
```bash
pytest tests/
```