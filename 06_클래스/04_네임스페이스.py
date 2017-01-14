class Stock:
    market = "kospi"

print(dir())

#  6.11과 같이 하나의 독립적인 네임스페이스가 생성됩니다.
# 그리고 클래스 내에 정의된 변수나 메서드는 그 네임스페이스 안에 파이썬 딕셔너리 타입으로 저장

# Stock 클래스의 네임스페이스를 파이썬 코드로 확인하려면 클래스의 __dict__ 속성을 확인
print("== stock 클래스의 네임 스페이스 ==")
print(Stock.__dict__)

print("===== dir 에서 s1, s2 확인")
s1 = Stock()
s2 = Stock()
print(dir())

print("== s1 마켓 설정 == ")
s1.market = 'kosdak'
print(s1.__dict__)
print(s2.__dict__)
print(s2.market)
