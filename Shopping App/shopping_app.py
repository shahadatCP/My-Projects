from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, email, password):
        self.email = email
        self.__password = password
       
    def get_pass(self):
        return self.__password


class UserManager:
    def __init__(self):
        self.customers = []
        self.sellers = []

    def customer_check(self, email, password):
        for person in self.customers:
            if person.email == email:
                return person.get_pass() == password
        return False
    
    def seller_check(self, email, password):
        for person in self.sellers:
            if person.email == email:
                return person.get_pass() == password
        return False
    
class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)

class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)



class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def buy_product(self, name, quantity):
        for product in self.products:
            if product.name == name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print(f"You bought {product.name} successfully")
                    return
                else:
                    print(f"Not enough stock for {product.name}")
                    return
        print("Product not available!")

    def show_products(self):
        print(f'Name\tPrice\tQuantity')
        for product in self.products:
            if product.quantity > 0:
                print(f'{product.name}\t{product.price}\t{product.quantity}')

        

# customer = Customer("saki@gmail.com", 1214)
# seller = Seller("faruk@gmail.com", 5658)
store = Store()
manager = UserManager()

# p1 = Product("Rice", 50, 10)
# p2 = Product("Oil", 120, 5)
# store.add_product(p1)
# store.add_product(p2)
# print(store.products[0].name)      
# print(store.products[1].price)
# store.buy_product('Rice', 10)
# print(store.products[0].quantity)
# store.show_products()

p1 = Product("Rice", 50, 10)
p2 = Product("Oil", 120, 5)
store.add_product(p1)
store.add_product(p2)



while True:
    print('\n--- MAIN MENU ---')
    print('1. Customer')
    print('2. Seller')
    print('3. Exit')
    option = int(input('Choose your option: '))

    # customer
    if option == 1:
        print('\n1. Login')
        print('2. Create Account')
        print('3. Back')
        choice = int(input('Choose: '))
        
        if choice == 1:
            email = input('Enter email: ')
            password = input('Enter password: ')
            if manager.customer_check(email, password):
                print('Login successful!')
                while True:
                    print('\n1. Show Products')
                    print('2. Buy Product')
                    print('3. Logout')
                    c_choice = int(input('Choose: '))
                    
                    if c_choice == 1:
                        store.show_products()
                    elif c_choice == 2:
                        name = input('Enter product name: ')
                        quantity = int(input('Enter quantity: '))
                        store.buy_product(name, quantity)
                    elif c_choice == 3:
                        break
                    else:
                        print('Invalid input!')
            else:
                print('Invalid email or password!')
        
        elif choice == 2:
            email = input('Enter new email: ')
            password = input('Enter new password: ')
            manager.customers.append(Customer(email, password))
            print('Account created successfully!')
        
        elif choice == 3:
            continue
        else:
            print('Invalid input!')

    # seller
    elif option == 2:
        print('\n1. Login')
        print('2. Create Account')
        print('3. Back')
        choice = int(input('Choose: '))
        
        if choice == 1:
            email = input('Enter email: ')
            password = input('Enter password: ')
            if manager.seller_check(email, password):
                print('Login successful!')
                while True:
                    print('\n1. Show Products')
                    print('2. Add Product')
                    print('3. Logout')
                    s_choice = int(input('Choose: '))
                    
                    if s_choice == 1:
                        store.show_products()
                    elif s_choice == 2:
                        name = input('Product name: ')
                        price = int(input('Price: '))
                        quantity = int(input('Quantity: '))
                        store.add_product(Product(name, price, quantity))
                        print('Product added successfully!')
                    elif s_choice == 3:
                        break
                    else:
                        print('Invalid input!')
            else:
                print('Invalid email or password!')
        
        elif choice == 2:
            email = input('Enter new email: ')
            password = input('Enter new password: ')
            manager.sellers.append(Seller(email, password))
            print('Seller account created successfully!')
        
        elif choice == 3:
            continue
        else:
            print('Invalid input!')

    # end
    elif option == 3:
        print('Exiting program...')
        break
    else:
        print('Invalid input!')
