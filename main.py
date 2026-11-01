#Робота з текстом. Напишіть функцію,
# яка приймає рядок як вхідні дані та повертає словник, де ключі - це унікальні слова
# в рядку, а значення - кількість їх появ.Створіть та виведіть на екран список, де
# зберігаються слова, що зустрічаються більше 3 разів.

import string
def get_word_frequencies(text):
    # Видаляємо пунктуацію та переводимо текст у нижній регістр
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = cleaned_text.split()

    # Створюємо словник частот
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


# Тестовий текст для перевірки
sample_text = """
Слово, слово, слово, слово. 
Код код код код код. 
Тест тест.
"""

# Отримуємо словник з частотою слів
word_counts = get_word_frequencies(sample_text)

# Створюємо список слів, які зустрічаються більше 3 разів
frequent_words = [word for word, count in word_counts.items() if count > 3]

# Виводимо результати
print("Словник частот слів:")
print(word_counts)
print("\nСлова, що зустрічаються більше 3 разів:")
print(frequent_words)

#Інвентаризація продуктів. Створіть словник, де ключі - це назви продуктів,
# а значення - їх кількість на складі. Напишіть функцію, яка приймає назву
# продукту та кількість, і оновлює словник відповідно до додавання або видалення
# продуктів. Додатково: створіть список продуктів, в яких кількість менше ніж 5.
# 1. Словник з початковою кількістю продуктів

inventory = {
    "яблука": 10,
    "молоко": 3,
    "хліб": 15,
    "сир": 2
}


# 2. Функція для оновлення (додавання або видалення)
def update_inventory(product, amount):
    if product in inventory:
        inventory[product] += amount
    else:
        inventory[product] = amount

    # Запобігаємо появі від'ємної кількості на складі
    if inventory[product] < 0:
        inventory[product] = 0


# Тестуємо роботу функції
update_inventory("яблука", -4)  # Видаляємо 4 яблука
update_inventory("банани", 7)  # Додаємо новий продукт
update_inventory("молоко", 1)  # Додаємо 1 молоко

print("Склад після оновлення:", inventory)

# 3. Створення списку продуктів, яких менше ніж 5
low_stock = [product for product, quantity in inventory.items() if quantity < 5]

print("Продукти, що закінчуються:", low_stock)


#Статистика продажів. Створіть список словників, де кожен словник
# представляє продаж з ключами: "продукт", "кількість", "ціна".
# Напишіть функцію, яка обчислює загальний дохід для кожного продукту
# та повертає словник, де ключі - це назви продуктів, а значення - загальний дохід.
# Створіть список продуктів, що принесли дохід більший ніж 1000.

# 1. Список словників, що представляє статистику продажів
sales = [
    {"продукт": "телефон", "кількість": 2, "ціна": 800},
    {"продукт": "ноутбук", "кількість": 1, "ціна": 1500},
    {"продукт": "навушники", "кількість": 5, "ціна": 50},
    {"продукт": "телефон", "кількість": 1, "ціна": 800},
    {"продукт": "планшет", "кількість": 3, "ціна": 400}
]


# 2. Функція для обчислення загального доходу для кожного продукту
def calculate_revenue(sales_data):
    revenue_dict = {}
    for item in sales_data:
        product = item["продукт"]
        # Обчислюємо дохід з конкретного продажу
        revenue = item["кількість"] * item["ціна"]

        # Якщо продукт вже є у словнику, додаємо дохід до існуючого
        if product in revenue_dict:
            revenue_dict[product] += revenue
        else:
            # Якщо немає - створюємо новий запис
            revenue_dict[product] = revenue

    return revenue_dict


# Викликаємо функцію та виводимо результат
product_revenues = calculate_revenue(sales)
print("Дохід по кожному продукту:\n", product_revenues)

# 3. Створення списку продуктів, що принесли дохід більший ніж 1000
top_products = [product for product, revenue in product_revenues.items() if revenue > 1000]

print("\nПродукти з доходом більшим ніж 1000:\n", top_products)

#Система управління задачами.
# Створіть словник, де ключі - це назви задач, а значення
# - їх статус ("виконано", "в процесі", "очікує"). Напишіть
# функції для додавання, видалення та зміни статусу задач. Додатково:
# створіть список задач, які мають статус "очікує".
# Словник із задачами та їхніми статусами
tasks = {
    "Зробити домашнє завдання": "виконано",
    "Написати код": "в процесі",
    "Прочитати книгу": "очікує",
    "Прибрати кімнату": "очікує"
}

# Функція для додавання задачі
def add_task(task_name, status="очікує"):
    if task_name not in tasks:
        tasks[task_name] = status
    else:
        print(f"Задача '{task_name}' вже існує.")

# Функція для видалення задачі
def remove_task(task_name):
    if task_name in tasks:
        del tasks[task_name]
    else:
        print(f"Задачу '{task_name}' не знайдено.")

# Функція для зміни статусу задачі
def change_status(task_name, new_status):
    if task_name in tasks:
        tasks[task_name] = new_status
    else:
        print(f"Задачу '{task_name}' не знайдено.")

# Викликаємо функції для перевірки
add_task("Купити продукти")
remove_task("Зробити домашнє завдання")
change_status("Написати код", "виконано")

print("Оновлений словник задач:\n", tasks)

# Створюємо список задач, які мають статус "очікує"
pending_tasks = [task for task, status in tasks.items() if status == "очікує"]

print("\nЗадачі зі статусом 'очікує':\n", pending_tasks)

#Аутентифікація користувачів.
# Створіть словник в якому зберігаються ім'я користувача(login),
# зашифрований пароль та повне ПІБ користувача. Для хешування пароля
# використовуйте функцію hashlib.md5(). Зробіть функцію перевірки введеного паролю користувача;
# пароль користувач вводить з консолі, зчитування за допомогою методу input()
import hashlib

# 1. Словник користувачів
# Паролі попередньо захешовані алгоритмом MD5
# (для 'user1' пароль 'qwerty', для 'admin' пароль 'admin123')
users_db = {
    "student": {
        "password_hash": hashlib.md5("qwerty".encode()).hexdigest(),
        "fullname": "Вероніка Романівна"
    },
    "admin": {
        "password_hash": hashlib.md5("admin123".encode()).hexdigest(),
        "fullname": " Дмитро Володиморович "
    }
}


# 2. Функція перевірки введеного паролю
def verify_user():
    login = input("Введіть логін: ")

    if login not in users_db:
        print("Помилка: Користувача з таким логіном не існує.")
        return

    password = input("Введіть пароль: ")

    # Хешуємо введений пароль, щоб порівняти його з тим, що у базі
    entered_hash = hashlib.md5(password.encode()).hexdigest()

    # Перевірка збігу хешів
    if entered_hash == users_db[login]["password_hash"]:
        full_name = users_db[login]["fullname"]
        print(f"\nУспішна авторизація! Вітаємо, {full_name}.")
    else:
        print("\nПомилка: Невірний пароль. Спробуйте ще раз.")


# Виклик функції
verify_user()

