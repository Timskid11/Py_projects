#Made by Oyinlola Timilehin
from The_oop_code_for_it import *

print("Welcome to Q  TPS Backend by Timilehin")
print()
int_inibalance = 0
Name = ""

def naming_balanceini():
        
        global int_inibalance
        global Name
    
        Name = input("What is your name?\n")
        inibalance = input((f"\n{Name},you have to fund your account with at least 2000 as per Bank Policy\n"))
        int_inibalance = int(inibalance)
        
        
        if int_inibalance < 2000 :
            print()
            print()
            return naming_balanceini()
        
        def do_after_optionpick():
                
                
                Choice_for_TDBx = input("Choose from the following \n1 to Transfer\n2 to Deposit\n3 to Check Balance\n4 to withdraw\n5 to Create another account")
                if Choice_for_TDBx == "1":
                        
                        question1 = int(input("Amount to transfer:  "))
                        
                        print()
                        question2 = input("Name to tranfer to:  ")
                        TPS_activities(int_inibalance,Name).transfer(question1,question2)
                        
                         
                elif Choice_for_TDBx == "2":
                        question3 = int(input("Amount to deposit:  "))
                        TPS_activities(int_inibalance,Name).deposit(question3)
                        
                        
                        print(question3)
                
                elif Choice_for_TDBx == "3":
                        print(f"Account Balance of {Name} : {int_inibalance} ")
                elif Choice_for_TDBx == "5":
                        
                        print()
                        print()
                        naming_balanceini()
                
        
                elif Choice_for_TDBx == "4":
                        
                        question5 = int(input("Amount to withdraw:  "))
                        TPS_activities(int_inibalance,Name).withdraw(question5)
                        
                print()
                
                                
        do_after_optionpick()        
        Name =  TPS_activities(int_inibalance,Name)
        do_after_optionpick()
        print()
        
          
        

naming_balanceini()