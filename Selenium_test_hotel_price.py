from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure

hotelList = []
hotelPrice = []

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.set_window_size(1800, 1200)
driver.get("http://www.kurs-selenium.pl/demo/")

driver.find_element_by_xpath("//span[@class='select2-chosen']").click()
driver.find_element_by_xpath(
    "//div[@id='select2-drop']//input[@type='text']").send_keys("dubai")
driver.find_element_by_xpath("//span[text()='Dubai']").click()

driver.find_element_by_xpath(
    "//div[@id='dpd1']//input[@class='form input-lg dpd1']").send_keys("15/07/2022")
driver.find_element_by_name("checkout").send_keys("21/07/2022")

driver.find_element_by_xpath("//input[@id='travellersInput']").click()
driver.find_element_by_xpath("//input[@name='adults']").clear()
driver.find_element_by_xpath("//input[@name='adults']").send_keys("4")
driver.find_element_by_xpath("//input[@name='child']").clear()
driver.find_element_by_xpath("//input[@name='child']").send_keys("4")
driver.find_element_by_xpath("//button[@type='submit']").click()

hotels = driver.find_elements_by_xpath(
    "//h4[contains(@class, 'list_title')]//b")
for hotel in hotels:
    hotelList.append(hotel.get_attribute("textContent"))
for hotel in hotelList:
    print("Hotel name found:", hotel)


prices = driver.find_elements_by_xpath("//div[@class='fs26 text-center']//b")
for price in prices:
    hotelPrice.append(price.get_attribute("textContent"))
for price in hotelPrice:
    print("Hotel price:", price)


@allure.title("test title")
@allure.description("test description")
def test_method():
    assert hotelList[0] == "Jumeirah Beach Hotel"
    assert hotelList[1] == "Oasis Beach Tower"
    assert hotelList[2] == "Rose Rayhaan Rotana"
    assert hotelList[3] == "Hyatt Regency Perth"

    assert hotelPrice[0] == "$22"
    assert hotelPrice[1] == "$50"
    assert hotelPrice[2] == "$80"
    assert hotelPrice[3] == "$150"


driver.quit()
