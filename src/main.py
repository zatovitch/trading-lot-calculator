def calculate_lot_size(account_balance, risk_per_trade, stop_loss_pips, pip_value):
    """
    Calculate the lot size for a trade.
    
    Parameters:
    account_balance (float): The balance of the trading account.
    risk_per_trade (float): The risk per trade as a decimal (e.g., 0.02 for 2%).
    stop_loss_pips (float): The stop loss in pips.
    pip_value (float): The value of one pip for the trading instrument.
    
    Returns:
    float: The calculated lot size.
    """
    risk_amount = account_balance * risk_per_trade
    lot_size = risk_amount / (stop_loss_pips * pip_value)
    return lot_size

def get_pip_value(currency_pair):
    """
    Get the pip value for a given currency pair.
    
    Parameters:
    currency_pair (str): The currency pair (e.g., 'USDJPY').
    
    Returns:
    float: The pip value for the currency pair.
    """
    pip_values = {
        'EURUSD': 0.0001,
        'USDJPY': 0.01,
        'GBPUSD': 0.0001,
        'USDCHF': 0.0001,
        'AUDUSD': 0.0001,
        'USDCAD': 0.0001,
        'NZDUSD': 0.0001,
        'XAUUSD': 0.01  # Gold (XAUUSD) pip value
    }
    return pip_values.get(currency_pair.upper(), 0.0001)

def calculate_margin_required(lot_size, contract_size, current_price, leverage):
    """
    Calculate the margin required for a trade.
    
    Parameters:
    lot_size (float): The size of the lot.
    contract_size (float): The size of the contract (e.g., 100 ounces for gold).
    current_price (float): The current price of the instrument.
    leverage (float): The leverage used for the trade.
    
    Returns:
    float: The margin required for the trade.
    """
    return (lot_size * contract_size * current_price) / leverage

def main():
    print("Welcome to the Trading Lot Calculator")
    
    try:
        account_balance = float(input("Enter your account balance: "))
        if account_balance <= 0:
            raise ValueError("Account balance must be positive.")
        
        risk_per_trade = float(input("Enter your risk per trade (as a decimal, e.g., 0.02 for 2%): "))
        if not (0 < risk_per_trade < 1):
            raise ValueError("Risk per trade must be between 0 and 1.")
        
        stop_loss_pips = float(input("Enter your stop loss in pips: "))
        if stop_loss_pips <= 0:
            raise ValueError("Stop loss pips must be positive.")
        
        currency_pair = input("Enter your currency pair (e.g., 'USDJPY' or 'XAUUSD' for gold): ")
        pip_value = get_pip_value(currency_pair)
        
        lot_size = calculate_lot_size(account_balance, risk_per_trade, stop_loss_pips, pip_value)
        
        if currency_pair.upper() == 'XAUUSD':
            contract_size = 100  # Contract size for gold
            current_price = float(input("Enter the current price of gold: "))
            leverage = float(input("Enter your leverage (e.g., 100): "))
            
            margin_required = calculate_margin_required(lot_size, contract_size, current_price, leverage)
            
            if margin_required > account_balance:
                print(f"Insufficient balance to trade {lot_size:.2f} lots of {currency_pair}. Required margin: ${margin_required:.2f}")
            else:
                print(f"Your calculated lot size for {currency_pair} is: {lot_size:.2f}")
                print(f"Required margin: ${margin_required:.2f}")
        else:
            print(f"Your calculated lot size for {currency_pair} is: {lot_size:.2f}")
        
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()