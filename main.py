import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cards_security = pd.read_csv('card_security.csv', dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

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
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation! 
        Here is your booking information: 
        Name: {self.customer_name} 
        Hotel name: {self.hotel.name}"""
        return content


class SpaTicket(ReservationConfirmation):
    def generate(self):
        content = f"""
        Thank you for your SPA reservation! 
        Here is your SPA booking information: 
        Name: {self.customer_name} 
        Hotel name: {self.hotel.name}"""
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {'number': self.number, 'expiration': expiration,
                     'holder': holder, 'cvc': cvc}
        if card_data in df_cards:
            return True


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security['number']
                                         == self.number, 'password'].squeeze()
        if password == given_password:
            return True


print(df)
hotel_ID = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard('1234567890123456')
    if credit_card.validate('12/26', 'JOHN SMITH', '123'):
        if credit_card.authenticate('mypass'):
            hotel.book()
            name = input('Enter your name: ')
            reservation_ticket = ReservationConfirmation(name, hotel)
            print(reservation_ticket.generate())
            to_spa = input('\n Do you want to book a spa package? ')
            if to_spa == 'yes':
                spa_ticket = SpaTicket(name, hotel)
                print(spa_ticket.generate())
        else:
            print('Credit card authentication failed.')
    else:
        print('There was a problem with your payment.')
else:
    print('Hotel is fully booked.')
