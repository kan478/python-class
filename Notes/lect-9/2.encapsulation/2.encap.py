# class OfficeDocument:
#     def __init__(self,name,reco, securedDocument,key):
#         self.nameDoc = name 
#         self.bankRecord = reco  
#         self.__secureddocument = securedDocument
#         self.Securedkey = key

#     def get_securedDocument(self,key):
#         if(self.Securedkey == key):
#              return self.__secureddocument
#         else:
#             print("Invalid password")
    
# doc1 = OfficeDocument('IndBankStatment24-25','ind25245',"credit-debit Records",1234)

# print(f'Document Details : {doc1.nameDoc} and {doc1.bankRecord}')

# print(doc1.__secureddocument)
# print(doc1.get_securedDocument(1234))


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0 :
            self.__balance += amount
        else:
            print("giver proper amount")

    def get_balance(self):
    
        return self.__balance
        
    
acc1 = BankAccount(100000)
acc1.deposit(-68568)
print(acc1.get_balance())
