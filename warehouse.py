# pylint: disable=too-few-public-methods
from enum import Enum


class CarBody(object):
    def __init__(self):
        self.colour = None    #kolor auta = brak

    def paint(self, colour):
        self.colour = colour   #pomaluj auto

    def __str__(self):
        return str(self.colour)    #zwroc kolor auta


class Engine(object):
    def __init__(self, horse_power):
        self.horse_power = horse_power     #naped auta

    def __str__(self):                      #wyswietlanie
        return str(self.horse_power)


class DriveType(Enum):    #grupy DriveType
    REAR = 1
    FRONT = 2
    ALL_WHEEL = 3


class Drive(object):          #rodzaj napedu
    def __init__(self, drive_type):
        self.drive_type = drive_type

    def __str__(self):
        return str(self.drive_type)


class Warehouse(object):    #magazyn
    @staticmethod
    def get_car_body():      #zwraca kolor auta
        return CarBody()

    @staticmethod
    def get_engine(order):     #
        return Engine(order.engine_power)

    @staticmethod
    def get_drive(order):
        return Drive(order.drive_type)

"""
carbody to np. kolor auta, można je pomalowąć
engine - napęd
drive - rodzaj napędy

Warehouse:
get_car_body - zwraca kolor auta
get-engine - zwraca rodzaj napedu enginepower-horsepower
get-drive - zwraca rodzaj napędu
"""
