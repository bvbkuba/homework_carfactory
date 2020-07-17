# pylint: disable=too-few-public-methods
import time
from warehouse import Warehouse


class CarFactory(object):
    def __init__(self):
        self.warehouse = Warehouse() #magazyn
        self.list_orders = []


    def take_order(self, order):
        self.list_orders.append(order)
        print("I added car order to list_orders")

    def get_car(self):
        print(f"We've in list_orders {len(self.list_orders)} car/s. Build car in progres..")
        order = self.list_orders[0]
        car_body = self.warehouse.get_car_body()
        engine = self.warehouse.get_engine(order)
        drive = self.warehouse.get_drive(order)
        car = Car(car_body, engine, drive)
        car_body.paint(order.colour)
        return car

class Car(object):
    def __init__(self, body, engine, drive):
        self.body = body   #karoseria/kolor
        self.engine = engine   #silnik
        self.drive_type = drive   #naped
        time.sleep(2)

    def drive(self):
        print(f"Driving car body:{self.body} "
                + f"engine:{self.engine} drive:{self.drive_type}")

"""CarFactory - fabryka aut - ma jeden magazyn i listę zamówień
takeorder - dodaje zamówienie do listy zamówień
getcar - zwraca auto które powstało na magazynie
"""
