import time
import psycopg2
import random


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='Food',
            user='postgres',
            password='2535',
            host='localhost',
            port=5432
        )
# Таблиця User
    def add_user(self, user_id, name, email, phone):
        c = self.conn.cursor()
        c.execute('INSERT INTO "User" ("user_id", "name", "email", "phone") VALUES (%s, %s, %s, %s)',
                  (user_id, name, email, phone))
        self.conn.commit()

    def get_all_users(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "User" ORDER BY user_id ASC')
            return cursor.fetchall()

    def update_user(self, name, email, phone, id):
        c = self.conn.cursor()
        c.execute('UPDATE "User" SET "name"=%s, "email"=%s, "phone"=%s WHERE "user_id"=%s',
                  (name, email, phone, id))
        self.conn.commit()

    def delete_user(self, user_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "User" WHERE "user_id"=%s', (user_id,))
        self.conn.commit()
#Таблиця Food
    def add_food(self, food_id, name, price):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Food" ("food_id", "name", "price") VALUES (%s, %s, %s)',
                  (food_id, name, price))
        self.conn.commit()

    def get_all_foods(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "Food" ORDER BY food_id ASC')
            return cursor.fetchall()

    def update_food(self, name, price, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Food" SET "name"=%s, "price"=%s WHERE "food_id"=%s',
                  (name, price, id))
        self.conn.commit()

    def delete_food(self, food_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Food" WHERE "food_id"=%s', (food_id,))
        self.conn.commit()

#Таблиця Order
    def add_order(self, order_id, order_date, user_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Order" ("order_id", "order_date", "user_id") VALUES (%s, %s, %s)',
                  (order_id, order_date, user_id))
        self.conn.commit()

    def get_all_orders(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "Order" ORDER BY order_id ASC')
            return cursor.fetchall()

    def update_order(self, order_date, user_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Order" SET "order_date"=%s, "user_id"=%s WHERE "order_id"=%s',
                  (order_date, user_id, id))
        self.conn.commit()

    def delete_order(self, order_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Order" WHERE "order_id"=%s', (order_id,))
        self.conn.commit()

#Таблиця Delivery
    def add_delivery(self, delivery_id, destination, status, order_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Delivery" ("delivery_id", "destination", "status", "order_id") VALUES (%s, %s, %s, %s)',
                  (delivery_id, destination, status, order_id))
        self.conn.commit()

    def get_all_deliveries(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "Delivery" ORDER BY delivery_id ASC')
            return cursor.fetchall()

    def update_delivery(self, destination, status, order_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Delivery" SET "destination"=%s, "status"=%s,"order_id"=%s WHERE "delivery_id"=%s',
                  (destination, status, order_id, id))
        self.conn.commit()

    def delete_delivery(self, delivery_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Delivery" WHERE "delivery_id"=%s', (delivery_id,))
        self.conn.commit()

#Таблиця Food_Order
    def add_food_order(self, fo_id, food_id, order_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Food_Order" ("fo_id","food_id", "order_id") VALUES (%s, %s,%s)',
                  (fo_id, food_id, order_id))
        self.conn.commit()

    def get_all_food_orders(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "Food_Order" ORDER BY fo_id ASC')
            return cursor.fetchall()

    def update_food_order(self, food_id, order_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Food_Order" SET "food_id"=%s,"order_id"=%s WHERE "fo_id"=%s',
                  (food_id, order_id, id))
        self.conn.commit()

    def delete_food_order(self, fo_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Food_Order" WHERE "fo_id"=%s', (fo_id,))
        self.conn.commit()

#Random

    def add_random_fields(self, number):
        c = self.conn.cursor()
        first_names = ['Andriy', 'Olena', 'Bohdan', 'Iryna', 'Oleksiy', 'Mariya', 'Sofiya', 'Viktoriya',
          'Ivan', 'Nataliya', 'Alina', 'Rostyslav', 'Vadym', 'Vira', 'Maksym', 'Oksana','Liubov', 'Yevhen', 'Liliya',
          'Yuriy', 'Kateryna', 'Dmytro', 'Anna', 'Mykhailo', 'Tetyana', 'Oleh', 'Liudmyla', 'Vasyl',
          'Serhiy', 'Vladyslav', 'Yevgeniya', 'Oleksandr', 'Daryna', 'Illia', 'Svitlana',
          'Pavlo', 'Valeriya', 'Larysa', 'Artem', 'Inna', 'Roman', 'Zoryana', 'Stepan',
          'Hanna', 'Taras', 'Veronika', 'Yuliya', 'Kyrylo', 'Yaroslava', 'Hryhoriy'
                    ]
        last_names = ['Shevchenko', 'Kovalenko', 'Bondarenko', 'Melnyk', 'Kravchenko', 'Oliynyk', 'Tkachenko',
          'Petrenko', 'Kalinychenko', 'Rudenko', 'Tymoshenko', 'Chernenko', 'Klymenko',
          'Savchenko', 'Kuzmenko', 'Sydoenko', 'Lysenko', 'Havrylyuk', 'Demchenko', 'Moroz',
          'Zakharchenko', 'Martynyuk', 'Ivanchenko', 'Honcharenko', 'Bondar', 'Rybak',
          'Kravchuk', 'Hrytsenko', 'Shapoval', 'Yakovlenko', 'Onyshchenko', 'Pavlenko',
          'Solovey', 'Skrypnyk', 'Levchenko', 'Bilan', 'Palamarchuk', 'Korol', 'Kulish'
                      ]

        query = '''
            WITH max_id AS (SELECT COALESCE(MAX("user_id"), 0) FROM public."User")
            INSERT INTO public."User" ("user_id", "name", "email", "phone")
            SELECT 
                (SELECT * FROM max_id) + row_number() OVER () AS "user_id",
                CONCAT_WS(' ', first_name, last_name) AS "name",
                LOWER(first_name || '.' || last_name) || '@' ||
                (CASE (random() * 10)::integer
                    WHEN 0 THEN 'gmail'
                    WHEN 1 THEN 'ukr'
                    WHEN 2 THEN 'yahoo'
                    WHEN 3 THEN 'llkpi'
                    WHEN 4 THEN 'ua'
                    WHEN 5 THEN 'outlook'
                    WHEN 6 THEN 'hotmail'
                    WHEN 7 THEN 'evite'
                    WHEN 8 THEN 'mailchi'
                    WHEN 9 THEN 'odido'
                    WHEN 10 THEN 'gmx'
                END) || '.com' AS "email",
                CONCAT('+1', (1000000000 + floor(random() * 9000000000)::bigint)::text) AS "phone"
            FROM (SELECT 
                      unnest(ARRAY[%s]) AS first_name, 
                      unnest(ARRAY[%s]) AS last_name
                  LIMIT %s) AS names;
        '''

        first_names_sample = [random.choice(first_names) for _ in range(number)]
        last_names_sample = [random.choice(last_names) for _ in range(number)]
        c.execute(query, (first_names_sample, last_names_sample, number))

#Search
    def get_users_by_name_initial(self, initial):
        with self.conn.cursor() as cursor:
            query = """
                SELECT u.name, u.email
                FROM "User" u
                WHERE u.name LIKE %s
                ORDER BY u.name;
            """
            cursor.execute(query, (initial + '%',))
            result = cursor.fetchall()
            return result

    def get_orders_by_user(self, user_id, start_date, end_date):
        with self.conn.cursor() as cursor:
            query = '''
                SELECT o.order_id, o.order_date, u.name AS user_name, d.status
                FROM "Order" o
                JOIN "User" u ON o.user_id = u.user_id
                LEFT JOIN "Delivery" d ON o.order_id = d.order_id
                WHERE o.user_id = %s AND o.order_date BETWEEN %s AND %s
                ORDER BY o.order_date;
            '''
            cursor.execute(query, (user_id, start_date, end_date))
            result = cursor.fetchall()
            return result

    def get_orders_count_by_date_and_status(self, delivery_status, start_date, end_date):
     with self.conn.cursor() as cursor:
        query = """
              SELECT o.order_date, d.status, COUNT(*) AS order_count
              FROM "Order" o
              JOIN "Delivery" d ON o.order_id = d.order_id
              WHERE d.status = %s AND o.order_date BETWEEN %s AND %s
              GROUP BY o.order_date, d.status
              ORDER BY o.order_date;
            """
        cursor.execute(query, (delivery_status, start_date, end_date))
        result = cursor.fetchall()
        return result













