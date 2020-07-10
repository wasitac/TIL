class User:
    #클래스 만들 때 이름첫글자는 항상 대문자
    def say_hello(self):
        #인사메세지 출력 메소드
        print("안녕하세여! 저는 {}입니다!".format(self.name))

    def login(self, my_email, my_password):
        #로그인 메소드
        if(self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다")
        else:
            print("로그인실패")

#인스턴스
user1 = User()
user2 = User()
user3 = User()

#인스턴스 변수
user1.name = "이지홍"
user1.email = "ghong817@gmail.com"
user1.password = "12345"

user2.name = "이지지"
user2.email = "yigigi10@gmail.com"
user2.password = "76845"

user3.name = "이지윤"
user3.email = "ssss1237@gmail.com"
user3.password = "13455"


print(user1.email)
User.say_hello(user1)
user1.login("ghong817@gmail.com", "12345")
