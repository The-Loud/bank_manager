# copying along some other code to learn classes and get pratice.

# high level account class.
class Account():

    def __init__(self, cust_id):
        self.cust_id = cust_id

class CheckingAccount(Account):

    def __init__(self, cust_id, deposit_amount):
        Account.__init__(self, cust_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_part = 0

        # pulls the whole number from amount as integer
        self.amount_whole = int(self.numstr[:self.numstr.find('.')])

        # pulls the decimal value from amount as integer
        self.amount_part = int(self.numstr[self.numstr.find('.') + 1:])

    # return the string of the amount of the deposit
    def __str__(self):
        return ("{0:.2f}".format(self.amount))

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        # debugging test
        print(f"self whole: {self.amount_whole}")
        print(f"self part: {self.amount_part}")

        self.withdraw_whole = int(withdraw_amount[:withdraw_amount.find('.')])
        numstr = str(withdraw_amount)
        self.withdraw_part = int(numstr[numstr.find('.') + 1:])


        if self.amount > float(withdraw_amount):
            self.amount_whole -= self.withdraw_whole

        # if the decimal value of the requested amount is 
        # greater than the decimal value of the account in the amount, 
        # then one dollar is taken out
            if self.withdraw_part > self.amount_part:
                self.amount_part = self.withdraw_part - self.amount_part
                self.amount_whole -= 1
                self. amount_part = 100 - self.amount_part
            else:
                self.amount_part -= self.withdraw_part


            # after cutting up and manipulating the values, put them back together.
            new_amount = str(self.amount_whole) + "." + str(self.amount_part)

            # cast it back to a float
            self.amount = round(float(new_amount), 2)
        else:
            print("Insufficient funds.")
