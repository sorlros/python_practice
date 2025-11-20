# class Car:
#     def init(self):
#         self.color = "black"
#         self.speed = 100

#     def info(self):
#         print(f"색깔은 {self.color}, 속도는 {self.speed}")

# redcar = Car()
# bluecar = Car()

# redcar.color = "red"
# redcar.speed = 150
# redcar.info()

# bluecar.color = "blue"
# bluecar.speed = 300
# bluecar.info()

# class CarI:
#     def __init__(self, c, s):
#         self.color = c
#         self.speed = s

#     def info(self):
#         return f"color: {self.color}, speed: {self.speed}"

# car_red = CarI("Red", 80)
# print("car info", car_red.info())

# class FourCal :
#   def __init__(self, fir, sec) :
#     self.first = fir
#     self.second = sec

#   def add(self) :
#     return self.first + self.second

#   def sub(self) :
#     return self.first - self.second

#   def mul(self) :
#     return self.first * self.second

#   def div(self) :
#     return self.first / self.second
  

# myfourcal1 =  FourCal(8,2)

# print(myfourcal1.add())
# print(myfourcal1.mul())

# class MoreFourCal(FourCal):
#     def pow(self):
#         return self.first ** self.second
    
# mymore1 = MoreFourCal(4, 3)
# print("ADD: ", mymore1.add())

# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else: 
#             return self.first / self.second

# a = SafeFourCal(6, 3)        
# print(a.div())


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def info(self):
#         return f"책의 제목은  {self.title}, 책의 저자는 {self.author}"

#     def get_title(self):
#         return self.title
#     def get_author(self):
#         return self.author
#     def set_title(self, new_title):
#         self.title = new_title
#     def set_author(self, new_author):
#         self.author = new_author

# book1 = Book("어린왕자", "베리")
# print(book1.get_title())
# print(book1.get_author())

# book2 = Book(None, None)
# book2.set_title("해리포터")
# book2.set_author("JK롤링")
# print(book2.info())


# class Stock:
#     def __init__(self):
#         self.name = input("종목명을 입력해주세요: ")
#         self.code = input("해당 종목의 코드를 입력해주세요: ")

#     def stock_info(self):
#         return f"주식명은 {self.name}, 코드는 {self.code}"
    
# stock1 = Stock()
# print(stock1.stock_info())

import random 

random.randint(1, 999999)

class Account:
    number_of_account = 0

    def __init__(self, owner_name, init_balance):
        self.owner_name = owner_name
        self.balance = init_balance
        
        self.account_number = self.generate_account_number()
        self.bank_name = "국민은행"

    def generate_account_number(self):
        first_number = str(random.randint(100, 999))
        second_number = str(random.randint(00, 99))
        third_number  = str(random.randint(100000, 999999))

        final_number = f"{first_number}-{second_number}-{third_number}"

        return final_number

    def display_info(self):
        print("은행명:",self.bank_name)
        print("이름:",self.owner_name)
        print("계좌번호:",self.account_number)
        print("잔액:", self.balance)
    
    def generate_account(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
        self.bank_name = "국민은행"
        self.account_number = self.generate_account_number()

        Account.number_of_account += 1

    def deposit(self, money):
        if money >= 1:
            self.balance += money
            print(f"현재 잔액은 {self.balance}")

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            print(f"현재 잔액은 {self.balance}")
        else: 
            print("잔액 부족")   

account1 = Account("최규철", 12312300)

account1.display_info()

account1.withdraw(50000)

account1.display_info()
