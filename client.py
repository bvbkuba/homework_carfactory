# pylint: disable=too-few-public-methods
from warehouse import DriveType
from notify_to_clients import sending_mail
class Client(object):
    def __init__(self,mail):  #by MS
        self.mail = mail

    @staticmethod
    def make_order(factory):
        client = Client("obek@op.pl")
        order = Order("RED", 200, DriveType.ALL_WHEEL)   #zamówienie złożone
        factory.take_order(order)  #dodaj do zamówień w fabryce


class Order(object):     #wymóg na zamówienie
    def __init__(self, colour, engine_power, drive_type):
        self.colour = colour
        self.engine_power = engine_power
        self.drive_type = drive_type


"""klient robi zamówienie i przekazuje je do fabryki"""
