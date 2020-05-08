import datetime
import robin_stocks
from secrets import ALPHA_VANTAGE_API_KEY, ROBINHOOD_USERNAME, ROBINHOOD_PASSWORD

market_open = datetime.time(9, 30)
market_close = datetime.time(16, 00)


# module buying/selling shares, using Robinhood API
class TradeEngine:

    # init takes in today's top five stocks
    def __init__(self, stocks):
        self.login()
        self.stocks = stocks
        self.funds = {}
        self.split_funds()
        self.trade()
        self.logout()

    # login to Robinhood client
    def login(self):
        robin_stocks.login(ROBINHOOD_USERNAME, ROBINHOOD_PASSWORD)

    # logout of Robinhood client
    def logout(self):
        robin_stocks.logout()

    # returns all stocks currently in portfolio
    def get_stocks(self):
        return robin_stocks.build_holdings()

    # returns all portfolio information
    def get_portfolio(self):
        return robin_stocks.profiles.load_portfolio_profile()

    # split current buying power in account between five stocks
    def split_funds(self):
        buying_power = float(
            robin_stocks.profiles.load_account_profile()['buying_power'])

        for s in self.stocks:
            self.funds[s] = buying_power / 5

    # main loop to be run during trading hours, constantly reassessing portfolio
    def trade(self):
        while self.in_trading_hours():
            # trading strategy

            # returns true if it is currently during trading hours
    def in_trading_hours(self):
        current_time = datetime.datetime.now().time()
        if (current_time >= market_open and current_time <= market_close):
            return True
        return False
