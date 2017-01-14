#  pass 키워드를 사용하면 클래스 내부에 아무것도 넣지 않은 상태로 클래스를 정의할 수 있습니다.
# 일단 클래스에 내부에 정의된 함수인 메서드의 첫 번째 인자는 반드시 self여야 한다고 당분간만 외우고 사용하기 바랍니다.
class BusinessCard:
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):
        print("--------------------")
        print("Name: ", self.name)
        print("E-mail: ", self.email)
        print("Address: ", self.addr)
        print("--------------------")


member1 = BusinessCard()
member1.set_info("Yuna Kim", "yunakim@naver.com", "Seoul")

print(member1.name)
print(member1.email)
print(member1.addr)

print("======")

member2 = BusinessCard()
member2.set_info("Sarang Lee", "sarang.lee@naver.com", "Kyunggi")
print(member2.name)
print(member2.email)
print(member2.addr)

print("=======")
member2.print_info()