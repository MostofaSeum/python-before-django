#Video Link: https://youtu.be/HeW-D6KpDwY?si=_XfyE6rwN-QnpneR

# class student:
#     def __init__(self, name, m1,m2,m3):
#         print("Hello", name)
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
        
#     def average(self):
#          print("average is", (self.m1+self.m2+self.m3)/3)

#     @staticmethod
#     def hello():
#         print("Hello World ")

# s1 = student("Seum", 90,80,70)
# s1.average()
# s1.hello()
    


#Pratice 2
class account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
        
    def debit(self, amt):
        self.balance -= amt
        print("Balance is", self.balance)
        
    def credit(self, amt):
        self.balance += amt
        print("Balance is", self.balance)

b1 = account(1000,1234) 
b1.debit(100)
b1.credit(200)

        
