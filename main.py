import json
from src.classes import Product, Category

def load_data_from_json(filepath="products.json"):
    """
    Загружает данные из JSON-файла и создает объекты Category и Product.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products_in_category = []
        for product_data in category_data.get("products", []):
            product = Product(
                name=product_data.get("name"),
                description=product_data.get("description"),
                price=float(product_data.get("price")),
                quantity=int(product_data.get("quantity"))
            )
            products_in_category.append(product)

        category = Category(
            name=category_data.get("name"),
            description=category_data.get("description"),
            products=products_in_category
        )
        categories.append(category)

    return categories

if __name__ == "__main__":
    print("\n--- Загрузка данных из JSON ---")

    loaded_categories = load_data_from_json("products.json")

    print(f"\nЗагружено категорий из файла: {len(loaded_categories)}")
    for cat in loaded_categories:
        print(f"Категория: {cat.name}. Товаров: {len(cat.products)}")
        for prod in cat.products:
            print(f"  - {prod.name} ({prod.price} руб.)")

    print("\n--- Итоговые значения счетчиков ---")
    print(f"\nВсего категорий создано: {Category.category_count}")
    print(f"Всего уникальных товаров во всех категориях: {Category.product_count}")