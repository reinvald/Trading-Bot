import robin_stocks
from secrets import ALPHA_VANTAGE_API_KEY, ROBINHOOD_USERNAME, ROBINHOOD_PASSWORD


# module buying/selling shares, using Robinhood API
class TradeEngine:
    def __init__(self):
        self.login()

    def login(self):
        robin_stocks.login(ROBINHOOD_USERNAME, ROBINHOOD_PASSWORD)

    def logout(self):
        robin_stocks.logout()

    def get_stocks(self):
        return robin_stocks.build_holdings()

    def get_portfolio(self):
        return robin_stocks.profiles.load_portfolio_profile()


te = TradeEngine()
te.get_stocks()
te.logout()
