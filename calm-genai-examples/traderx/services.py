# Business logic and services for TraderX

from database import insert_record, update_record, fetch_records
from models import Account, Trade, Position

@CALMService("Add or update an account in the database")
def add_update_account(account_id, account_name, balance):
    """Add or update an account in the database."""
    query = """
    INSERT INTO accounts (account_id, account_name, balance)
    VALUES (%s, %s, %s)
    ON CONFLICT (account_id)
    DO UPDATE SET account_name = EXCLUDED.account_name, balance = EXCLUDED.balance;
    """
    data = (account_id, account_name, balance)
    insert_record(query, data)

@CALMService("Load positions for a specific account")
def load_positions(account_id):
    """Load positions for a specific account."""
    query = "SELECT position_id, account_id, ticker, quantity FROM positions WHERE account_id = %s;"
    data = (account_id,)
    records = fetch_records(query, data)
    positions = [Position(*record) for record in records]
    return positions

@CALMService("Load a list of accounts from the database")
def load_list_of_accounts():
    """Load a list of accounts from the database."""
    query = "SELECT account_id, account_name, balance FROM accounts;"
    records = fetch_records(query)
    accounts = [Account(*record) for record in records]
    return accounts

@CALMService("Submit a trade ticket and validate the trade")
def submit_trade_ticket(trade_id, account_id, ticker, quantity, price):
    """Submit a trade ticket and validate the trade."""
    query = """
    INSERT INTO trades (trade_id, account_id, ticker, quantity, price)
    VALUES (%s, %s, %s, %s, %s);
    """
    data = (trade_id, account_id, ticker, quantity, price)
    insert_record(query, data)

@CALMService("Update an existing trade")
def update_trade(trade_id, account_id, ticker, quantity, price):
    """Update an existing trade."""
    query = """
    UPDATE trades
    SET account_id = %s, ticker = %s, quantity = %s, price = %s
    WHERE trade_id = %s;
    """
    data = (account_id, ticker, quantity, price, trade_id)
    update_record(query, data)
