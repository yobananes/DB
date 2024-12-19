from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# --- Оголошення сутностей ---

class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    orders = relationship('Order', back_populates='user', cascade="all, delete-orphan")


class Food(Base):
    __tablename__ = 'Food'
    food_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)


class Order(Base):
    __tablename__ = 'Order'
    order_id = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('User.user_id', ondelete='CASCADE'))
    user = relationship('User', back_populates='orders')
    deliveries = relationship('Delivery', back_populates='order', cascade="all, delete-orphan")
    food_orders = relationship('FoodOrder', back_populates='order', cascade="all, delete-orphan")


class Delivery(Base):
    __tablename__ = 'Delivery'
    delivery_id = Column(Integer, primary_key=True)
    destination = Column(String, nullable=False)
    status = Column(String, nullable=False)
    order_id = Column(Integer, ForeignKey('Order.order_id', ondelete='CASCADE'))
    order = relationship('Order', back_populates='deliveries')


class FoodOrder(Base):
    __tablename__ = 'Food_Order'
    fo_id = Column(Integer, primary_key=True)
    food_id = Column(Integer, ForeignKey('Food.food_id', ondelete='CASCADE'))
    order_id = Column(Integer, ForeignKey('Order.order_id', ondelete='CASCADE'))
    food = relationship('Food')
    order = relationship('Order', back_populates='food_orders')


# --- Основний клас для роботи з БД ---

class Model:
    def __init__(self):
        engine_url = 'postgresql+psycopg2://postgres:2535@localhost:5432/Food'
        self.engine = create_engine(engine_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    # --- Методи для таблиці User ---
    def add_user(self, user_id, name, email, phone):
        with self.Session() as session:
            user = User(user_id=user_id, name=name, email=email, phone=phone)
            session.add(user)
            session.commit()

    def update_user(self, name, email, phone, user_id):
        with self.Session() as session:
            user = session.query(User).filter_by(user_id=user_id).first()
            if user:
                user.name = name
                user.email = email
                user.phone = phone
                session.commit()

    def delete_user(self, user_id):
        with self.Session() as session:
            user = session.query(User).filter_by(user_id=user_id).first()
            if user:
                session.delete(user)
                session.commit()

    # --- Методи для таблиці Food ---
    def add_food(self, food_id, name, price):
        with self.Session() as session:
            food = Food(food_id=food_id, name=name, price=price)
            session.add(food)
            session.commit()

    def update_food(self, name, price, food_id):
        with self.Session() as session:
            food = session.query(Food).filter_by(food_id=food_id).first()
            if food:
                food.name = name
                food.price = price
                session.commit()

    def delete_food(self, food_id):
        with self.Session() as session:
            food = session.query(Food).filter_by(food_id=food_id).first()
            if food:
                session.delete(food)
                session.commit()

    # --- Методи для таблиці Order ---
    def add_order(self, order_id, order_date, user_id):
        with self.Session() as session:
            order = Order(order_id=order_id, order_date=order_date, user_id=user_id)
            session.add(order)
            session.commit()

    def update_order(self, order_date, user_id, order_id):
        with self.Session() as session:
            order = session.query(Order).filter_by(order_id=order_id).first()
            if order:
                order.order_date = order_date
                order.user_id = user_id
                session.commit()

    def delete_order(self, order_id):
        with self.Session() as session:
            order = session.query(Order).filter_by(order_id=order_id).first()
            if order:
                session.delete(order)
                session.commit()

    # --- Методи для таблиці Delivery ---
    def add_delivery(self, delivery_id, destination, status, order_id):
        with self.Session() as session:
            delivery = Delivery(delivery_id=delivery_id, destination=destination, status=status, order_id=order_id)
            session.add(delivery)
            session.commit()

    def update_delivery(self, destination, status, order_id, delivery_id):
        with self.Session() as session:
            delivery = session.query(Delivery).filter_by(delivery_id=delivery_id).first()
            if delivery:
                delivery.destination = destination
                delivery.status = status
                delivery.order_id = order_id
                session.commit()

    def delete_delivery(self, delivery_id):
        with self.Session() as session:
            delivery = session.query(Delivery).filter_by(delivery_id=delivery_id).first()
            if delivery:
                session.delete(delivery)
                session.commit()

    # --- Методи для таблиці Food_Order ---
    def add_food_order(self, fo_id, food_id, order_id):
        with self.Session() as session:
            food_order = FoodOrder(fo_id=fo_id, food_id=food_id, order_id=order_id)
            session.add(food_order)
            session.commit()

    def update_food_order(self, food_id, order_id, fo_id):
        with self.Session() as session:
            food_order = session.query(FoodOrder).filter_by(fo_id=fo_id).first()
            if food_order:
                food_order.food_id = food_id
                food_order.order_id = order_id
                session.commit()

    def delete_food_order(self, fo_id):
        with self.Session() as session:
            food_order = session.query(FoodOrder).filter_by(fo_id=fo_id).first()
            if food_order:
                session.delete(food_order)
                session.commit()
