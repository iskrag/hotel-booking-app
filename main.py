import pandas as pd

df = pd.read_csv('hotels.csv')

class User:
    def view_hotels(self):
        pass


class Hotel:
    def __init__(self, id):
        pass
    def book(self):
        pass
    def available(self):
        pass

class ReservationConfirmation:
    def __init__(self, customer_name, hotel_object):
        pass
    def generate(self):
        content = f'Name of the customer hotel'
        return content


print(df)
id = input('Enter the id of the hotel: ')
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input('Enter your name: ')
    reservation_ticket = ReservationConfirmation(hotel)
    print(reservation_ticket.generate())
else:
    print('Hotel is fully booked.')
