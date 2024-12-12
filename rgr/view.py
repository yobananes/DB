from datetime import datetime

class View:

    def show_menu(self):
        self.show_message("\nМеню:")
        self.show_message("1. Додати рядок")
        self.show_message('2. Редагувати рядок')
        self.show_message("3. Показати таблицю")
        self.show_message("4. Видалити рядок")
        self.show_message("5. Пошук")
        self.show_message('6. Генерувати рандомізовані дані (тільки для таблиці "User")')
        self.show_message("7. Вихід")
        return input("Виберіть пункт: ")

    def show_tables(self):
        self.show_message("\nТаблиці:")
        self.show_message("1. User (Користувач)")
        self.show_message("2. Food (Їжа)")
        self.show_message("3. Order (Замовлення)")
        self.show_message("4. Delivery (Доставка)")
        self.show_message("5. Food_Order (Їжа-замовлення)")
        self.show_message("6. Повернутися до меню")
        return input("Оберіть потрібну таблицю: ")

    def show_users(self, users):
        print("\nUsers:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Phone: {user[3]}")

    def show_food(self, food_items):
        print("\nFood:")
        for food in food_items:
            print(f"ID: {food[0]}, Name: {food[1]}, Price: {food[2]}")

    def show_orders(self, orders):
        print("\nOrders:")
        for order in orders:
            print(f"ID: {order[0]}, Date: {order[1]}, User ID: {order[2]}")

    def show_deliveries(self, deliveries):
        print("\nDeliveries:")
        for delivery in deliveries:
            print(f"ID: {delivery[0]}, Destination: {delivery[1]}, Status: {delivery[2]}, Order ID: {delivery[3]}")

    def show_food_orders(self, food_orders):
        print("\nFood Orders:")
        for food_order in food_orders:
            print(f"ID: {food_order[0]}, Food ID: {food_order[1]}, Order ID: {food_order[2]}")

    def get_user_input(self, include_id=True):
        if include_id:
            user_id = input("Введіть ID Користувача: ")
        else:
            user_id = None
        while True:
            name = input("Введіть ім'я користувача: ")
            if name.strip():
                break
            else:
                print("Ім'я не може бути порожнім.")
        while True:
            email = input("Введіть пошту користувача: ")
            if email.strip():
                break
            else:
                print("Пошта не може бути порожньою.")
        while True:
            phone = input("Введіть номер телефону користувача: ")
            if phone.strip():
                break
            else:
                print("Номер телефону не може бути порожнім.")
        return (user_id, name, email, phone) if include_id else (name, email, phone)

    def get_food_input(self, include_id=True):
        if include_id:
            food_id = input("Введіть ID Їжі: ")
        else:
            food_id = None
        while True:
            name = input("Введіть назву іжі: ")
            if name.strip():
                break
            else:
                print("Назва не може бути порожньою.")
        while True:
            try:
                price = int(input("Введіть ціну: "))
                break
            except ValueError:
                print("Ціна повинна бути числом.")
        return (food_id, name, price) if include_id else (name, price)

    def get_order_input(self, include_id=True):
        if include_id:
            order_id = input("Введіть ID Замовлення: ")
        else:
            order_id = None
        while True:
            try:
                date = input("Введіть дату (YYYY-MM-DD): ")
                date = datetime.strptime(date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Недійсний формат дати. Введіть дату у форматі (YYYY-MM-DD).")
        while True:
            try:
                user_id = int(input("Введіть ID користувача: "))
                break
            except ValueError:
                print("ID користувача повинно бути числом.")
        return (order_id, date, user_id) if include_id else (date, user_id)

    def get_delivery_input(self, include_id=True):
        if include_id:
            delivery_id = input("Введіть ID Доставки: ")
        else:
            delivery_id = None
        while True:
            destination = input("Введіть пункт призначення: ")
            if destination.strip():
                break
            else:
                print("Пункт призначення не може бути порожнім.")
        while True:
            status = input("Введіть статус (Збирається, В дорозі, Доставлено, Скасовано): ")
            if status.strip():
                break
            else:
                print("Статус не може бути порожнім.")
        while True:
            try:
                order_id = int(input("Введіть ID замовлення: "))
                break
            except ValueError:
                print("ID замовлення повинно бути числом.")
        return (delivery_id, destination, status, order_id) if include_id else (destination, status, order_id)

    def get_food_order_input(self, include_id=True):
        if include_id:
            fo_id = input("Введіть ID Їжа_Замовлення: ")
        else:
            fo_id = None
        while True:
            try:
                food_id = int(input("Введіть ID Їжі: "))
                break
            except ValueError:
                print("ID їжі повинно бути числом.")
        while True:
            try:
                order_id = int(input("Введіть ID Замовлення: "))
                break
            except ValueError:
                print("ID замовлення повинно бути числом.")
        return (fo_id, food_id, order_id) if include_id else (food_id, order_id)

    def get_id(self):
        while True:
            try:
                id = int(input("Введіть ID: "))
                break
            except ValueError:
                print("Це повинно бути число.")
        return id

    def show_message(self, message):
        print(message)

    def get_number(self):
        while True:
            try:
                number = int(input("Введіть число: "))
                break
            except ValueError:
                print("Це повинно бути число.")
        return number
#Search
    def show_search(self):
        self.show_message("\nПошук:")
        self.show_message("1. Користувачі за початковою літерою імені")
        self.show_message("2. Замовлення користувача за проміжок часу")
        self.show_message("3. Доставки за статусом і датою")
        self.show_message("4. Повернутися до меню")
        choice = input("Оберіть щось: ")
        return choice

    def get_name_initial_input(self):
        initial = input("Введіть початкову літеру імені користувача: ")
        return initial

    def show_users_by_name_initial(self, users):
        print("\nКористувачі за початковою літерою імені:")
        for customer_name, email in users:
            print(f"Ім'я: {customer_name}, Пошта: {email}")

    def get_user_search_input(self):
        user_id = int(input("Введіть ID користувача: "))
        start_date = input("Введіть початкову дату (YYYY-MM-DD): ")
        end_date = input("Введіть кінцеву дату (YYYY-MM-DD): ")
        return user_id, start_date, end_date

    def show_orders_with_status(self, orders):
        print("\nЗамовлення клієнта за проміжок часу:")
        for order in orders:
            order_id, order_date, customer_name, delivery_status = order
            print(f"ID замовлення: {order_id}, Дата: {order_date}, Клієнт: {customer_name}, Статус: {delivery_status}")

    def get_status_and_date_input(self):
        delivery_status = input("Введіть статус доставки (наприклад, 'В дорозі', 'Доставлено'): ")
        start_date = input("Введіть початкову дату (YYYY-MM-DD): ")
        end_date = input("Введіть кінцеву дату (YYYY-MM-DD): ")
        return delivery_status, start_date, end_date

    def show_orders_count_by_date(self, orders_count):
        print("\nКількість замовлень за датами та статусом:")
        for order_date, delivery_status, order_count in orders_count:
            print(f"Дата: {order_date}, Статус: {delivery_status}, Кількість замовлень: {order_count}")




