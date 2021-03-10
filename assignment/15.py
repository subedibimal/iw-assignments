class Customer:

    def __init__(self, name, age, acc_number, location, curr_balance):
        self.name = name
        self.age = age
        self.acc_number = acc_number
        self.location = location
        self.curr_balance = curr_balance

    def withDrawBalance(self, balance):
        if balance <= self.curr_balance:
            self.curr_balance -= balance
        return balance

    def depositBalance(self, balance):
        self.curr_balance += balance
        return self.curr_balance

    def update_location(self, location):
        self.location = location

    def update_name(self, name):
        self.name = name

    def update_age(self, age):
        self.age = age
