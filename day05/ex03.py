a=1234
b=3.14
c=["문자열"]
def func02():
    print(f"{__name__}의 func02실행")

class Cl01:
    def func01(self):
        print("인스턴스의 기능 실행")
    
    @staticmethod
    def func02():
        print('static 메서드')

    @classmethod
    def func03(cls):
        print(cls, 'class 메서드')