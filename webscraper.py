from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


# WebScraper module for getting tickers of top five gainers from Yahoo Finance
class WebScraper:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.stocks = self.get_stocks()

    # method for fetching stocks
    def get_stocks(self):
        print('fetching top five stocks for today...')
        self.driver.get("https://finance.yahoo.com/gainers")
        time.sleep(3)

        # XPath for "Change" filter
        changes = self.driver.find_element_by_xpath(
            '//*[@id="scr-res-table"]/div[1]/table/thead/tr/th[4]')

        # filter by decreasing Change
        changes.click()
        time.sleep(3)
        changes.click()
        time.sleep(3)

        # get tickers for top five NYSE stocks
        stocks = []
        curr_stock_ctr = 1

        while len(stocks) != 5:

            # click stock
            curr_stock = self.driver.find_element_by_xpath(
                '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(curr_stock_ctr) + ']/td[1]/a')

            curr_stock_ticker = curr_stock.text

            curr_stock.click()

            time.sleep(5)
            while not self.page_has_loaded():
                time.sleep(5)

            # market information
            market_info = self.driver.find_element_by_xpath(
                '//*[@id="quote-header-info"]/div[2]/div[1]/div[2]/span').text

            if (market_info[0:4] == 'NYSE'):
                stocks.append(curr_stock_ticker)

            curr_stock_ctr += 1

            self.driver.execute_script("window.history.go(-1)")

            time.sleep(5)
            while not self.page_has_loaded():
                time.sleep(5)

        print('today\'s top five gainers: ' + stocks[0] + ', ' + stocks[1] +
              ', ' + stocks[2] + ', ' + stocks[3] + ', ' + stocks[4])
        self.driver.quit()

        return stocks

    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def old_get_stocks(self):
        print('fetching top five stocks for today...')
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://finance.yahoo.com/gainers")

        # XPath for "Change" filter
        changes = driver.find_element_by_xpath(
            '//*[@id="scr-res-table"]/div[1]/table/thead/tr/th[4]')

        # filter by decreasing Change
        changes.click()
        time.sleep(2)
        changes.click()
        time.sleep(2)

        # TODO: only fetch top 5 NYSE gainers
        # get tickers for top five stocks
        stocks = []
        stocks.append(driver.find_element_by_xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[1]/a').text)
        stocks.append(driver.find_element_by_xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[2]/td[1]/a').text)
        stocks.append(driver.find_element_by_xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[3]/td[1]/a').text)
        stocks.append(driver.find_element_by_xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[4]/td[1]/a').text)
        stocks.append(driver.find_element_by_xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[5]/td[1]/a').text)

        print('today\'s top five gainers: ' + stocks[0] + ', ' + stocks[1] +
              ', ' + stocks[2] + ', ' + stocks[3] + ', ' + stocks[4])
        driver.quit()

        return stocks
