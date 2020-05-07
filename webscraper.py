from selenium import webdriver
import time


# WebScraper module for getting tickers of top five gainers from Yahoo Finance
class WebScraper:

    def __init__(self):
        self.stocks = self.get_stocks()

    # method for fetching stocks
    def get_stocks(self):
        print('fetching top five stocks for today...')
        driver = webdriver.Chrome()
        driver.get("https://finance.yahoo.com/gainers")

        # XPath for "Change" filter
        changes = driver.find_element_by_xpath(
            '//*[@id="scr-res-table"]/div[1]/table/thead/tr/th[4]')

        # filter by decreasing Change
        changes.click()
        time.sleep(2)
        changes.click()
        time.sleep(2)

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

        print('today\'s top five gainers: ' + stocks[1] + ', ' + stocks[1] +
              ', ' + stocks[2] + ', ' + stocks[3] + ', ' + stocks[4])
        driver.quit()

        return stocks
