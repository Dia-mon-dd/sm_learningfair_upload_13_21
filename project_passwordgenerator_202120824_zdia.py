print("====================")
print(" Password generator")
print(" Password generator")
print(" Password generator")
print(" Password generator")
print(" Password generator")
print(" Password generator")
print("====================")
print()
print()
print()
print("숫자 1과 2로 작동하며 다른 숫자를 입력하면 프로그램을 다시 시작해야 합니다.")
print("비밀번호를 설정할 기기는 pc인지 스마트폰인지 알려주세요")
print()
P = int(input ("""
pc는 숫자 1을,스마트폰은 숫자 2를 입력해주세요.

"""))

print()
print()


large   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small   = "abcdefghijklmnopqrstuvwxyz"
nums    = "0123456789"
symbols = "!@#$%^&*()[]{}-_=+"

if P == 1 :
        import random

        letters = large+small+nums+symbols

        while True:    

            password_length = int(input("""

비밀번호를 생성할 기기의 유형을 바꾸려면 프로그램을 다시 시작해주세요! 

혹시 사이트에서 요구하는 문자열이 포함되어있지 않다면 한번 더 실행해주세요. 

몇 자리 비밀번호를 만들까요?   """))   
            password_count  = 1
            
            for i in range (0,password_count): 
                password = ""
                
                for i in range(0,password_length):
                    password_list = random.choice(letters) 
                    password      = password+password_list
                    
                print("=================================")    
                print("=================================")
                print("생성된 비밀번호 : " , password, )
                print("=================================")
                print("=================================")
                print()
elif P == 2 :
        import random
    
        while True:

             password_length = int(input("""

비밀번호를 생성할 기기의 유형을 바꾸려면 프로그램을 다시 시작해주세요!

몇 자리 비밀번호를 만들까요?   """))   
             password_count  = 1
            
             for i in range (0,password_count): 
                 password = ""
                 
                 for i in range(0,password_length):
                    password_list = random.choice(nums) 
                    password      = password+password_list
                 print("=================================")
                 print("=================================")
                 print("생성된 비밀번호 : " , password )
                 print("=================================")
                 print("=================================")
                 print()

else : print("비밀번호를 생성하려면 프로그램을다시 실행해 주세요.")

print()
print()
print()
print()

