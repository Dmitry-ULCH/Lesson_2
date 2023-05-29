from statistics import mean
from rich import print


def count_sales(products):
    total_items_sold = []
    for position, phone in enumerate(products, start=1):
        total_sales = f"Суммарное количество продаж: {sum(phone['items_sold'])}"
        average_sales = f"Среднее количество продаж: {round(mean(phone['items_sold']), 2)}"
        total_items_sold += phone['items_sold']
        print(f"[underline]{phone['product']}[/underline]", total_sales, average_sales, sep='\n')
        if position != len(products):
            print("---")
        else:
            print("===")
    print(f"Суммарное количество продаж всех товаров: {sum(total_items_sold)}")
    print(f"Среднее количество продаж всех товаров: {round(mean(total_items_sold), 2)}")


def main():
    phone_sales = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    count_sales(phone_sales)


if __name__ == "__main__":
    main()
