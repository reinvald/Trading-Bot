import datetime
from tradeengine import TradeEngine

# main script
if __name__ == "__main__":

    # dictionary containing all of the day's information, stored at end of day
    record = {"datetime": str((datetime.datetime.now())),
              "stocks": []}

    # start trade engine
    te = TradeEngine()
    record["stocks"] = te.stocks
