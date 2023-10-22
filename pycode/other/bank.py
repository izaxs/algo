import heapq

class Bank:
    CODE_SUCCEED = 0
    CODE_ERROR_ACCOUNT_EXISTS = 1
    CODE_ERROR_ACCOUNT_NOT_EXISTS = 2
    CODE_ERROR_NOT_ENOUGH_FUND = 3
    CODE_ERROR_DEPOSIT_NEGATIVE = 4
    CODE_ERROR_TRANSFER_NEGATIVE = 5
    CODE_ERROR_TOPK_NEGATIVE = 6


    def __init__(self):
        self.accounts: dict[str, int] = {}
        self.moneyOut: dict[str, int] = {}

    def request(self, query: list[str]):
        pass

    def createAccount(self, name: str) -> int:
        if name in self.accounts: return self.CODE_ERROR_ACCOUNT_EXISTS
        self.accounts[name] = 0
        return self.CODE_SUCCEED

    def deposit(self, name: str, amount: int) -> int:
        if amount <= 0: return self.CODE_ERROR_DEPOSIT_NEGATIVE
        if name not in self.accounts: return self.CODE_ERROR_ACCOUNT_NOT_EXISTS
        self.accounts[name] += amount
        return self.CODE_SUCCEED
    
    def transfer(self, fromName: str, toName: str, amount: int) -> int:
        if amount <= 0: return self.CODE_ERROR_TRANSFER_NEGATIVE
        if fromName not in self.accounts or toName not in self.accounts:
            return self.CODE_ERROR_ACCOUNT_NOT_EXISTS
        if self.accounts[fromName] < amount:
            return self.CODE_ERROR_NOT_ENOUGH_FUND
        self.accounts[fromName] -= amount
        self.accounts[toName] += amount
        self.moneyOut[fromName] += amount
        return self.CODE_SUCCEED
    
    def topKActiveUsers(self, topK: int) -> list[str]:
        if topK < 0: topK = 0
        topKUsers = heapq.nlargest(topK, self.moneyOut.items(), key=lambda x: (x[1], x[0]))
        return [user for user, _ in topKUsers]
    

        
    
        