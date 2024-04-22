import json

# DataBase
def load_finances():
    try:
        with open('finances.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'income': 0, 'expenses': 0, 'balance': 0}

# Save
def save_finances(finances):
    with open('finances.json', 'w') as file:
        json.dump(finances, file)

# Add income
def add_income(finances):
    amount = float(input("Введите сумму дохода: "))
    finances['income'] += amount
    finances['balance'] += amount
    print("Доход добавлен.")

# Add consumption
def add_expense(finances):
    amount = float(input("Введите сумму расхода: "))
    finances['expenses'] += amount
    finances['balance'] -= amount
    print("Расход добавлен.")

# data
def display_finances(finances):
    print("Финансовый отчет:")
    print(f"Доход: {finances['income']}")
    print(f"Расход: {finances['expenses']}")
    print(f"Баланс: {finances['balance']}")

# Main
def main():
    finances = load_finances()

    while True:
        print("\nМеню:")
        print("1. Добавить доход")
        print("2. Добавить расход")
        print("3. Просмотреть финансовый отчет")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_income(finances)
        elif choice == '2':
            add_expense(finances)
        elif choice == '3':
            display_finances(finances)
        elif choice == '4':
            save_finances(finances)
            print("Данные сохранены. Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
