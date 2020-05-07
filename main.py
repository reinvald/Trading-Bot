# @ts-ignore
from selenium import webdriver
import time


# navigate to Yahoo Finance using Selenium ChromeDriver to get top five gainers
def get_stocks():

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

    print('today\'s stocks: ' + stocks[1] + ', ' + stocks[1] +
          ', ' + stocks[2] + ', ' + stocks[3] + ', ' + stocks[4])
    driver.quit()


if __name__ == "__main__":
    get_stocks()
