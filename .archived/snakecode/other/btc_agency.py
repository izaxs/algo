from typing import Union
from datetime import date
from decimal import Decimal

class DailyStatus:
    def __init__(self) -> None:
        self.balance = Decimal(0)
        self.achVol = Decimal(0)
        self.ccVol = Decimal(0)

    def __repr__(self) -> str:
        return f'{{balance: {self.balance:.4f}, ach: {self.achVol:.4f}, cc: {self.ccVol:.4f}}}'

class UserStatus:
    def __init__(self) -> None:
        self.avgDailyBtc: Decimal = Decimal(0)
        self.avgDailyUsd: Decimal = Decimal(0)
        self.dailyStatus: dict[date, DailyStatus] = {}

    def __repr__(self) -> str:
        return f'{{status: {self.dailyStatus}, avg daily btc: {self.avgDailyBtc:.4f}, avg daily usd: {self.avgDailyUsd:.4f}'

def aggregate(logs: list[dict[str, Union[str, int, float]]]) -> str:
    userDb: dict[str, UserStatus] = {}
    for action in logs:
        user = userDb.setdefault(str(action['user_id']), UserStatus())
        actionDate = date.fromtimestamp(int(action['timestamp']))
        btcVol = Decimal(action['btc'])
        usdVol = Decimal(action['usd'])
        preCount = len(user.dailyStatus)
        s = user.dailyStatus.setdefault(actionDate, DailyStatus())
        if action['payment_method'] == 'ach':
            s.achVol += usdVol
        elif action['payment_method'] == 'cc':
            s.ccVol += usdVol
        if action['type'] == 'buy':
            s.balance += btcVol
        elif action['type'] == 'sell':
            s.balance -= btcVol
        curCount = len(user.dailyStatus)
        user.avgDailyBtc = (user.avgDailyBtc*preCount+btcVol)/curCount
        user.avgDailyUsd = (user.avgDailyUsd*preCount+usdVol)/curCount

    return str(userDb)


transactions = [
    {"user_id":"1","timestamp":1536987178,"type":"buy","btc":0.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"1","timestamp":1537095561,"type":"buy","btc":1.52,"usd":7256.52,"payment_method":"cc"},
    {"user_id":"1","timestamp":1537121938,"type":"sell","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537229927,"type":"buy","btc":0.03,"usd":7256.52,"payment_method":"cc"},
    {"user_id":"1","timestamp":1537242677,"type":"sell","btc":0.01,"usd":7256.52,"payment_method":"cc"},
    {"user_id":"1","timestamp":1537244060,"type":"buy","btc":2.7,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"1","timestamp":1537275458,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"1","timestamp":1537299582,"type":"sell","btc":0.9,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537424460,"type":"buy","btc":1.8,"usd":7256.52,"payment_method":"cc"},
    {"user_id":"2","timestamp":1537441605,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537491412,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537529720,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"1","timestamp":1537598813,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537620168,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537681809,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"cc"},
    {"user_id":"1","timestamp":1537683845,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"1","timestamp":1537772265,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"}
]

summary = aggregate(transactions)
print(summary)