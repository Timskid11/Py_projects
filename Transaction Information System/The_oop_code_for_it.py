#Timi's project on oop using polymorphism and the rest.
class Exception_for_Balance:
    pass
class TPS_activities:
    def __init__(self,initial_balance,account_holder):
        self.initial_balance = initial_balance
        self.account_holder = account_holder
        print(f"Account '{self.account_holder}' created successfully.\n")
    def balance(self):
                 print(f" {self.account_holder}'s balance is £{self.initial_balance:.2f}")
    
    def deposit(self,amount):
        self.initial_balance = self.initial_balance + amount
        self.balance()
    def viableTransaction(self, amount):
        if self.initial_balance >= amount:
            return
        else:
            raise Exception_for_Balance(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    def withdraw(self,amount):
        self.initial_balance = self.initial_balance - amount
        self.balance()
        
    def transfer(self, amount, account_holder):
        
        self.withdraw(amount)
        if isinstance(account_holder, str):
            print(f" Transfer of £{amount:.2f} to account '{account_holder}'")
        else:
            account_holder.deposit(amount)
            print("Transfer Successful")
            self.balance()
            
            
            
        
    
    
    
        
        
            
    
        
        
    
                    
                    
            
            
            
                
                    
                    
            
                    
                    
            
            
            
        
            
            
    
    
        
