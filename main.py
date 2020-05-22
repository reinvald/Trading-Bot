from tradeengine import TradeEngine
import caffeine

# main script
if __name__ == "__main__":

    # enable caffeine to prevent connection loss during trading
    caffeine.on(display=False)

    # start trade engine
    te = TradeEngine()

    # turn off caffeine so that system can sleep after script finishes
    caffeine.off()
