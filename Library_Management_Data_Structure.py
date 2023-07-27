class library:
    def __init__(self, book_list):
        self.book_list = book_list

    def view_book(self):
        for i in self.book_list:
            print(i)

    def lend_book(self, customer_id, customer_name, book_name):
        if book_name in self.book_list:
            if customer_id in customer_data:
                if customer_data[customer_id][0] == customer_name:
                    customer_data[customer_id].append(book_name)
                    self.book_list.remove(book_name)
                    print("Your request is done")
                else:
                    print("Name mismatch. Please verify your name")
            else:
                customer_data[customer_id] = [customer_name, book_name]
                self.book_list.remove(book_name)
                print("Your request is done")
            print(customer_data)
        else:
            print("The book is out of stock")

    def return_book(self, customer_id, book_name):
        if customer_id in customer_data and book_name in customer_data[customer_id]:
            customer_data[customer_id].remove(book_name)
            self.book_list.append(book_name)
            self.book_list.sort(reverse=False)
            print("Your request is done")
        else:
            if customer_id not in customer_data:
                print("Your Member ID is invalid or you are not a registered member")
            else:
                print("you didn't lend the book " + book_name)
        print(customer_data)
class customer:
    def customer_id(self):
        self.id = input("Enter your Member ID: ")
        self.id = self.id.upper()
        return self.id

    def customer_name(self):
        self.name = input("Enter your name: ")
        self.name = self.name.upper()
        return self.name

    def book_name(self):
        self.book = input("Enter book name: ")
        self.book = self.book.upper()
        return self.book

lib = library(['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10'])
cus = customer()
customer_data = {}
while True:
    print("\nEnter the option below: ")
    print("1 - Show list of books \n2 - Lend book \n3 - Return book \n4 - exit\n")
    option = int(input("Option: "))
    if option == 1:
        lib.view_book()
    elif option == 2:
        customer_id = cus.customer_id()
        customer_name = cus.customer_name()
        book_name = cus.book_name()
        lib.lend_book(customer_id, customer_name, book_name)
    elif option == 3:
        customer_id = cus.customer_id()
        book_name = cus.book_name()
        lib.return_book(customer_id, book_name)
    elif option == 4:
        print("Thank you for using our service. Have a great day!")
        break
    else:
        print("you entered the incorrect option")
