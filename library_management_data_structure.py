class library:
    def __init__(self, book_list):
        self.book_list = book_list

    def view_book(self):
        for i in self.book_list:
            print(i)

    def lend_book(self, customer_name, book_name):
        if book_name in self.book_list:
            if customer_name in customer_data:
                customer_data[customer_name].append(book_name)
                self.book_list.remove(book_name)
                print("Your request is done")
            else:
                customer_data[customer_name] = [book_name]
                self.book_list.remove(book_name)
                print("Your request is done")
            print(customer_data)
        else:
            print("The book is not available")

    def return_book(self, customer_name, book_name):
        if customer_name in customer_data and book_name in customer_data[customer_name]:
            customer_data[customer_name].remove(book_name)
            self.book_list.append(book_name)
            self.book_list.sort(reverse=False)
        else:
            if customer_name not in customer_data:
                print("Yor name is not in our database")
            else:
                print("You are not lend the book of " + book_name)
        print(customer_data)
class customer:
    def customer_name(self):
        print("Enter your name")
        self.name = input()
        return self.name

    def book_name(self):
        print("Enter book name")
        self.book = input()
        return self.book

lib = library(['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10'])
cus = customer()
customer_data = {}
while True:
    print("\nSelect the option below: ")
    print("1 - Show list of books \n2 - Lend book \n3 - Return book \n4 - exit")
    option = int(input())
    if option == 1:
        lib.view_book()
    elif option == 2:
        name = cus.customer_name()
        book = cus.book_name()
        lib.lend_book(name, book)
    elif option == 3:
        name = cus.customer_name()
        book = cus.book_name()
        lib.return_book(name, book)
    elif option == 4:
        break
    else:
        print("you entered the incorrect option")
