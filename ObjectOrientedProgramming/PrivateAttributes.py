class Account:
    def __init__(self,acc_no,acc_pass):
        self.__acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pwd(self,new_pwd):
        self.__acc_pass=new_pwd

Ac1=Account("AB01","@123")

print(Ac1.__acc_no)
print(Ac1.__acc_pass)
