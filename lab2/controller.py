import time
from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '7':
                break
            if choice == '5':
                self.process_search_option()
            elif choice in ['1', '2', '3', '4', '6']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Неправильний вибір. Спробуйте ще.")

    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()
            if table == '6':
                break
            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_update_option(table)
            elif choice == '3':
                self.process_view_option(table)
            elif choice == '4':
                self.process_delete_option(table)
            elif choice == '6':
                self.process_add_random_option(table)

    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nДодавання користувача:")
            self.add_user()
        elif table == '2':
            self.view.show_message("\nДодавання їжі:")
            self.add_food()
        elif table == '3':
            self.view.show_message("\nДодавання замовлення:")
            self.add_order()
        elif table == '4':
            self.view.show_message("\nДодавання доставки:")
            self.add_delivery()
        elif table == '5':
            self.view.show_message("\nДодавання зв'язку їжа-замовлення:")
            self.add_food_order()
        else:
            self.view.show_message("Неправильний вибір. Спробуйте ще.")

    def process_add_random_option(self, table):
        if table == '1':
            self.view.show_message("\nДодавання рандомізованих користувачів:")
            self.add_random_fields()
        else:
            self.view.show_message("Неправильний вибір. Спробуйте ще.")

    def process_view_option(self, table):
        if table == '1':
            self.view_users()
        elif table == '2':
            self.view_food()
        elif table == '3':
            self.view_orders()
        elif table == '4':
            self.view_deliveries()
        elif table == '5':
            self.view_food_orders()
        else:
            self.view.show_message("Неправильний вибір. Спробуйте ще.")

    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nОновлення користувача:")
            self.update_user()
        elif table == '2':
            self.view.show_message("\nОновлення їжі:")
            self.update_food()
        elif table == '3':
            self.view.show_message("\nОновлення замовлення:")
            self.update_order()
        elif table == '4':
            self.view.show_message("\nОновлення доставки:")
            self.update_delivery()
        elif table == '5':
            self.view.show_message("\nОновлення зв'язку їжа-замовлення:")
            self.update_food_order()
        else:
            self.view.show_message("Неправильний вибір. Спробуйте ще.")

    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nВидалення користувача:")
            self.delete_user()
        elif table == '2':
            self.view.show_message("\nВидалення їжі:")
            self.delete_food()
        elif table == '3':
            self.view.show_message("\nВидалення замовлення:")
            self.delete_order()
        elif table == '4':
            self.view.show_message("\nВидалення доставки:")
            self.delete_delivery()
        elif table == '5':
            self.view.show_message("\nВидалення зв'язку їжа-замовлення:")
            self.delete_food_order()
        else:
            self.view.show_message("Неправильний вибір. Спробуйте ще.")

    def add_user(self):
        try:
            user_id, name, email, phone = self.view.get_user_input()
            self.model.add_user(user_id, name, email, phone)
            self.view.show_message("Користувача успішно додано!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def add_food(self):
        try:
            food_id, name, price = self.view.get_food_input()
            self.model.add_food(food_id, name, price)
            self.view.show_message("Їжу успішно додано!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def add_order(self):
        try:
            order_id, order_date, user_id = self.view.get_order_input()
            self.model.add_order(order_id, order_date, user_id)
            self.view.show_message("Замовлення успішно додано!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def add_delivery(self):
        try:
            delivery_id, destination, status, order_id = self.view.get_delivery_input()
            self.model.add_delivery(delivery_id, destination, status, order_id)
            self.view.show_message("Доставку успішно додано!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def add_food_order(self):
        try:
            fo_id, food_id, order_id = self.view.get_food_order_input()
            self.model.add_food_order(fo_id, food_id, order_id)
            self.view.show_message("Зв'язок їжа-замовлення успішно додано!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def view_users(self):
        users = self.model.get_all_users()
        self.view.show_users(users)

    def view_food(self):
        food_items = self.model.get_all_foods()
        self.view.show_food(food_items)

    def view_orders(self):
        orders = self.model.get_all_orders()
        self.view.show_orders(orders)

    def view_deliveries(self):
        deliveries = self.model.get_all_deliveries()
        self.view.show_deliveries(deliveries)

    def view_food_orders(self):
        food_orders = self.model.get_all_food_orders()
        self.view.show_food_orders(food_orders)

    def update_user(self):
        try:
            user_id = self.view.get_id()
            name, email, phone = self.view.get_user_input(include_id=False)
            self.model.update_user(name, email, phone, user_id)
            self.view.show_message("Користувача успішно оновлено!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def update_food(self):
        try:
            food_id = self.view.get_id()
            name, price = self.view.get_food_input(include_id=False)
            self.model.update_food(name, price, food_id)
            self.view.show_message("Їжу успішно оновлено!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def update_order(self):
        try:
            order_id = self.view.get_id()
            order_date, user_id = self.view.get_order_input(include_id=False)
            self.model.update_order(order_date, user_id, order_id)
            self.view.show_message("Замовлення успішно оновлено!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def update_delivery(self):
        try:
            delivery_id = self.view.get_id()
            destination, status, order_id = self.view.get_delivery_input(include_id=False)
            self.model.update_delivery(destination, status, order_id, delivery_id)
            self.view.show_message("Доставку успішно оновлено!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def update_food_order(self):
        try:
            fo_id = self.view.get_id()
            food_id, order_id = self.view.get_food_order_input(include_id=False)
            self.model.update_food_order(food_id, order_id, fo_id)
            self.view.show_message("Зв'язок їжа-замовлення успішно оновлено!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def delete_user(self):
        try:
            user_id = self.view.get_id()
            self.model.delete_user(user_id)
            self.view.show_message("Користувача успішно видалено!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def delete_food(self):
        try:
            food_id = self.view.get_id()
            self.model.delete_food(food_id)
            self.view.show_message("Їжу успішно видалено!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def delete_order(self):
        try:
            order_id = self.view.get_id()
            self.model.delete_order(order_id)
            self.view.show_message("Замовлення успішно видалено!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def delete_delivery(self):
        try:
            delivery_id = self.view.get_id()
            self.model.delete_delivery(delivery_id)
            self.view.show_message("Доставку успішно видалено!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def delete_food_order(self):
        try:
            fo_id = self.view.get_id()
            self.model.delete_food_order(fo_id)
            self.view.show_message("Зв'язок їжа-замовлення успішно видалено!")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def add_random_fields(self):
      try:
          num_users = self.view.get_number()
          self.model.add_random_fields(num_users)
          self.view.show_message(f"{num_users} рандомізованих користувачів було успішно додано!")
      except Exception as e:
          self.view.show_message(f"Щось пішло не так: {e}")

#Search
    def process_search_option(self):
        option = self.view.show_search()
        if option == '1':
            self.show_users_by_name_initial()
        elif option == '2':
            self.show_user_orders()
        elif option == '3':
            self.show_orders_count_by_date_and_status()
        else:
            self.view.show_message("Недійсний вибір, назад до меню")
            return

    def show_users_by_name_initial(self):
        try:
            initial = self.view.get_name_initial_input()
            start_time = time.time()
            users = self.model.get_users_by_name_initial(initial)
            self.view.show_users_by_name_initial(users)
            elapsed_time = (time.time() - start_time) * 1000
            print(f"Час виконання запиту: {elapsed_time:.2f} мс")
        except Exception as e:
            self.view.show_message(f"Помилка: {e}")

    def show_user_orders(self):
        try:
            user_id = self.view.get_id()
            start_date = input("Введіть початкову дату (YYYY-MM-DD): ")
            end_date = input("Введіть кінцеву дату (YYYY-MM-DD): ")
            start_time = time.time()
            orders = self.model.get_orders_by_user(user_id, start_date, end_date)
            if orders:
                self.view.show_orders_with_status(orders)
                elapsed_time = (time.time() - start_time) * 1000
                print(f"Час виконання запиту: {elapsed_time:.2f} мс")
            else:
                self.view.show_message("Не знайдено замовлень для цього клієнта у вказаний період.")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_orders_count_by_date_and_status(self):
        try:
            delivery_status, start_date, end_date = self.view.get_status_and_date_input()
            start_time = time.time()
            orders_count = self.model.get_orders_count_by_date_and_status(delivery_status, start_date, end_date)
            if orders_count:
                self.view.show_orders_count_by_date(orders_count)
                elapsed_time = (time.time() - start_time) * 1000
                print(f"Час виконання запиту: {elapsed_time:.2f} мс")
            else:
                self.view.show_message("Не знайдено замовлень з таким статусом у вказаний період.")
        except Exception as e:
            self.view.show_message(f"Помилка: {e}")

