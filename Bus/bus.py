class Bus:

    earning = 0

    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

        BusSystem.buses.append(self)

    def available_seats(self):
        return self.total_seats - self.booked_seats
    
    def book_seat(self):
        if self.total_seats > self.booked_seats:
            self.booked_seats += 1
            Bus.earning += 500
        else:
            print('\nSeat not available!\n')



class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus

        BusSystem.passengers.append(self)


class BusSystem:
    buses = []
    passengers = []

    def show_buses(self):
        found = False
        for bus in self.buses:
            found = True
            if bus.available_seats() > 0:
                print(f'{bus.number}\t{bus.route}\t{bus.available_seats()}')
        if not found:
            print('\nNo bus available\n')

    def book_ticket(self, bus_number, name, phone):
        found = False
        for bus in self.buses:
            if bus.number == bus_number:
                if bus.available_seats() > 0:
                    bus.book_seat()
                    Passenger(name, phone, bus)
                    print('\nTicket booked successfully! Fare : 500Tk\n')
                    found = True
                    break
                else:
                    print('\nNo available seat\n')
        
        if not found:
            print('\nBus not found!\n')

    def view_all_buses(self):
        found = False
        for bus in self.buses:
            found = True
            print(f'{bus.number}\t{bus.route}')
        if not found:
            print('\nNo bus available\n')



class Admin:
    def __init__(self):
        self.__username = 'Admin'
        self.__password = 1234

    def login(self, username, password):
        if self.__username == username and self.__password == password:
            # print('Welcome Admin')
            return True
        else:
            # print('Wrong input. Try again')
            return False
        
    def add_bus(self, number, route, seats):
        for bus in bus_system.buses:
            if bus.number == number:
                print(f'\nBus with {number} is alreay exist\n')
                return
        Bus(number, route, seats)
    

admin = Admin()
bus_system = BusSystem()  

while True:

    print('1. Admin Login')
    print('2. Book Ticket')
    print('3. View Buses')
    print('4. Exit')

    choice = int(input('\nEnter your choice : '))
    if choice == 1:
        username = input('Enter Admin username : ')
        password = int(input('Enter Admin password : '))
        if admin.login(username, password):
            while True:
                print("Select an Option\n"
                    "1. Add Bus\n"
                    "2. View All Buses\n"
                    "3. Logout")
            
                admin_input = int(input('\nEnter your choce : '))
                if admin_input == 1:
                    number = input('Enter bus number : ')
                    route = input('Enter bus route : ')
                    seats = int(input('Enter the number of total seats : '))
                    admin.add_bus(number, route, seats)
                elif admin_input == 2:
                    bus_system.view_all_buses()
                elif admin_input == 3:
                    break
                else:
                    print('\nWrong input. Try again!\n')

        else:
            print('\nWrong input. Try again!\n')


    elif choice == 2:
        bus_number = input('Enter bus number : ')
        name = input('Enter your name : ')
        phone = input('Enter your phone number : ')
        bus_system.book_ticket(bus_number, name, phone)

    elif choice == 3:
        bus_system.show_buses()
    elif choice == 4:
        break
    else:
        print('\nWrong input. Try again!\n')
