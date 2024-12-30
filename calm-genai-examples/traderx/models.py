# Data models for TraderX architecture

@CALMNode("Data model for Account node")
class Account:
    def __init__(self, account_id, account_name, balance):
        self.account_id = account_id
        self.account_name = account_name
        self.balance = balance

    def __repr__(self):
        return f"<Account(account_id={self.account_id}, account_name={self.account_name}, balance={self.balance})>"

@CALMNode("Data model for Trade node")
class Trade:
    def __init__(self, trade_id, account_id, ticker, quantity, price):
        self.trade_id = trade_id
        self.account_id = account_id
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"<Trade(trade_id={self.trade_id}, account_id={self.account_id}, ticker={self.ticker}, quantity={self.quantity}, price={self.price})>"

@CALMNode("Data model for Position node")
class Position:
    def __init__(self, position_id, account_id, ticker, quantity):
        self.position_id = position_id
        self.account_id = account_id
        self.ticker = ticker
        self.quantity = quantity

    def __repr__(self):
        return f"<Position(position_id={self.position_id}, account_id={self.account_id}, ticker={self.ticker}, quantity={self.quantity})>"
