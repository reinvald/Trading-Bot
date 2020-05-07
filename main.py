import datetime
from webscraper import WebScraper

# main script
if __name__ == "__main__":

    # dictionary containing all of the day's information, stored at end of day
    record = {"datetime": str((datetime.datetime.now())),
              "stocks": []}

    # 1.) scrape Yahoo Finance for tickers of today's top gainers
    ws = WebScraper()
    record["stocks"] = ws.stocks

    # 2.) split current balance between five stocks

    # 3.) enter main loop, reassessing portfolio/reinvesting
