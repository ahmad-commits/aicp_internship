import os

class Train:
    def __init__(self, train_number, departure_time, return_time, departing_seats_available, returning_seats_available):
        self.train_number = train_number
        self.departure_time = departure_time
        self.return_time = return_time
        self.departing_seats_available = departing_seats_available
        self.returning_seats_available = returning_seats_available
        self.total_passengers = 0
        self.total_money = 0
        self.status = 'Open'

    def book_ticket(self, passengers, is_returning, return_train=None):
        if self.status == 'Closed':
            print('This train is closed')
            return False, 0
        if passengers < 1:
            print('Invalid number of passengers')
            return False, 0
        if is_returning:
            if return_train is not None:
                if return_train.returning_seats_available == 0:
                    print('No seats available for returning train')
                    return False, 0
                if passengers > return_train.returning_seats_available:
                    print('No seats available for returning train')
                    return False, 0
                discount_eligible, cost = self._book_ticket_helper(passengers)
                return_train.returning_seats_available -= passengers
                if return_train.returning_seats_available == 0 and self.departing_seats_available == 0:
                    self.status = 'Closed'
                    return_train.status = 'Closed'
                return discount_eligible, cost
            else:
                if self.returning_seats_available == 0:
                    print('No seats available for returning train')
                    return False, 0
                if passengers > self.returning_seats_available:
                    print('No seats available for returning train')
                    return False, 0
                discount_eligible, cost = self._book_ticket_helper(passengers)
                self.returning_seats_available -= passengers
                if self.returning_seats_available == 0 and self.departing_seats_available == 0:
                    self.status = 'Closed'
                return discount_eligible, cost
        else:
            if self.departing_seats_available == 0:
                print('No seats available for departing train')
                return False, 0
            if passengers > self.departing_seats_available:
                print('No seats available for departing train')
                return False, 0
            discount_eligible, cost = self._book_ticket_helper(passengers)
            self.departing_seats_available -= passengers
            if self.departing_seats_available == 0 and self.returning_seats_available == 0:
                self.status = 'Closed'
                self.departure_time = 'Closed'
            return discount_eligible, cost

    def _book_ticket_helper(self, passengers):
        free_tickets = passengers // 10
        paid_tickets = passengers - free_tickets
        cost = paid_tickets * 50
        discount_eligible = False
        if passengers >= 10:
            cost *= 1
            discount_eligible = True
        self.total_passengers += passengers
        self.total_money += cost
        return discount_eligible, cost

    def display(self):
        print('┌' + '─' * 16 + '┬' + '─' * 16 + '┬' + '─' * 16 + '┬' + '─' * 16 + '┬' + '─' * 16 + '┬' + '─' * 16 + '┐')
        print('│' + f'{"Train number:":^15} ' + '│' + f'{"Departure:":^15} ' + '│' + f'{"Return:":^15} ' + '│' + f'{"Departure Seats":^15} ' + '│' + f'{"Return Seats:":^15} ' + '│' + f'{"Status:":^15} ' + '│')
        print('├' + '─' * 16 + '┼' + '─' * 16 + '┼' + '─' * 16 + '┼' + '─' * 16 + '┼' + '─' * 16 + '┼' + '─' * 16 + '┤')
        print('│' + f'{self.train_number:^15}' + ' │' + f'{self.departure_time:^15}' + ' │' + f'{self.return_time:^15}' + ' │' + f'{self.departing_seats_available:^15}' + ' │' + f'{self.returning_seats_available:^15}' + ' │' + f'{self.status:^15}' + ' │')
        print('└' + '─' * 16 + '┴' + '─' * 16 + '┴' + '─' * 16 + '┴' + '─' * 16 + '┴' + '─' * 16 + '┴' + '─' * 16 + '┘')

trains = [Train(0, '09:00', '10:00', 480, 480), Train(1, '11:00', '12:00', 480, 480), Train(2, '13:00', '14:00', 480, 480), Train(3, '15:00', '16:00', 480, 640)]

for train in trains:
    train.display()

most_departing_tickets = 0
most_returning_tickets = 0
most_departing_train = None
most_returning_train = None

while any(train.status == 'Open' for train in trains):
    try:
        train_num_input = input('Enter train number to book (0-3) or enter "all" to show all schedules or enter "end": ')
        if train_num_input == 'all':
            for train in trains:
                train.display()
            continue
        elif train_num_input == 'end':
            break
        train_num = int(train_num_input)
        if train_num not in range(len(trains)):
            raise ValueError('Invalid train number')
        departing_train = trains[train_num]
        if departing_train.departing_seats_available == 0 and departing_train.returning_seats_available == 0:
            print('No seats available for this train')
            continue
        if train_num == 3:
            return_on_same_train = 'y'
        else:
            return_on_same_train = input('Do you want to return on the same train? (y/n): ')
            while return_on_same_train not in ['y', 'n']:
                return_on_same_train = input('Do you want to return on the same train? (y/n): ')
        if return_on_same_train == 'y':
            passengers = int(input('Enter number of passengers: '))
            departing_train.departing_seats_available -= passengers
            discount_eligible, price = departing_train.book_ticket(passengers, True)
            if discount_eligible:
                print('Discount eligible')
            departing_train.display()
            os.system('clear')
            print(f'Total cost of tickets: ${price:.2f}')
            if departing_train.total_passengers > most_departing_tickets:
                most_departing_tickets = departing_train.total_passengers
                most_departing_train = departing_train
        else:
            available_returning_trains = [train for train in trains if train.status == 'Open' and train.returning_seats_available > 0 and train != departing_train]
            if not available_returning_trains:
                raise ValueError('No available returning trains')
            print('Available returning trains:')
            for i, train in enumerate(available_returning_trains):
                print(f'Selection {i}')
                train.display()
            return_train_num = int(input('Enter selection number: '))
            if return_train_num not in range(len(available_returning_trains)):
                raise ValueError('Invalid returning train number')
            return_train = available_returning_trains[return_train_num]
            if return_train.returning_seats_available == 0:
                print('No seats available for returning train')
                continue
            passengers = int(input('Enter number of passengers: '))
            departing_train.departing_seats_available -= passengers
            discount_eligible, price = departing_train.book_ticket(passengers, True, return_train)
            if discount_eligible:
                print('Discount eligible')
            print(f'Total cost of tickets: ${price:.2f}')
            os.system('clear')
            departing_train.display()
            return_train.display()
            if departing_train.total_passengers > most_departing_tickets:
                most_departing_tickets = departing_train.total_passengers
                most_departing_train = departing_train
            if return_train.total_passengers > most_returning_tickets:
                most_returning_tickets = return_train.total_passengers
                most_returning_train = return_train
    except ValueError as e:
        print(e)

total_money_earned = sum(train.total_money for train in trains)
print(f'Total money earned: ${total_money_earned:.2f}')
if most_departing_train is not None:
    print(f'Train with most departing tickets: {most_departing_train.train_number}, {most_departing_tickets} tickets sold')
if most_returning_train is not None:
    print(f'Train with most returning tickets: {most_returning_train.train_number}, {most_returning_tickets} tickets sold')
