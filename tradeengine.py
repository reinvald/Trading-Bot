import datetime
import time
import robin_stocks
from pprint import pprint
from alpha_vantage.timeseries import TimeSeries
from secrets import ALPHA_VANTAGE_API_KEY, ROBINHOOD_USERNAME, ROBINHOOD_PASSWORD

market_open = datetime.time(9, 30)
market_close = datetime.time(15, 30)


# module buying/selling shares, using Robinhood API
class TradeEngine:

    # init takes in today's top five stocks
    def __init__(self, stocks):
        self.login()
        self.stocks = stocks
        # keys: stocks, values: buying power allocated to stock
        self.funds = {}
        self.start_funds = self.split_funds()
        # boolean dictionary: holds number of shares, None otherwise
        self.bought = {}
        for s in stocks:
            self.bought[s] = None
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

        return buying_power

    # main loop to be run during trading hours, constantly reassessing portfolio
    def trade(self):

        # setup Alpha Vantage API for getting stock prices
        ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

        if !self.in_trading_hours():
            print('waiting for market to open...'):

        while !self.in_trading_hours():
            time.sleep(60)

        # main loop, runs every minute reevaluates portfolio/current holdings, appropriately triggering buys/sells
        while self.in_trading_hours():

            # fetch current price of each of our stocks
            for s in self.stocks:
                data, meta_data = ts.get_intraday(
                    symbol=s, interval='1min', outputsize='full')

                print('*' * 60)
                pprint(data.head(2))

                curr_price = data['4. close'][0]
                prev_price = data['4. close'][1]
                open_price = data['1. open'][0]

                # TODO: replace with Robinhood API calls
                # if bullish candle forms, purchase
                if self.bought[s] == None and curr_price > open_price:
                    self.buy(s, curr_price)

                # if we own and price starts to go down, sell
                elif self.bought[s] != None and curr_price < prev_price:
                    self.sell(s, curr_price)

            time.sleep(60)

        # sell any remaining shares, empty portfolio
        for s in self.stocks:
            data, meta_data = ts.get_intraday(
                symbol=s, interval='1min', outputsize='full')

            curr_price = data['4. close'][0]

            # if we own and price starts to go down, sell
            if self.bought[s] != None:
                self.sell(s, curr_price)

        end_funds = float(
            robin_stocks.profiles.load_account_profile()['buying_power'])

        end_funds = 0
        for s in self.stocks:
            end_funds += self.funds[s]

        # print out stats for day's trading
        print('*' * 20)
        print('trading for the day complete...')
        print('today\'s stocks: ' + str(self.stocks))
        print('starting buying power: ' + str(self.start_funds))
        print('end buying power: ' + str(end_funds))
        print('profit/loss: ' +
              str(((end_funds - self.start_funds) / self.start_funds) * 100) + '%')
        print('*' * 20)

    # buys as many shares of s as possible
    def buy(self, s, curr_price):
        print('buying ' + s + '...')
        self.bought[s] = self.funds[s] / curr_price
        self.funds[s] = 0

    # sells all shares of s
    def sell(self, s, curr_price):
        print('selling ' + s + '...')
        self.funds[s] = self.bought[s] * curr_price
        self.bought[s] = None

    # returns true if it is currently during trading hours
    def in_trading_hours(self):
        current_time = datetime.datetime.now().time()
        if (current_time >= market_open and current_time <= market_close):
            return True
        return False
