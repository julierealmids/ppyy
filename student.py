class Student:
    school="Akirachix"
    def __init__(self,name,age,country,full_name,year_of_birth,initials):
        self.name=name
        self.age=age
        self.country=country
        self.full_name=full_name
        self.year_of_birth=year_of_birth
        self.initials=initials
    def get_initials(fullname):
      xs = (fullname)
    name_list = xs.split()

    initials = ""

    for name in name_list:
      initials += name[0].upper()
      return initials
    def greet(self):
           f"Hello {self.full_name},you were born in {self.year_of_birth}"
        
      
      
        
    
class Account:
    Bank="Centenary"
    def __init__(self,name,number,deposit,withdraw,balance):
        self.name=name
        self.number=number
        self.balance=balance
        self.deposit=deposit
        self.withdraw=withdraw
    def deposit(self):
    		self.total_amount += float(input('Hello {}, please enter amount to deposit : '(self.name)))
      self.print_current_balance()

    def withdraw(self):
        amount_to_withdraw = float(input('Enter amount to withdraw : '))
        if amount_to_withdraw > self.total_amount:
            print('Insufficient Balance !!')
        else:
	        self.total_amount -= amount_to_withdraw
        self.print_current_balance()