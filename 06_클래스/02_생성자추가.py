class BusinessCard:
    def __init__(self):
        print("객체가 생성되었습니다.")
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):
        print("--------------------")
        print("Name: ", self.name)
        print("E-mail: ", self.email)
        print("Address: ", self.addr)
        print("--------------------")

class MyClass:
    def __init__(self):
        print("객체가 생성되었습니다.")

inst1 = MyClass()

member1 = BusinessCard("Kangsan Lee", "kangsan.lee", "USA")
member1.print_info()

