import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """Book hotel and change to unavailable"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """Checks if hotel is available"""
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationConfirmation:
    def __init__(self, customer_name, hotel_object):
        pass
    def generate(self):
        content = f'Name of the customer hotel'
        return content


print(df)
hotel_ID = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input('Enter your name: ')
    reservation_ticket = ReservationConfirmation(name, hotel)
    print(reservation_ticket.generate())
else:
    print('Hotel is fully booked.')
