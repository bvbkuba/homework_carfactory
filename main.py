from client import Client
from carfactory import CarFactory
from notify_to_clients import sending_mail
import asyncio

client = Client("abecadlo@gmail.com")  # tworzymy klienta
factory = CarFactory()  # tworzymy fabryki

async def orders():
    client.make_order(factory)   #składamy zamówienie w fabryce
    sending_mail(client.mail, "#1 Welcome in car factory - order","Your order is collected. We'll send you email if your car will be ready to get")
    await asyncio.sleep(1)
    sending_mail(client.mail, "#2 Welcome in car factory - your car is ready!","We realised your order. Visit us and enjoy your car.")

async def client_get_car():
    car = factory.get_car()
    await asyncio.sleep(1)
    car.drive()
    sending_mail(client.mail, "#3 Welcome in car factory - regards","You took your car. Thanks for trust, cu soon")

async def main():
    await asyncio.gather(orders(),client_get_car())
    print("Car was sending. Order is closed.")


if __name__ == "__main__":
    asyncio.run(main())

"""klient składa zamówienie w CarFactory,
odbiera je i nim jedzie"""
